"""Finite checks for the glued safe action and overlap-deficit schedule."""

import numpy as np


def overlap_deficit(left, right, q):
    """Deficit of the normalized safe pair with a shared, orthogonal flag."""
    left_norm = float(np.vdot(left, left).real)
    right_norm = float(np.vdot(right, right).real)
    cross = np.vdot(left, right)
    common = np.sqrt((1 - q * left_norm) * (1 - q * right_norm))
    overlap = abs(common + q * cross)
    # Evaluate (1 - overlap²)/(1 + overlap) without cancellation near q = 0.
    return float(q * (left_norm + right_norm - 2 * common * cross.real
                      - q * (left_norm * right_norm + abs(cross)**2))
                 / (1 + overlap))


def flagged_pair(vacuum, left, right, q):
    return tuple(np.concatenate((np.sqrt(1 - q * np.vdot(x, x).real) * vacuum,
                                 np.sqrt(q) * x)) for x in (left, right))


def aligned_pair(pair):
    left, right = pair
    overlap = np.vdot(left, right)
    return left, right * (overlap.conjugate() / abs(overlap))


def pair_frame(pair):
    """Complete the two ordered, noncollinear states to an orthonormal frame."""
    left, right = pair
    perpendicular = right - np.vdot(left, right) * left
    pair_basis = np.column_stack((left, perpendicular / np.linalg.norm(perpendicular)))
    _, _, adjoint = np.linalg.svd(pair_basis.conj().T, full_matrices=True)
    return np.column_stack((pair_basis, adjoint.conj().T[:, 2:]))


def invert_deficit(deficit_at, target, upper, tolerance):
    assert 0 < target <= deficit_at(upper) + tolerance
    low, high = 0.0, upper
    for _ in range(60):
        mid = (low + high) / 2
        if deficit_at(mid) < target:
            low = mid
        else:
            high = mid
    q = (low + high) / 2
    assert abs(deficit_at(q) - target) < tolerance
    return q


def normalized_pair(pair):
    return tuple(state / np.linalg.norm(state) for state in pair)


def check_case(name, input_cross, output_cross, tolerance):
    vacuum, reference, h, v = np.eye(4)
    safe_b = input_cross * h + np.sqrt(1 - abs(input_cross)**2) * v
    output_b = output_cross * h + np.sqrt(1 - abs(output_cross)**2) * v
    input_basis = np.column_stack((vacuum, reference, h, safe_b))
    output_basis = np.column_stack((vacuum, reference, h, output_b))
    glued = output_basis @ np.linalg.inv(input_basis)
    _, singular_values, adjoint = np.linalg.svd(glued)
    gain = float(singular_values[0]**2)

    # The larger root of det(G_out - gain * G_in) = 0 on the exclusive span.
    input_determinant = 1 - abs(input_cross)**2
    output_determinant = 1 - abs(output_cross)**2
    linear = 1 - (output_cross * np.conj(input_cross)).real
    expected = (linear + np.sqrt(linear**2 - input_determinant * output_determinant))
    expected /= input_determinant
    assert abs(gain - expected) < tolerance
    if name == "original optical pair":
        assert abs(gain - 2) < tolerance

    coordinates = np.linalg.solve(input_basis, adjoint[0].conj())
    left = coordinates[2] * h
    right = -coordinates[3] * safe_b
    left_out = coordinates[2] * h
    right_out = -coordinates[3] * output_b
    assert np.linalg.norm(left - right) > tolerance
    assert np.linalg.norm(glued @ (left - right) - (left_out - right_out)) < tolerance

    # Check the deficit derivative even when the safe vectors have unequal norm.
    tiny_q = 1e-7
    for a, b in ((left, right), (left_out, right_out)):
        a = 0.6 * a
        derivative = np.linalg.norm(a - b)**2 / 2
        assert abs(overlap_deficit(a, b, tiny_q) / tiny_q - derivative) < 1e-7
    initial_gain = overlap_deficit(left_out, right_out, tiny_q)
    initial_gain /= overlap_deficit(left, right, tiny_q)
    assert abs(initial_gain - gain) < 1e-6

    # Invert the output deficit on the small-overlap-deficit interval.
    common = np.outer(vacuum, vacuum) + np.outer(reference, reference)
    no_event_a = np.kron(np.eye(2), common + np.outer(h, h))
    no_event_b = np.kron(np.eye(2), common + np.outer(output_b, safe_b.conj()))
    steps = 10
    terminal_q = 0.04 / max(np.vdot(x, x).real for x in (left, right))

    def output_deficit(q):
        return overlap_deficit(left_out, right_out, q)

    terminal_deficit = output_deficit(terminal_q)
    deficit = terminal_deficit
    parameters = []
    for _ in range(steps):
        q = invert_deficit(output_deficit, deficit, terminal_q, tolerance)
        parameters.append(q)
        deficit = overlap_deficit(left, right, q)
    assert all(a > b for a, b in zip(parameters, parameters[1:]))
    scaled_deficit = gain**steps * deficit / terminal_deficit
    assert 0.95 < scaled_deficit < 1.05

    def seed_histories(q):
        seed = np.concatenate((np.sqrt(1 - q) * vacuum, np.sqrt(q) * h))
        return no_event_a @ seed, no_event_b @ seed

    def seed_deficit(q):
        return 1 - abs(np.vdot(*normalized_pair(seed_histories(q))))

    seed_q = invert_deficit(seed_deficit, deficit, 0.1, tolerance)
    seeded = seed_histories(seed_q)
    seed_loss = [float(1 - np.linalg.norm(x)**2) for x in seeded]
    assert abs(seed_loss[0]) < tolerance
    assert abs(seed_loss[1] - seed_q * input_determinant) < tolerance

    # Rebuild each common unitary from the surviving states of one common seed.
    current_pair = normalized_pair(seeded)
    control_residuals = []
    for q in reversed(parameters):
        source = aligned_pair(current_pair)
        target = aligned_pair(flagged_pair(vacuum, left, right, q))
        assert abs(np.vdot(*source) - np.vdot(*target)) < tolerance
        control = pair_frame(target) @ pair_frame(source).conj().T
        assert np.linalg.norm(control.conj().T @ control - np.eye(8), 2) < tolerance
        residual = max(np.linalg.norm(control @ x - y) for x, y in zip(source, target))
        assert residual < tolerance
        control_residuals.append(float(residual))
        current_pair = (no_event_a @ (control @ source[0]),
                        no_event_b @ (control @ source[1]))
        assert max(abs(np.linalg.norm(x)**2 - 1) for x in current_pair) < tolerance
        actual_deficit = 1 - abs(np.vdot(*current_pair))
        assert abs(actual_deficit - output_deficit(q)) < tolerance

    return {"case": name, "glued_gain": gain, "expected_gain": float(expected),
            "safe_steps": steps, "initial_deficit": deficit,
            "terminal_deficit": terminal_deficit, "scaled_initial_deficit": scaled_deficit,
            "seed_input_weight": seed_q, "seed_event_probabilities": seed_loss,
            "max_common_control_residual": max(control_residuals)}


def check_safe_amplification(tolerance):
    return [check_case("original optical pair", 0.0, -1.0, tolerance),
            check_case("nonorthogonal inputs, complex output overlap", 0.6, -0.24 + 0.32j,
                       tolerance)]
