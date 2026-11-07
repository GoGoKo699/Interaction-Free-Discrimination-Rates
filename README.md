# Interaction-Free Discrimination Rates

**How quickly can repeated quantum interrogation identify a device while suppressing absorption?** For two fixed lossy devices, one photon and N preprogrammed interrogations achieve exponentially small absorption and unconditional discrimination error:

```math
P_{\mathrm{abs}}^{A}=P_{\mathrm{abs}}^{B}
=\frac{1}{2^N+1},\qquad
P_{\mathrm{error}}=\frac{1}{2(2^N+1)}.
```

The device is promised to be one of two known filters. Each has a perfectly transparent input mode; one also rotates its transmitted output. A first weak interrogation creates a small difference between the possible surviving states. Subsequent common controls place each possibility in its corresponding transparent space. Further queries amplify their separation without additional absorption on surviving histories. The final photon states are orthogonal, while a lost photon contributes a fair binary guess. Every run is counted.

The protocol uses three one-photon modes, an absorbing vacuum and no access to the device's environment. The controls depend on the query number and the known pair, and are identical under the two unknown hypotheses. At **exactly zero absorption**, any finite-query strategy for this pair has identical outputs and error one half, even with arbitrary ancillary memory and adaptive control.

## The rate depends on safe input and output actions

Orthogonal transparent input directions do not by themselves force an inverse-N absorption law. The construction satisfies the written hypotheses of Hasenöhrl and Wolf's rate theorem but violates its conclusion. A direct one-query counterexample identifies omitted cross terms in its supporting multiblock fidelity estimate. Their channel framework and general feasibility results remain separately credited in [Related work](references/RELATED_WORK.md).

A corrected sufficient condition is also proved: **if the two safe actions preserve all cross inner products, an inverse-N lower bound holds** for arbitrary causal strategies and memories. On the same finite input/output space, this means that one unitary can extend both safe restrictions. The exponential pair fails this condition because its orthogonal transparent inputs have overlapping outputs.

| Statement | Scope |
|---|---|
| Exponential absorption and error | Explicit ideal protocol, every integer $`N\ge1`$ |
| No informative exactly zero-absorption strategy | Every finite query count, arbitrary common causal controls and ancillary memory |
| Inverse-N lower bound under compatible safe actions | Sufficient geometric condition; not a complete classification |
| Imperfection accounting | Sufficient precision budget, exact uniform apparatus-loss formula and a fixed sample-loss damage floor |

## Read the science

Start with the [question, model and exact claims](science/model.md), then follow the [explicit construction](science/exponential_protocol.md), [zero-absorption obstruction](science/zero_absorption.md), [rate geometry](science/rate_geometry.md) and [resource interpretation](science/resources.md).

| To inspect | Read |
|---|---|
| Physical channels, event definition and unconditional error | [Model](science/model.md) |
| Seed, common controls and exact output states | [Exponential protocol](science/exponential_protocol.md) |
| The finite exact-zero impossibility proof | [Zero absorption](science/zero_absorption.md) |
| Published cross-term issue and repaired fidelity/rate bounds | [Rate geometry](science/rate_geometry.md) |
| Passive rotations, passage, calibration and loss | [Resources and imperfections](science/resources.md) |
| Inherited tools and nearby operational tasks | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Full-channel calculations and their limits | [Verification](verification/README.md) |

## Learn the project

The single educational anchor is **John Watrous, *Understanding Quantum Information and Computation*, the author’s July 2025 “Director’s Cut.”** The [Watrous bridge](learning/BRIDGE.md) identifies the relevant lessons, translates their notation into this experiment, and works through a complete two-query example. It then connects the example to the exact protocol, the fidelity argument and the physical resource limits.

The [30-milestone map](learning/MILESTONES.md) develops the project in two phases: **13 background/preliminaries milestones** establish the operational framework, and **17 narrative/innovation milestones** connect the protocol, rate arguments and physical boundaries. Each phase moves from individual objects and mechanisms to their combined meaning. Every milestone states its understanding target, dependencies, conceptual connection and source pointers.

Use the bridge alongside the map for self-directed study. [The LLM reading guide](llms.txt) maps scientific and learning questions to their authoritative files. Specialists can follow the direct proof route above.

## Reproduce the finite checks

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The suite propagates full density matrices through every Kraus branch, constructs controls from two-mode rotations, and checks the output states, unconditional error, absorption, passage totals, loss models and the omitted-cross-block counterexample. The written proofs establish the all-N and arbitrary-strategy claims; finite numerical agreement does not replace them.

## Physical scope

Expected sample-input passage tends to one even though absorption falls exponentially. Whole-apparatus occupancy grows approximately as N. The result concerns absorbed energy and environmental disturbance, not vanishing traversal.

Exact transparent modes and calibrated controls are essential idealizations. A sufficient absolute precision schedule shrinks as $`2^{-N}/N`$ per operation. Fixed loss in the transparent sample modes creates a positive damage floor, and fixed uniform apparatus loss eventually destroys the discrimination advantage. No optimal exponential base, general classification or experimental demonstration is claimed.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
