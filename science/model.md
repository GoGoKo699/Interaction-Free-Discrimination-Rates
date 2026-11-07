# Question, model and results

Can repeated interrogation identify a lossy device while making the probability of absorption exponentially small in the number of calls? The answer is yes for a fixed pair of devices whose transparent input modes differ and whose transparent outputs rotate into the same mode. The same pair carries no information at exactly zero absorption for any finite number of calls.

The physical cost here is an absorbed photon, or equivalently an environmental record different from the vacuum record. A transmitted photon can still acquire a phase or change polarization. This cost therefore does not measure whether light ever traverses the sample. The distinction is quantified in [Resources and imperfections](resources.md).

## Operational experiment

The unknown device is one of two known, fixed, memoryless channels, with equal prior probabilities. A strategy makes an integer number $`N\ge1`$ of forward calls. Between calls it may apply common controls that depend on the known pair, the call number and $`N`$. The controls do not depend on the unknown identity. The general bounds permit ancillary systems, intermediate measurements, classical records and adaptive causal control, represented together as channels on a memory.

The explicit construction needs one photon, three one-photon modes and a final measurement. It does not observe the device's environment or condition its subsequent controls on photon survival. A fresh environment for each use is part of the memoryless channel model.

Use the orthonormal basis $`\{f,r,a,b\}`$. Here $`f`$ is the physical vacuum, $`r`$ is a reference path bypassing the sample, and $`a,b`$ are two sample modes. In ket notation, the two channels are

```math
\mathcal X(\rho)=X_0\rho X_0^\dagger+X_1\rho X_1^\dagger,
\qquad X\in\{A,B\}.
```

The operators are

```math
\begin{aligned}
A_0&=|f\rangle\langle f|+|r\rangle\langle r|+|a\rangle\langle a|,
& A_1&=|f\rangle\langle b|,\\
B_0&=|f\rangle\langle f|+|r\rangle\langle r|-|a\rangle\langle b|,
& B_1&=|f\rangle\langle a|.
\end{aligned}
```

Both Kraus sums satisfy $`\sum_{j=0}^1X_j^\dagger X_j=I`$. Device A transmits mode a and absorbs b. Device B transmits b into minus a and absorbs a. Both fix the reference mode and vacuum.

The Stinespring isometry $`V_X\psi=X_0\psi\otimes|0\rangle_E+X_1\psi\otimes|1\rangle_E`$ identifies the environmental no-absorption state $`|0\rangle_E`$ and absorption state $`|1\rangle_E`$. This isometry is a model of the device, not an extra control available to the experimenter. The environment is traced out.

## Absorption, error and safe spaces

For an arbitrary strategy, let $`\widetilde\rho_{X,N}`$ be its subnormalized final state obtained by retaining only the no-event operation $`\rho\mapsto X_0\rho X_0^\dagger`$ at every call. Define

```math
p_X=1-\mathrm{tr}\,\widetilde\rho_{X,N}.
```

This is the probability of at least one absorption event. It is not generally a count of all events. In the explicit number-preserving protocol, absorption leaves the system in f forever, so the expected absorbed-photon count equals $`p_X`$ as well.

Write $`\rho_A,\rho_B`$ for the full normalized accessible outputs, including all event branches. Their optimal equal-prior binary error is the Helstrom error,

```math
e_* =\frac{1-D(\rho_A,\rho_B)}{2},\qquad
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
```

The safe input space of a no-event contraction $`K_X`$ is $`S_X=\ker(I-K_X^\dagger K_X)`$. For this pair,

```math
S_A=\mathrm{span}\{f,r,a\},\qquad
S_B=\mathrm{span}\{f,r,b\},\qquad
S_A\cap S_B=\mathrm{span}\{f,r\}.
```

The channels coincide on their common safe space. Their exclusive safe input directions a and b are orthogonal, but their safe outputs a and minus a are not orthogonal. That change of cross inner products is the useful geometric feature.

## Exact claims and their homes

| Result | Precise scope | Proof |
|---|---|---|
| Exponential absorption and error | For every integer N, the explicit protocol has absorption $`p_N=(2^N+1)^{-1}`$ under either device and unconditional error $`p_N/2`$ | [Exponential protocol](exponential_protocol.md) |
| Exact zero absorption gives no information | For every finite N, arbitrary common causal controls and ancillary memory, zero absorption under both hypotheses gives identical outputs | [Zero-absorption obstruction](zero_absorption.md) |
| A sufficient inverse-N condition | Safe actions that preserve every cross inner product obey a quantitative inverse-N lower bound, with arbitrary memory and adaptive controls | [Rate geometry](rate_geometry.md) |
| Specific published rate claim fails | The pair satisfies the written hypotheses of Hasenöhrl–Wolf Theorem 5.9; a one-query counterexample isolates the omitted cross terms in Proposition 5.2 | [Rate geometry](rate_geometry.md#the-published-multiblock-step) |
| Resource and noise accounting | Exact sample passage, sufficient control accuracy, and the consequence of uniform apparatus loss | [Resources and imperfections](resources.md) |

The exponential base is achieved by this construction; global optimality is not claimed. The sufficient inverse-N condition is not a complete classification of all channel pairs. The exact transparent modes, known binary device promise and ideal calibrated controls are assumptions of the result. [Related work](../references/RELATED_WORK.md) identifies inherited results and the different operational tasks in nearby literature.

## Reading route

Read the [construction](exponential_protocol.md), then the [zero-cost obstruction](zero_absorption.md), and then the [rate geometry](rate_geometry.md). The [resource account](resources.md) explains which physical advantages survive the definition of cost. The [verification guide](../verification/README.md) separates finite computational checks from the analytic proofs.
