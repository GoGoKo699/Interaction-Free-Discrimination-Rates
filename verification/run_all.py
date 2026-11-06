"""Finite four-level, unconditional CPTP checks of the optical protocol.

Requires Python 3 and NumPy. Run: python3 verification/run_all.py
No environment outcomes are observed or selected. Every density update sums
all Kraus operators. Optical controls are assembled from two mode rotations.
"""

import argparse
import json
from pathlib import Path
import numpy as np

if not __debug__:
    raise SystemExit("Run without -O: this scientific check suite uses assertions.")

# h and v below are the sample modes a and b in the scientific account.


f, r, h, v = np.eye(4)


def ketbra(a, b=None):
    return np.outer(a, (a if b is None else b).conj())


Pf = ketbra(f)
Psample = ketbra(h) + ketbra(v)
Pphoton = np.eye(4) - Pf
plus, minus = (r + h) / np.sqrt(2), (r - h) / np.sqrt(2)
PiA = ketbra(plus) + (Pf + ketbra(v)) / 2
PiB = ketbra(minus) + (Pf + ketbra(v)) / 2


def rotate(a, b, theta):
    """Passive mode rotation: a -> cos(theta)a + sin(theta)b."""
    return (
        np.eye(4)
        + (np.cos(theta) - 1) * (ketbra(a) + ketbra(b))
        + np.sin(theta) * (ketbra(b, a) - ketbra(a, b))
    )


Q = rotate(h, v, -np.pi / 4)


def channels(eta=1.0):
    """eta attenuates the nominally transmitted sample polarization only."""
    common = Pf + ketbra(r)
    A = [
        common + np.sqrt(eta) * ketbra(h),
        ketbra(f, v),
        np.sqrt(1 - eta) * ketbra(f, h),
    ]
    B = [
        common - np.sqrt(eta) * ketbra(h, v),
        ketbra(f, h),
        np.sqrt(1 - eta) * ketbra(f, v),
    ]
    return A, B


def loss_channel(eta):
    """Uniform apparatus attenuation of every live one-photon mode."""
    return [Pf + np.sqrt(eta) * Pphoton] + [
        np.sqrt(1 - eta) * ketbra(f, mode) for mode in (r, h, v)
    ]


def apply(kraus, rho):
    return sum(K @ rho @ K.conj().T for K in kraus)


def weight(P, rho):
    return float(np.trace(P @ rho).real)


def trace_distance(a, b):
    return float(np.abs(np.linalg.eigvalsh(a - b)).sum() / 2)


def schedule(N, eta):
    """Precomputed controls for a known transmitted intensity eta."""
    gain = 2 * eta
    series = sum(gain**j for j in range(N))
    seed_weight = 1 / (2 + eta * series)
    c2, d2 = 1 - 2 * seed_weight, eta * seed_weight
    angles = []
    for _ in range(N - 1):
        q = d2 / (c2 + d2)
        assert -1e-14 <= q <= 0.5 + 1e-14
        angles.append(float(np.arcsin(np.sqrt(q / (1 - q)))))
        c2, d2 = c2 - d2, gain * d2
    return seed_weight, angles


def simulate(N, eta_sample=1.0, eta_loop=1.0, control_error=0.0,
             prep_error=0.0):
    seed_weight, angles = schedule(N, eta_sample)
    seed_angle = np.arcsin(np.sqrt(2 * seed_weight))
    ideal_psi = Q @ rotate(r, v, seed_angle) @ r
    psi = Q @ rotate(r, v, seed_angle + prep_error) @ r
    rho = [ketbra(psi), ketbra(psi)]
    Ks = channels(eta_sample)
    Ls = loss_channel(eta_loop)
    input_passages = [0.0, 0.0]
    transmitted_passages = [0.0, 0.0]
    apparatus_passes = [0.0, 0.0]
    sample_absorption = [0.0, 0.0]
    loop_absorption = [0.0, 0.0]
    perturbation_budget = trace_distance(ketbra(psi), ketbra(ideal_psi))
    max_unitarity_residual = 0.0

    for query in range(N):
        if query:
            ideal = Q @ rotate(r, v, angles[query - 1])
            offset = control_error * (-1 if query % 2 else 1)
            actual = Q @ rotate(r, v, angles[query - 1] + offset)
            perturbation_budget += float(np.linalg.norm(actual - ideal, 2))
            max_unitarity_residual = max(
                max_unitarity_residual,
                float(np.linalg.norm(actual.conj().T @ actual - np.eye(4), 2)),
            )
            rho = [actual @ x @ actual.conj().T for x in rho]

        for x in range(2):
            input_passages[x] += weight(Psample, rho[x])
            apparatus_passes[x] += weight(Pphoton, rho[x])
            sample_absorption[x] += sum(
                float(np.trace(K @ rho[x] @ K.conj().T).real)
                for K in Ks[x][1:]
            )
            rho[x] = apply(Ks[x], rho[x])
            transmitted_passages[x] += weight(Psample, rho[x])
            loop_absorption[x] += (1 - eta_loop) * weight(Pphoton, rho[x])
            rho[x] = apply(Ls, rho[x])

    pe = (weight(PiB, rho[0]) + weight(PiA, rho[1])) / 2
    helstrom = (1 - trace_distance(rho[0], rho[1])) / 2
    survival = eta_loop**N * (2 * eta_sample)**N * seed_weight
    target = [survival * ketbra(plus) + (1 - survival) * Pf,
              survival * ketbra(minus) + (1 - survival) * Pf]
    return {
        "N": N,
        "eta_sample": eta_sample,
        "eta_loop": eta_loop,
        "seed_weight": seed_weight,
        "sample_absorption": sample_absorption,
        "loop_absorption": loop_absorption,
        "final_vacuum": [weight(Pf, x) for x in rho],
        "sample_input_passages": input_passages,
        "sample_transmitted_passages": transmitted_passages,
        "whole_apparatus_query_occupancy": apparatus_passes,
        "binary_error": pe,
        "helstrom_error": helstrom,
        "analytic_error": (1 - survival) / 2,
        "max_final_state_residual": max(
            float(np.linalg.norm(x - y, 2)) for x, y in zip(rho, target)
        ),
        "max_unitarity_residual": max_unitarity_residual,
        "control_perturbation_budget": perturbation_budget,
        "states": rho,
    }


def summary(row):
    return {key: value for key, value in row.items() if key != "states"}


def check():
    tolerance = 5e-12
    for eta in (1.0, 0.9, 0.5):
        for kraus in channels(eta):
            assert np.linalg.norm(sum(K.conj().T @ K for K in kraus)
                                  - np.eye(4), 2) < tolerance

    ideal_rows = []
    for N in (1, 2, 4, 8, 12, 20):
        row = simulate(N)
        p = 1 / (2**N + 1)
        assert row["max_final_state_residual"] < tolerance
        assert abs(row["binary_error"] - p / 2) < tolerance
        assert abs(row["helstrom_error"] - p / 2) < tolerance
        for value in row["sample_absorption"]:
            assert abs(value - p) < tolerance
        for value in row["sample_input_passages"]:
            assert abs(value - (1 - p)) < tolerance
        for value in row["sample_transmitted_passages"]:
            assert abs(value - (1 - 2 * p)) < tolerance
        for value in row["whole_apparatus_query_occupancy"]:
            assert abs(value - (N - (N - 1) * p)) < tolerance
        ideal_rows.append(summary(row))

    loop_rows = []
    for N, eta in ((4, 0.99), (10, 0.99), (20, 0.99), (10, 0.9)):
        row = simulate(N, eta_loop=eta)
        p = 1 / (2**N + 1)
        expected = (1 - eta**N * (1 - p)) / 2
        assert row["max_final_state_residual"] < tolerance
        assert abs(row["binary_error"] - expected) < tolerance
        assert max(abs(x - p) for x in row["sample_absorption"]) < tolerance
        loop_rows.append(summary(row))

    sample_rows = []
    for N, eta in ((4, 0.9), (10, 0.9), (20, 0.9), (10, 0.75),
                   (5, 0.6), (5, 0.5), (5, 0.25)):
        row = simulate(N, eta_sample=eta)
        assert row["max_final_state_residual"] < tolerance
        assert abs(row["binary_error"] - row["analytic_error"]) < tolerance
        for value in row["sample_absorption"]:
            assert abs(value - 2 * row["analytic_error"]) < tolerance
        sample_rows.append(summary(row))

    perturbation_rows = []
    for N in (4, 8, 12):
        base = simulate(N)
        pert = simulate(N, control_error=1e-4, prep_error=1e-4)
        budget = pert["control_perturbation_budget"]
        distances = [trace_distance(x, y) for x, y in
                     zip(base["states"], pert["states"])]
        assert max(distances) <= budget + tolerance
        assert abs(pert["binary_error"] - base["binary_error"]) <= budget + tolerance
        assert max(abs(a - b) for a, b in
                   zip(pert["sample_absorption"], base["sample_absorption"])) <= budget + tolerance
        perturbation_rows.append({
            "N": N,
            "operator_norm_budget": budget,
            "final_trace_distances": distances,
            "actual_absorption": pert["sample_absorption"],
            "ideal_absorption": base["sample_absorption"],
            "actual_error": pert["binary_error"],
            "ideal_error": base["binary_error"],
        })

    # The local counterexample must retain its off-diagonal overlap defect.
    A, B = channels()
    defect = np.eye(4) - A[0].conj().T @ B[0]
    cross = ketbra(h) @ defect @ ketbra(v)
    assert abs(np.linalg.norm(cross, 2) - 1) < tolerance
    counterexamples = []
    for q in (0.0625, 0.125, 0.25):
        xa = np.sqrt(1 - q) * r + np.sqrt(q) * h
        xb = np.sqrt(1 - q) * r + np.sqrt(q) * v
        fin = abs(np.vdot(xa, xb))
        fout = abs(np.vdot(A[0] @ xa, B[0] @ xb))
        diagonal_rhs = sum(np.sqrt(weight(P, ketbra(xa)) * weight(P, ketbra(xb)))
                           for P in (ketbra(h), ketbra(v)))
        assert abs(fin - fout - q) < tolerance
        assert diagonal_rhs == 0
        counterexamples.append({"q": q, "root_fidelity_drop": float(fin - fout),
                                "diagonal_rhs": float(diagonal_rhs)})
    PA = Pf + ketbra(r) + ketbra(h)
    PB = Pf + ketbra(r) + ketbra(v)
    projector_defect = np.eye(4) - PA @ PB
    assert np.linalg.norm(PA @ projector_defect @ PB, 2) < tolerance

    # Check the model-specific fixed-transparency-loss converse on these examples.
    for row in sample_rows:
        eta = row["eta_sample"]
        pe = row["binary_error"]
        m = (np.sqrt(4 + eta * eta) + eta) / 2
        floor = (1 - eta) / m * (1 - 2 * np.sqrt(pe * (1 - pe)))
        assert np.sqrt(np.prod(row["sample_absorption"])) + tolerance >= floor

    return {"status": "all assertions passed", "ideal": ideal_rows,
            "omitted_cross_block": counterexamples,
            "uniform_loop_loss": loop_rows, "known_sample_loss": sample_rows,
            "coherent_control_perturbations": perturbation_rows}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, help="write the detailed JSON observations")
    args = parser.parse_args()
    result = check()
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, indent=2) + "\n")
    summary = {"status": result["status"],
               "cases": {k: len(v) for k, v in result.items() if isinstance(v, list)},
               "largest_ideal_state_residual": max(x["max_final_state_residual"] for x in result["ideal"]),
               "note": "Finite checks support the implementation; written proofs establish the general claims."}
    print(json.dumps(summary, indent=2))
