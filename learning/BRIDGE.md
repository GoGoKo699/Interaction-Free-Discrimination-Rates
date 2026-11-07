# From Watrous's course to low-absorption discrimination

Imagine sending one photon through an apparatus containing an unknown optical device. The device is promised to be one of two known alternatives, A or B. The aim is to identify it while keeping the probability that it absorbs the photon small. Reusing the apparatus permits more calls to the device, but a useful protocol must account for every lost photon and every incorrect answer.

The [project's model](../science/model.md) makes this question precise. The complete two-call experiment below has absorption probability one fifth and binary error one tenth. Its generalization achieves exponentially decreasing absorption with the number of calls. Understanding why requires keeping track of the device's transparent **outputs**, the inaccessible absorption record, and the full final state.

## Source and route

The selected educational anchor is **John Watrous, [Understanding Quantum Information and Computation](https://jhwatrous.github.io/UQIC.pdf)**, the author-hosted **Director's Cut whose preface is dated July 2025**. The [author's course page](https://jhwatrous.github.io/books-and-courses.html) links the written source and accompanying videos. The section references below refer to that PDF; printed page numbers are six smaller than PDF page numbers.

Use the relevant sections alongside this bridge. The [30-milestone map](MILESTONES.md) supplies the project's dependency order and understanding targets; it does not require reading the entire course first.

| Question in this project | Relevant part of the selected source | Connection supplied here |
|---|---|---|
| What are amplitudes, basis states and reversible controls? | Lesson 1, **Single Systems**, [§1.2, Quantum information](https://jhwatrous.github.io/UQIC.pdf#page=18), p. 12; Lesson 2, **Multiple Systems**, [§2.2, Quantum information](https://jhwatrous.github.io/UQIC.pdf#page=49), p. 43, as needed for joint systems | One photon occupies a superposition of modes; a common unitary acts on both possible states. |
| How do surviving and absorbed runs form one state? | Lesson 9, **Density Matrices**: [§9.1, Density matrix basics](https://jhwatrous.github.io/UQIC.pdf#page=262), p. 256, and [§9.2, Convex combinations of density matrices](https://jhwatrous.github.io/UQIC.pdf#page=268), p. 262 | The surviving photon and the vacuum contribute to one normalized density matrix. |
| What happens to an inaccessible environment? | [§9.4, Multiple systems and reduced states](https://jhwatrous.github.io/UQIC.pdf#page=281), p. 275; the partial-trace discussion starts on [p. 279](https://jhwatrous.github.io/UQIC.pdf#page=285) | Tracing out the absorption record removes coherence between distinct recorded outcomes. It does not remove their probabilities. |
| How can a device transmit one mode and absorb another? | Lesson 10, **Quantum Channels**: [§10.1, Quantum channel basics](https://jhwatrous.github.io/UQIC.pdf#page=294), p. 288, and [§10.2, Channel representations](https://jhwatrous.github.io/UQIC.pdf#page=302), p. 296; especially Stinespring representations on p. 297 and Kraus representations on p. 304 | The two Kraus operators describe no absorption and absorption. Their sum gives the full channel. |
| Which final readout gives the best binary answer? | Lesson 11, **General Measurements**: [§11.1, Mathematical formulations of measurements](https://jhwatrous.github.io/UQIC.pdf#page=327), p. 321, and [§11.3, Quantum state discrimination and tomography](https://jhwatrous.github.io/UQIC.pdf#page=347), p. 341 | The final measurement distinguishes two output density matrices; the Helstrom–Holevo formula includes vacuum runs. |
| Why may general controls be analyzed using larger pure states? | Lesson 12, **Purifications and Fidelity**: [§12.1, Purifications](https://jhwatrous.github.io/UQIC.pdf#page=355), p. 349 | Purifying preparation and retaining control registers supports proofs for arbitrary ancillary memory. |
| How does an overlap bound constrain discrimination? | [§12.2, Fidelity](https://jhwatrous.github.io/UQIC.pdf#page=368), p. 362; basic inequalities on p. 365 and Uhlmann's theorem on p. 369 | These tools enter the general rate bounds, after the explicit construction is understood. |

The foundations are organized in [M01–M13](MILESTONES.md#m01); [M14](MILESTONES.md#m14) begins the narrative about this particular pair of devices.

## From states to recorded absorption

A ket such as $`|r\rangle`$ denotes a vector representing a physical state. A coefficient multiplying a basis vector is an amplitude; its absolute square is the probability of that basis outcome. A normalized pure state has squared amplitudes summing to one. The four orthogonal basis states in this project have the following meanings and device actions.

| Input basis state | Physical meaning | Device A | Device B |
|---|---|---|---|
| f | No photon: physical vacuum | Leaves f unchanged | Leaves f unchanged |
| r | One photon in the reference path that bypasses the sample | Transmits r unchanged | Transmits r unchanged |
| a | One photon in the first sample mode | Transmits a unchanged | Absorbs the photon, leaving f |
| b | One photon in the second sample mode | Absorbs the photon, leaving f | Transmits b into minus a |

The minus sign in B's transmitted output matters relative to the unchanged reference amplitude. Although a sign on an isolated ket is an unobservable global phase, a sign on one component of a superposition changes interference.

The [canonical model](../science/model.md#operational-experiment) gives the four Kraus matrices. Write $`K_X=X_0`$ for the no-absorption operator and $`L_X=X_1`$ for the absorption operator, where $`X\in\{A,B\}`$. The density matrix is the matrix that predicts all measurement probabilities; for a pure state it is $`\rho=|\psi\rangle\langle\psi|`$. One device call gives

```math
\mathcal X(\rho)=K_X\rho K_X^\dagger+L_X\rho L_X^\dagger,
\qquad K_X^\dagger K_X+L_X^\dagger L_X=I.
```

The dagger denotes the conjugate transpose. The second identity ensures that total probability remains one. The first term alone is generally **subnormalized**: its trace is the probability of no absorption, rather than necessarily one. Dividing it by that trace describes the normalized state conditional on survival. The physical output retains both terms.

The environment makes the meaning of these terms explicit:

```math
V_X|\psi\rangle
=K_X|\psi\rangle\otimes|0\rangle_E
 +L_X|\psi\rangle\otimes|1\rangle_E.
```

Here the two environment states record no absorption and absorption. The experimenter cannot read or manipulate them. Tracing out E yields the channel above because the two records are orthogonal. This is the source's Stinespring construction specialized to the device. Watrous writes the initialized workspace first in the tensor product in §10.2; the display here puts the optical system first. This ordering choice changes no probabilities.

Kraus representations of a channel need not be unique, as the source explains. The damage statistic here refers to the **specified physical absorption record**. An arbitrary mathematical change of Kraus representation does not redefine that physical cost. The no-event branch is a calculation tool; the subsequent optical controls are applied without observing survival. See [M06–M07](MILESTONES.md#m06).

## Notation and assumptions

| Source notation or concept | Translation into this project |
|---|---|
| X and Y name physical systems | The optical space has basis f, r, a, b. In the scientific pages, X in a subscript often labels the hypothesis A or B. |
| A collection of Kraus matrices represents one channel | Here A and B name different devices; A₀, A₁ and B₀, B₁ are their respective Kraus matrices. In the general proofs, K denotes the specified no-event operator. |
| N in the Kraus formula counts matrices | Here N counts calls to the unknown device. Each of the explicit devices has two Kraus matrices for every N. |
| p in §11.3 is a prior probability | The two device priors here are fixed at one half. The symbol $`p_N`$ means absorption probability, and $`s_N=1-p_N`$ means survival probability. |
| A density matrix has trace one | A tilde or an explicitly unnormalized no-event vector retains its branch weight. Its trace or squared norm is a probability. The parameter $`q_j`$ is a sample-mode weight **within the normalized surviving state**, not the loss probability. |
| General measurement matrices are positive and sum to identity | A final effect E gives outcome probability $`\mathrm{tr}(E\rho)`$. The complete readout below includes vacuum. |
| Fidelity is unsquared in §12.2 | The project uses the same convention, called root fidelity in its proofs. The same formula is also used for positive subnormalized operators, without adding a failure-probability term. |

In particular,

```math
F(R,S)=\|\sqrt R\sqrt S\|_1,
\qquad
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
```

The trace norm is the sum of singular values; for a Hermitian matrix it is the sum of absolute eigenvalues. F is an overlap measure, whereas the two-argument D is trace distance. The [rate-geometry page](../science/rate_geometry.md#notation-and-the-environmental-event) also uses the single letter D for a **cross-defect operator**; that is a different object, defined there. Watrous's fidelity conventions and trace-norm formula are stated on [pp. 363–365](https://jhwatrous.github.io/UQIC.pdf#page=369).

The unknown label is chosen once, and the same fixed, known pair is used throughout. Every call has a fresh environment. Controls may depend on the known pair, N and the query number; they cannot depend on the hidden label. In the explicit protocol they are predetermined, preserve photon number and fix f. Perfect transparent modes and ideal calibration are assumptions. The general impossibility and rate theorems allow additional memory, intermediate measurements and common adaptive control; the elementary construction does not need those resources.

## A complete two-query experiment

This is the finite example supporting [M18](MILESTONES.md#m18). It uses the definitions above and the special case $`N=2`$ of the [general protocol](../science/exponential_protocol.md).

### 1. Prepare the photon and make the first call

Prepare

```math
|\psi_2\rangle
=\frac{\sqrt3|r\rangle+|a\rangle+|b\rangle}{\sqrt5}.
```

Its squared amplitudes are three fifths in the reference path and one fifth in each sample mode. A absorbs the b component; B absorbs the a component. Thus either device absorbs with probability one fifth. The unnormalized no-absorption outputs are

```math
K_A|\psi_2\rangle=\frac{\sqrt3|r\rangle+|a\rangle}{\sqrt5},
\qquad
K_B|\psi_2\rangle=\frac{\sqrt3|r\rangle-|a\rangle}{\sqrt5}.
```

Both have squared norm four fifths. Dividing by the square root of four fifths gives the normalized surviving pair

```math
|y_+\rangle=\frac{\sqrt3}{2}|r\rangle+\frac12|a\rangle,
\qquad
|y_-\rangle=\frac{\sqrt3}{2}|r\rangle-\frac12|a\rangle.
```

The full state under A is four fifths of the density matrix of $`|y_+\rangle`$ plus one fifth of the vacuum density matrix; under B replace the plus state by the minus state. These are alternatives in the calculation, not instructions to select a different control after learning the device's identity.

### 2. Apply one common control

Define U on the complete basis by

```math
\begin{aligned}
U|f\rangle&=|f\rangle,\\
U|r\rangle&=\sqrt{\frac23}|r\rangle
             +\frac{|a\rangle+|b\rangle}{\sqrt6},\\
U|a\rangle&=\frac{|a\rangle-|b\rangle}{\sqrt2},\\
U|b\rangle&=-\frac{|r\rangle}{\sqrt3}
             +\frac{|a\rangle+|b\rangle}{\sqrt3}.
\end{aligned}
```

The four displayed output columns are orthonormal, so U is unitary. It is exactly $`U_{1/4}`$ in the general construction. Substitution gives

```math
U|y_+\rangle=\frac{|r\rangle+|a\rangle}{\sqrt2},
\qquad
U|y_-\rangle=\frac{|r\rangle+|b\rangle}{\sqrt2}.
```

The first state occupies only modes safe for A, and the second occupies only modes safe for B. The same U achieves both transformations. Their inner product is one half before U and one half afterward, as a unitary requires. This is the two-state Gram-matrix condition: the pair's norms and mutual inner product agree.

### 3. Make the second call and retain every branch

A leaves its surviving input unchanged. B turns its b component into minus a. Neither surviving input has any amplitude in its own device's absorbing mode, so this call has zero additional absorption probability. The normalized surviving outputs are

```math
|+\rangle=\frac{|r\rangle+|a\rangle}{\sqrt2},
\qquad
|-\rangle=\frac{|r\rangle-|a\rangle}{\sqrt2},
\qquad \langle+|-\rangle=0.
```

Any photon absorbed on the first call remains in f throughout U and the second call. Consequently the full normalized outputs are

```math
\rho_A=\frac45|+\rangle\langle+|+\frac15|f\rangle\langle f|,
\qquad
\rho_B=\frac45|-\rangle\langle-|+\frac15|f\rangle\langle f|.
```

### 4. Measure and give a binary answer

Measure in the complete orthonormal basis $`\{|+\rangle,|-\rangle,|b\rangle,|f\rangle\}`$. A balanced interferometer mixing r and a resolves the plus and minus states. Report A on plus and B on minus. On vacuum, use a fair binary guess. The unused b outcome has probability zero in the ideal experiment; a fair guess on that outcome completes the rule as well.

| Actual device | Plus outcome | Minus outcome | b outcome | Vacuum outcome |
|---|---:|---:|---:|---:|
| A | 4/5 | 0 | 0 | 1/5 |
| B | 0 | 4/5 | 0 | 1/5 |

All detected photons are identified correctly, while the vacuum guess is wrong half the time. Therefore

```math
p_2=\frac15,
\qquad
e_* =\frac15\,\frac12=\frac1{10}.
```

This readout is optimal for these outputs. The eigenvalues of $`\rho_A-\rho_B`$ are four fifths, minus four fifths and two zeros, so its trace norm is eight fifths. The source's [Helstrom–Holevo formula](https://jhwatrous.github.io/UQIC.pdf#page=349), with equal priors and correctness converted to error, gives

```math
e_* =\frac12-\frac14\|\rho_A-\rho_B\|_1
     =\frac12-\frac14\,\frac85
     =\frac1{10}.
```

The output error is thus unconditional. Calling vacuum inconclusive would describe a different reporting convention; it would not erase the one-fifth probability of absorption.

## From two queries to the general result

The control in the example preserves the overlap one half. The following device call changes it to zero because **different channels act under the two hypotheses**. There is no conflict with the source's statement that fidelity cannot decrease under one common channel. In particular, the safe input directions a and b have inner product zero, while their respective safe outputs a and minus a have inner product minus one.

The general [construction](../science/exponential_protocol.md#2-a-common-control-sends-both-possibilities-to-their-own-safe-spaces) repeats this mechanism. Write a normalized surviving pair as

```math
|y_\pm(q)\rangle
=\sqrt{1-q}|r\rangle\pm\sqrt q|a\rangle,
\qquad \langle y_+(q)|y_-(q)\rangle=1-2q.
```

A common control sends the two possibilities into their respective safe spaces. One device call then turns q into 2q without further absorption. The quantity that doubles is this squared sample amplitude, or equivalently the overlap deficit; the trace distance itself does not double. Choosing the seed so that $`q_1=2^{-N}`$ gives

```math
q_j=2^{j-N-1},\qquad q_N=\frac12,
\qquad
p_N=\frac1{2^N+1},\qquad e_* =\frac{p_N}{2}.
```

The [canonical proof](../science/exponential_protocol.md) establishes these identities for every integer $`N\ge1`$, including all event branches. The two-call calculation is a concrete instance, not a substitute for that proof. [M15–M18](MILESTONES.md#m15) connect the seed, common control, recurrence and full output.

Exactly zero absorption at a finite N has a different consequence. Before any separation has been created, the shared input would need to lie in both safe spaces. On their intersection, spanned by f and r, the devices agree. Common controls cannot turn equal states into different states, and imposing zero absorption at every subsequent call keeps this obstruction in place. The [finite-query theorem](../science/zero_absorption.md) makes this argument precise even with ancillary memory and adaptive controls. Every member of the exponential sequence has a strictly positive first-call risk.

The [sufficient inverse-N theorem](../science/rate_geometry.md#a-sufficient-inverse-n-theorem) identifies a complementary class of device pairs: their safe actions preserve all cross inner products, or equivalently extend to one common unitary after the prescribed vacuum phase alignment. Such pairs require absorption of order at least inverse N for fixed discrimination advantage. Our pair violates that compatibility condition. Its failure alone does not establish an exponential protocol for every other pair; a necessary-and-sufficient rate classification is not supplied. See [M23–M24](MILESTONES.md#m23).

## What the physical cost means

The no-event record means that the sample did not absorb the photon. The photon can still pass through the sample, acquire a relative phase or change its mode. The two-query example makes the distinction quantitative. The following weights include all runs, including those lost on the first call.

| Sample-mode occupation | First call | Second call | Sum |
|---|---:|---:|---:|
| Immediately before the device | 2/5 | 2/5 | 4/5 |
| Immediately after the device | 1/5 | 2/5 | 3/5 |

For example, the second input has conditional sample weight one half and survives the earlier call with probability four fifths, giving two fifths. The difference between the two totals is the absorbed-photon probability one fifth.

For general N, [the resource account](../science/resources.md#absorption-and-passage-are-different-costs) gives sample-input passage $`1-p_N`$ and transmitted passage $`1-2p_N`$. Both approach one. The construction uses one photon and three available one-photon modes, with N device calls and a growing list of control angles. Its absorption advantage does not imply that traversal, elapsed time or the number of controls vanish. In this passive protocol an absorbed photon is never replaced, so its expected absorbed-photon count equals its probability of any absorption; those are different statistics for more general strategies.

The same resource page proves several consequential boundaries:

| Changed assumption | Consequence and canonical account |
|---|---|
| Imperfect preparation or controls | A conservative sufficient error budget shrinks with N to retain the ideal exponential scale. The [precision estimate](../science/resources.md#a-sufficient-precision-schedule) is a sufficient schedule, not a lower bound on the accuracy every implementation needs. A bound on a specified environmental record uses the flagged instrument. |
| Additional loss throughout the apparatus | With fixed survival probability per query below one, repeated calls eventually drive binary error toward one half. See [uniform apparatus loss](../science/resources.md#uniform-loss-in-the-whole-apparatus). |
| Loss in the nominally transparent sample modes | Fixed nonzero leakage creates a positive damage floor for fixed nontrivial discrimination accuracy, even with arbitrary common controls. See [the transparent-mode loss model](../science/resources.md#loss-in-the-nominally-transparent-sample-modes). |
| Conclusive reports must also be impossible for an empty device | This adds a third-process constraint absent from the binary promise. For the identity empty device, [the darkness bound](../science/resources.md#requiring-darkness-on-an-empty-device) prevents retaining constant conclusive A success with exponentially low absorption. |

These distinctions are developed in [M25–M29](MILESTONES.md#m25). The construction is an exact ideal model result; the resource analysis does not establish an experimental implementation or an optimal exponential base.

## Reading the proof dependencies

The course supplies the mathematical language. The project supplies the optical construction and its rate analysis. Keeping their roles separate gives a direct route from the worked example to the stronger statements.

| Claim or ingredient | Foundation and further work required | Authoritative project home |
|---|---|---|
| Channel and measurement probabilities | Lessons 9–11 supply density matrices, partial trace, Kraus representations and the binary discrimination formula. | [Model](../science/model.md) and the complete example above |
| Exponential construction | Normalization, orthonormal columns and inner-product preservation suffice to check the recurrence. Matching Gram matrices and completing an isometry to a unitary are standard linear algebra, credited in the research references. | [Exponential protocol](../science/exponential_protocol.md) |
| Finite exact-zero obstruction | A positive operator with zero expectation restricts the state's support; induction then covers all finite common strategies. The example alone establishes no universal obstruction. | [Zero absorption](../science/zero_absorption.md) |
| Corrected fidelity estimate and sufficient inverse-N bound | Lesson 12 introduces purifications and Uhlmann's theorem. The project additionally handles subnormalized inputs, retains every cross block, accumulates losses across queries and connects the no-event state back to the full output. The basic fidelity properties on source p. 365 are listed without proofs; the project gives the argument needed for its rate theorem. | [All-cross-block lemma](../science/rate_geometry.md#a-corrected-all-cross-block-fidelity-bound) and [rate theorem](../science/rate_geometry.md#a-sufficient-inverse-n-theorem) |
| Comparison with the written published rate statement | This requires the actual hypotheses and proof step of the primary research paper, beyond the educational anchor. The counterexample concerns the identified block estimate and dependent rate claim. | [Published multiblock step](../science/rate_geometry.md#the-published-multiblock-step) and [related work](../references/RELATED_WORK.md#hasenoehrl-wolf) |
| Robustness and changed operational tasks | Instrument-level perturbation estimates, loss models and the empty-device hybrid argument require their own stated assumptions. They are not consequences of the elementary two-call calculation alone. | [Resources and imperfections](../science/resources.md) |

The [verification guide](../verification/README.md) explains the finite checks and their limits. The scientific proofs remain the authority for all N and for arbitrary strategies. [M30](MILESTONES.md#m30) integrates the construction, converse conditions and physical boundaries into the project's overall conclusion.
