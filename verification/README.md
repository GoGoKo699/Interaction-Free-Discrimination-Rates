# Reproduce the finite checks

The analytic statements live in [science/](../science/model.md). This suite verifies that an explicit implementation of the physical channels and passive controls reproduces the stated finite examples, including every absorption branch.

## Run

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

Use ordinary Python execution, without `-O`. The script rejects optimized execution because its numerical checks use assertions. NumPy is the only external dependency; [requirements.txt](requirements.txt) records the version used for validation. To retain detailed values:

```bash
python3 verification/run_all.py --report verification-results.json
```

The default output is a compact pass/fail summary. The optional report contains the tested parameters, physical probabilities, passage totals and residuals. Floating-point residuals can vary slightly across platforms; the explicit tolerance is $`5\times10^{-12}`$.

## What is checked

| Check | Cases and assertion |
|---|---|
| Ideal full CPTP evolution | N = 1, 2, 4, 8, 12, 20; exact final-state formula, absorption, binary error, Helstrom error and passage identities |
| Omitted cross block | q = 1/16, 1/8, 1/4; positive root-fidelity drop with zero diagonal-only bound |
| Compatible projector actions | The safe cross defect vanishes for projector no-event operators |
| Uniform whole-apparatus loss | Four combinations of query count and survival; exact survival/error and distinct sample-loss probability |
| Known transparent-mode loss | Seven combinations, including transmission above, at and below one half; compensated-schedule output and the model-specific damage bound |
| Coherent preparation/control errors | N = 4, 8, 12; actual state, error and absorption changes stay inside the norm budget |

The code labels the two sample polarizations h and v; these are a and b in the scientific account. It builds each common control as two passive rotations and updates the physical density matrix by summing all Kraus terms. The closed-form output states are a separate comparison. The binary measurement assigns a fair guess to vacuum; the Helstrom value is also computed from the full output density matrices.

The sample-transmission parameter and apparatus-transmission parameter describe different loss channels. The compensated schedule for imperfect sample transmission is derived in [Resources and imperfections](../science/resources.md#loss-in-the-nominally-transparent-sample-modes); its gain is not silently substituted into the ideal claim.

## Expected result and limits

A successful run reports `all assertions passed`, with 6 ideal, 3 cross-block, 4 uniform-loss, 7 sample-loss and 3 control-perturbation cases. It also reports the largest ideal output-state residual. The tested ideal values are well above the floating-point absorption floor.

These checks do not prove a universal or asymptotic result, establish the optimal exponential base, test arbitrary adaptive controllers, certify laboratory components, or verify literature priority. The exact construction, zero-event induction, general fidelity estimates and fixed-loss converse are established by the written proofs. The suite provides a reproducible implementation check alongside them.
