# Thirty milestones for understanding interaction-free discrimination rates

The scientific question is whether repeated calls to a fixed lossy device can reveal its identity while the probability of absorption falls exponentially. Understanding the answer requires following the accessible quantum state, the unobserved environmental event, and the restrictions on the controls together.

This map has exactly 30 project-defined milestones. Each records a central question, an understanding target, earlier dependencies, a conceptual connection and source pointers. The canonical statements and proofs remain in [science/](../science/model.md); the [educational bridge](BRIDGE.md#source-and-route) connects them to the selected source and supplies a [complete two-query example](BRIDGE.md#a-complete-two-query-experiment).

## Anchor and allocation

The single educational anchor is John Watrous, *Understanding Quantum Information and Computation*, **July 2025 Director’s Cut**: [author’s course page](https://jhwatrous.github.io/books-and-courses.html) and [author-hosted PDF](https://jhwatrous.github.io/UQIC.pdf). Every Watrous pointer below refers to that edition. Lesson and section numbers identify the material; PDF links open the relevant pages. Printed page numbers are six less than the PDF viewer’s page numbers.

The allocation is **13 milestones for background/preliminaries, M01–M13, and 17 for narrative/innovation, M14–M30**. The background connects individual modes and amplitudes to mixed states, open dynamics, event probabilities, safe spaces, measurement, fidelity and sequential control. M13 integrates those objects into the operational question.

The narrative receives more space because the result combines a concrete coherent mechanism with a correction to a rate argument and several distinct physical boundaries. M14–M18 assemble the experiment from its device action, seed and common controls. M19–M24 connect finite zero absorption, the published counterexample and the repaired converse. M25–M29 connect the ideal result to resources, precision, two different loss models and a changed reporting promise. M30 integrates the contribution and its scope.

Anchor sections supply the foundational tools. The optical model, event convention, protocol, corrected inequalities and resource bounds are supplied by the linked project sources. Primary research attribution and proof dependencies remain in [Related work](../references/RELATED_WORK.md); they are not additional educational anchors.

## Phase I — Background/preliminaries, M01–M13

### M01

**The physical states of one interrogation**

**Central question.** What distinguishes an absent photon, a photon in the reference path and a photon in either sample mode?

**Understanding target.** Interpret the orthonormal basis f, r, a, b as one physical vacuum and three one-photon modes. Explain why a four-dimensional state space does not mean four photons, and why replacing the reference state r by vacuum f changes the experiment.

**Dependencies and story role.** None. This establishes the physical objects before their mathematical descriptions and keeps the two meanings of an unoccupied sample distinct.

**Conceptual connection.** A basis labels alternatives of a system; the physical interpretation of those alternatives determines what absorption and passage mean.

**Source pointers.** Anchor: [Watrous Lesson 1, §1.2, Quantum information][w12]. Project: [model.md — Operational experiment](../science/model.md#operational-experiment); [exponential_protocol.md — Why the rate is possible](../science/exponential_protocol.md#why-the-rate-is-possible).

### M02

**Amplitudes, probabilities and relative phase**

**Central question.** How can two states have the same mode probabilities while carrying different information?

**Understanding target.** Distinguish complex amplitudes from their squared magnitudes, and relative phase from an irrelevant global phase. Explain why the plus and minus superpositions of r and a can be distinguished by interference even though measuring their mode populations gives the same distribution.

**Dependencies and story role.** M01. This adds coherence to the physical alternatives and prepares the phase-sensitive mechanism.

**Conceptual connection.** The device’s minus sign becomes useful only because a surviving reference amplitude remains coherent with the sample amplitude.

**Source pointers.** Anchor: [Watrous Lesson 1, §1.2, quantum state vectors and measurements][w12]. Project: [model.md — Operational experiment](../science/model.md#operational-experiment); [exponential_protocol.md — Theorem](../science/exponential_protocol.md#theorem).

### M03

**Inner products, projectors and common unitaries**

**Central question.** What must one unitary preserve when it acts on two possible input states?

**Understanding target.** Interpret inner products as the geometry of a pair of vectors, orthogonality as zero overlap, and projectors as selecting subspaces. Explain why a common unitary preserves the pair’s Gram matrix and why mapping two possible inputs cannot be specified independently without this constraint.

**Dependencies and story role.** M02. This supplies the local geometry needed both for the constructive control and for the rate obstruction.

**Conceptual connection.** The same preservation law that restricts a control later certifies that the required two-state transformation is physically possible.

**Source pointers.** Anchor: [Watrous Lesson 1, §1.2, Unitary operations][w12unitary]; [Lesson 3, §3.2, Inner products and projections][w32]. Project: [exponential_protocol.md — A common control sends both possibilities to their own safe spaces](../science/exponential_protocol.md#2-a-common-control-sends-both-possibilities-to-their-own-safe-spaces).

### M04

**Density matrices and mixtures**

**Central question.** How should an experiment with surviving-photon and absorbed-photon runs be represented?

**Understanding target.** Distinguish a pure state vector from a density matrix and a coherent superposition from a probability-weighted mixture. Explain how a normalized output can contain both an informative photon component and an uninformative vacuum component without placing them in a coherent superposition.

**Dependencies and story role.** M02. This expands the state description so that all experimental outcomes can be retained.

**Conceptual connection.** The full discrimination error is a property of the density matrices that include loss, even when the surviving vectors are orthogonal.

**Source pointers.** Anchor: [Watrous Lesson 9, §9.1, Density matrix basics][w91]; [§9.2, Convex combinations of density matrices][w92]. Project: [exponential_protocol.md — Theorem](../science/exponential_protocol.md#theorem); [model.md — Absorption, error and safe spaces](../science/model.md#absorption-error-and-safe-spaces).

### M05

**Accessible memory and unobserved environment**

**Central question.** What changes when part of a joint quantum system is inaccessible?

**Understanding target.** Read tensor products and reduced states, and distinguish tracing out an environment from conditioning on an observed result. Keep the controller’s ancillary memory separate from the device’s environment, including when both appear in a mathematical dilation.

**Dependencies and story role.** M04. This connects the local optical state to the larger systems needed for open dynamics and general strategies.

**Conceptual connection.** Environmental records can define a physical cost without becoming information available to the controller.

**Source pointers.** Anchor: [Watrous Lesson 2, §2.2, Quantum information][w22]; [Lesson 9, §9.4, Multiple systems and reduced states][w94]. Project: [model.md — Operational experiment](../science/model.md#operational-experiment); [rate_geometry.md — Notation and the environmental event](../science/rate_geometry.md#notation-and-the-environmental-event).

### M06

**Channels and Kraus descriptions**

**Central question.** How does a channel describe both transmission and absorption as one valid physical operation?

**Understanding target.** Explain the roles of the terms in a Kraus sum and the completeness relation that preserves total probability. Connect this description to a unitary or isometric evolution with an environment, and understand why validity must persist when an ancillary system is present.

**Dependencies and story role.** M03, M04, M05. This joins coherent evolution, mixtures and inaccessible systems into the channel framework.

**Conceptual connection.** A no-event contraction is one component of the device; the full trace-preserving channel includes the event components as well.

**Source pointers.** Anchor: [Watrous Lesson 10, §10.1, Quantum channel basics][w101]; [§10.2, Stinespring representations][w102stinespring] and [Kraus representations][w102kraus]. Project: [model.md — Operational experiment](../science/model.md#operational-experiment).

### M07

**Event weights without postselection**

**Central question.** How can a no-absorption history be analyzed without selecting successful runs in the experiment?

**Understanding target.** Distinguish the subnormalized operator $`K_X\rho K_X^\dagger`$, its trace, and the normalized state obtained by dividing by that trace. Explain how the trace retains the history’s probability, why first-event probabilities add to the probability of ever absorbing, and why this bookkeeping supplies no bath access.

**Dependencies and story role.** M06. This turns the channel decomposition into the probability accounting used throughout the project.

**Conceptual connection.** Conditional vectors simplify a derivation; their weights and the omitted event branches still determine the unconditional output.

**Source pointers.** Anchor: [Watrous Lesson 11, §11.2, Non-destructive measurements][w112non]; [§11.2, From a Kraus representation][w112kraus]. Project: [model.md — Absorption, error and safe spaces](../science/model.md#absorption-error-and-safe-spaces); [rate_geometry.md — Proof: accumulation and unconditional outputs](../science/rate_geometry.md#proof-accumulation-and-unconditional-outputs).

### M08

**Safe spaces as kernels of positive event effects**

**Central question.** Which inputs produce no environmental event with certainty?

**Understanding target.** Relate the positive event effect $`G_X=I-K_X^\dagger K_X`$ to its kernel $`S_X`$. Explain why the no-event map is isometric on that kernel, and why zero event expectation for a positive joint state restricts its support to the safe space tensored with the memory.

**Dependencies and story role.** M03, M06, M07. This converts probability statements into geometry that can constrain an entire protocol.

**Conceptual connection.** Positivity links a zero physical cost to a precise restriction on accessible input states.

**Source pointers.** Anchor: [Watrous Lesson 3, §3.2, projections][w32]; [Lesson 9, §9.1, positive semidefinite matrices][w91]; [Lesson 10, §10.2, Kraus representations][w102kraus]. Project: [model.md — Absorption, error and safe spaces](../science/model.md#absorption-error-and-safe-spaces); [zero_absorption.md — Proof](../science/zero_absorption.md#proof).

### M09

**Binary readout and unconditional error**

**Central question.** What does it mean to identify the device when every run must receive a binary decision?

**Understanding target.** Interpret measurement effects and equal prior probabilities, and connect the optimal binary error to half the trace norm of the output difference. Distinguish a binary decision on a vacuum run from declaring that run inconclusive, and explain why the latter convention does not remove its probability from the stated experiment.

**Dependencies and story role.** M03, M04. This connects mathematical state separation to the actual reporting task.

**Conceptual connection.** Perfect distinction of the surviving states is compatible with a positive unconditional error because the shared loss branch remains.

**Source pointers.** Anchor: [Watrous Lesson 11, §11.1, Mathematical formulations of measurements][w111]; [§11.3, Quantum state discrimination and tomography][w113], especially the two-state discrimination discussion. Project: [model.md — Absorption, error and safe spaces](../science/model.md#absorption-error-and-safe-spaces); [exponential_protocol.md — Theorem](../science/exponential_protocol.md#theorem).

### M10

**Purification as a proof representation**

**Central question.** Why can a proof use pure states and common isometries when the actual strategy contains mixtures, measurements and discards?

**Understanding target.** Explain how a mixed state can arise by tracing out part of a pure state, and how channel dilations retain discarded systems for analysis. Distinguish this enlargement of a proof from granting the experimenter extra control of the device’s environment.

**Dependencies and story role.** M05, M06. This prepares a representation that can cover all allowed strategies without restricting them to the explicit optical controls.

**Conceptual connection.** Purified descriptions make overlap arguments available while the operational state remains the reduced accessible state.

**Source pointers.** Anchor: [Watrous Lesson 12, §12.1, Purifications][w121]; [Lesson 10, §10.2, Stinespring representations][w102stinespring]. Project: [rate_geometry.md — A corrected all-cross-block fidelity bound](../science/rate_geometry.md#a-corrected-all-cross-block-fidelity-bound); [resources.md — A damage floor for arbitrary strategies](../science/resources.md#a-damage-floor-for-arbitrary-strategies).

### M11

**Root fidelity connects overlap to distinguishability**

**Central question.** How can overlap calculations constrain a measurement error for mixed outputs?

**Understanding target.** Use the root-fidelity convention, its pure-state overlap formula, its purification interpretation and its relation to trace distance. Explain why a common channel cannot decrease fidelity, while different channels under the two hypotheses can. Recognize where the project extends normalized-state facts to positive subnormalized branches.

**Dependencies and story role.** M03, M09, M10. This combines geometric and operational measures of information.

**Conceptual connection.** A local change in overlap becomes useful in a converse only after it is related to the full output states and their attainable binary error.

**Source pointers.** Anchor: [Watrous Lesson 12, §12.2, Fidelity][w122], particularly [Basic properties of fidelity, printed p. 365][w122properties] and [Uhlmann’s theorem, printed pp. 368–370][w122uhlmann]. Project: [rate_geometry.md — Notation and the environmental event](../science/rate_geometry.md#notation-and-the-environmental-event); [Proof: accumulation and unconditional outputs](../science/rate_geometry.md#proof-accumulation-and-unconditional-outputs).

### M12

**One common strategy for an unknown device**

**Central question.** What is allowed to depend on the known promise, and what cannot depend on the device’s hidden identity?

**Understanding target.** Describe a causal sequence of device calls interleaved with common controls on system and memory. Explain how measurements and classical feedback fit into common CPTP maps, why the controls may depend on N, and how fixed or hard-capped query counts differ from expected counts.

**Dependencies and story role.** M05, M06, M07, M09, M10. This assembles the individual operations into the general discrimination strategy.

**Conceptual connection.** Hypothesis-dependent intermediate states can arise under common controls; preparing or selecting a control using the unknown identity would change the task.

**Source pointers.** Anchor: [Watrous Lesson 3, §3.1, Circuits][w31]; [Lesson 10, §10.1, Quantum channel basics][w101]; [Lesson 11, §11.1, measurements and classical outputs][w111]. Project: [model.md — Operational experiment](../science/model.md#operational-experiment); [rate_geometry.md — A sufficient inverse-N theorem](../science/rate_geometry.md#a-sufficient-inverse-n-theorem).

### M13

**The operational question as a whole**

**Central question.** Which distinct questions are posed by exact zero absorption, asymptotically small absorption, and a rate in the number of calls?

**Understanding target.** Give one consistent account of the hypotheses, accessible registers, common controls, environmental event, unconditional error and query count. Distinguish a construction from a statement about every strategy, and distinguish absorption probability from physical passage and apparatus use.

**Dependencies and story role.** M08, M11, M12. This integrates the background into the framework that the narrative will answer, including the quantifiers that separate its claims.

**Conceptual connection.** The same channel formalism supports a low-damage protocol, an exact-zero obstruction and a conditional rate converse because these address different questions.

**Source pointers.** Anchor: [Watrous Lesson 10, §10.2, Channel representations][w102]; [Lesson 11, §11.3, state discrimination][w113]; [Lesson 12, §12.2, Fidelity][w122]. Project: [model.md — Operational experiment](../science/model.md#operational-experiment) and [Exact claims and their homes](../science/model.md#exact-claims-and-their-homes); [resources.md — Absorption and passage are different costs](../science/resources.md#absorption-and-passage-are-different-costs).

## Phase II — Narrative/innovation, M14–M30

### M14

**The two fixed devices and their safe outputs**

**Central question.** Which feature of the specific channel pair creates an opportunity beyond repeated weak absorption tests?

**Understanding target.** Follow A and B on each basis direction: their shared action on f and r, their different absorbed modes, and B’s transmitted output minus a. Identify their common and exclusive safe inputs, and explain why orthogonal exclusive inputs can have nonorthogonal outputs under different devices.

**Dependencies and story role.** M13. The narrative starts with the local device action whose consequences will be assembled into a protocol.

**Conceptual connection.** Each safe restriction is isometric by itself, but this does not force the cross inner products between the two restrictions to be preserved.

**Source pointers.** Anchor: [Watrous Lesson 3, §3.2, Inner products and projections][w32]; [Lesson 10, §10.2, Kraus representations][w102kraus]. Project: [model.md — Operational experiment](../science/model.md#operational-experiment) and [Absorption, error and safe spaces](../science/model.md#absorption-error-and-safe-spaces).

### M15

**Paying for a small initial separation**

**Central question.** How does one common input create a useful difference while paying only a small first-call absorption probability?

**Understanding target.** Explain the role of the N-dependent reference-dominated seed. Track its event weight and its two normalized surviving states separately, and relate the initial excitation $`q_1=2^{-N}`$ to the later number of doubling steps.

**Dependencies and story role.** M07, M14. This supplies the initial difference that later safe calls will amplify.

**Conceptual connection.** A strictly positive initial event probability permits the two hypotheses to leave different accessible states, which the exact-zero case cannot do.

**Source pointers.** Anchor: [Watrous Lesson 1, §1.2, quantum state vectors][w12]; [Lesson 11, §11.2, Kraus outcome probabilities][w112kraus]. Project: [exponential_protocol.md — Seed a small separation](../science/exponential_protocol.md#1-seed-a-small-separation).

### M16

**A physically valid control for both possibilities**

**Central question.** How can the same control send two unknown possible states into two different safe input spaces?

**Understanding target.** Explain the Gram-matrix compatibility of the input and target pairs, and how the displayed orthonormal columns define one unitary $`U_q`$. Keep its dependence on the predetermined q separate from dependence on the unknown hypothesis.

**Dependencies and story role.** M03, M14, M15. This establishes the control step that makes the mechanism implementable.

**Conceptual connection.** Preserving the overlap during the common control allows the subsequent differing channel actions to change it.

**Source pointers.** Anchor: [Watrous Lesson 1, §1.2, Unitary operations][w12unitary]; [Lesson 3, §3.2, orthonormal sets and basis extension][w32]. Project: [exponential_protocol.md — A common control sends both possibilities to their own safe spaces](../science/exponential_protocol.md#2-a-common-control-sends-both-possibilities-to-their-own-safe-spaces).

### M17

**One safe call doubles the overlap deficit**

**Central question.** What grows in the decisive control-and-query step, and why does its growth add no absorption?

**Understanding target.** Follow the two transformed inputs into their respective safe spaces and then through their respective devices. Explain the update $`q\mapsto2q`$, identify q as a squared excitation weight, and distinguish doubling the overlap deficit from doubling trace distance.

**Dependencies and story role.** M08, M14, M16. This isolates the new local amplification mechanism before it is iterated.

**Conceptual connection.** The channels preserve each safe input’s norm while changing the cross overlap between the two hypotheses.

**Source pointers.** Anchor: [Watrous Lesson 3, §3.2, inner products][w32]; [Lesson 12, §12.2, fidelity for pure states][w122]. Project: [exponential_protocol.md — A common control sends both possibilities to their own safe spaces](../science/exponential_protocol.md#2-a-common-control-sends-both-possibilities-to-their-own-safe-spaces) and [Why the rate is possible](../science/exponential_protocol.md#why-the-rate-is-possible).

### M18

**The complete unconditional protocol**

**Central question.** How do the seed and safe updates combine into the stated N-call absorption and error laws?

**Understanding target.** Connect the schedule $`q_j=2^{j-N-1}`$ to the final orthogonal surviving states. Include the absorbing vacuum branch to obtain $`p_N=(2^N+1)^{-1}`$ and $`e_*=p_N/2`$. Relate the complete two-query example to the general proof without turning a conditional calculation into experimental postselection.

**Dependencies and story role.** M07, M09, M15, M17. This is the first narrative synthesis: preparation, control, query, event accounting and readout form one finite experiment.

**Conceptual connection.** The achieved exponential rate follows from a linear number of deficit doublings after one paid seed, with every branch retained.

**Source pointers.** Anchor: [Watrous Lesson 9, §9.2, mixtures][w92]; [Lesson 11, §11.3, two-state discrimination][w113]. Project: [exponential_protocol.md — Iterate and include all branches](../science/exponential_protocol.md#3-iterate-and-include-all-branches) and [Theorem](../science/exponential_protocol.md#theorem); [BRIDGE.md — A complete two-query experiment](BRIDGE.md#a-complete-two-query-experiment).

### M19

**Why exactly zero absorption cannot seed information**

**Central question.** Why does the exponential sequence coexist with an obstruction at exactly zero absorption for every finite N?

**Understanding target.** Explain the induction from equal inputs, zero event expectations, support in the common safe space and equal outputs. Identify why the argument still permits arbitrary memory and common adaptive controls. Distinguish an N-dependent sequence with positive absorption from one finite zero-absorption experiment.

**Dependencies and story role.** M08, M12, M18. This places the positive construction beside its exact limiting obstruction.

**Conceptual connection.** A nonnegative cost that is exactly zero constrains every call; a small positive cost can first create different states and change what later calls can do.

**Source pointers.** Anchor: [Watrous Lesson 9, §9.1, positivity][w91]; [Lesson 10, §10.1, channels with ancillary systems][w101]. Project: [zero_absorption.md — General finite-query obstruction](../science/zero_absorption.md#general-finite-query-obstruction) and [Application to the optical pair](../science/zero_absorption.md#application-to-the-optical-pair).

### M20

**The missing cross block in one query**

**Central question.** Why can a fidelity decrease be missed by counting only populations in matching orthogonal blocks?

**Understanding target.** Follow the safe-input example with $`0\lt q\lt1/2`$ whose root fidelity changes from $`1-q`$ to $`1-2q`$, even though all same-block population products vanish. For the cross defect $`D=I-K_A^\dagger K_B`$, locate the nonzero block between a and b and explain why $`P_aP_b=0`$ does not imply $`P_aDP_b=0`$.

**Dependencies and story role.** M11, M14, M17. This turns the physical mechanism into a precise local diagnostic of the published inequality.

**Conceptual connection.** Coherence between different safe-input blocks is the information source that a diagonal population estimate omits.

**Source pointers.** Anchor: [Watrous Lesson 3, §3.2, projections][w32]; [Lesson 12, §12.2, pure-state fidelity][w122]. Project: [rate_geometry.md — The published multiblock step](../science/rate_geometry.md#the-published-multiblock-step); primary comparison: [Related work — Hasenöhrl–Wolf](../references/RELATED_WORK.md#hasenoehrl-wolf).

### M21

**From the local defect to the stated rate failure**

**Central question.** What exactly does the exponential protocol disprove in the published rate theorem?

**Understanding target.** Match the fixed pair to the written common-safe-action and exclusive-input-orthogonality hypotheses, then understand why no N-independent positive constant can bound its absorption by the stated inverse-N expression. Separate this failure from the feasibility characterization and constructions that remain outside the counterexample.

**Dependencies and story role.** M18, M19, M20. This connects the one-query diagnostic to a global claim about every finite strategy.

**Conceptual connection.** A valid rate comparison requires the same event definition, unconditional error, device pair and quantifiers, not merely similar asymptotic terminology.

**Source pointers.** Anchor tools: [Watrous Lesson 11, §11.3, discrimination error][w113]; [Lesson 12, §12.2, Fidelity][w122]. Project: [rate_geometry.md — Consequence for the written rate theorem](../science/rate_geometry.md#consequence-for-the-written-rate-theorem) and [Scope](../science/rate_geometry.md#scope); primary theorem attribution: [Related work — Hasenöhrl–Wolf](../references/RELATED_WORK.md#hasenoehrl-wolf).

### M22

**Keeping all cross blocks repairs the one-query estimate**

**Central question.** Which fidelity inequality survives when the omitted coherences are retained?

**Understanding target.** Explain how purifications turn fidelity loss into a matrix element of a cross defect, why the aligned common isometric part cancels, and why inserting a block decomposition gives a sum over both block indices. Understand the role of operator norms and the applicability to ancillary and subnormalized inputs, including the valid one-block specialization.

**Dependencies and story role.** M03, M05, M10, M11, M20. This replaces the local failed estimate with the ingredient needed for reliable converses.

**Conceptual connection.** The repaired bound accounts for the same cross action that powers the constructive protocol.

**Source pointers.** Anchor: [Watrous Lesson 12, §12.1, Purifications][w121] and [§12.2, Uhlmann’s theorem][w122uhlmann]; [Lesson 3, §3.2, projections][w32]. Project: [rate_geometry.md — A corrected all-cross-block fidelity bound](../science/rate_geometry.md#a-corrected-all-cross-block-fidelity-bound).

### M23

**Compatible safe actions and one common unitary**

**Central question.** When do the two safe restrictions preserve the geometry needed for an inverse-N bound?

**Understanding target.** Interpret $`P_ADP_B=0`$ as preservation of every safe cross inner product, after aligning no-event Kraus phases through the common vacuum output. Explain its equivalence to extending both safe restrictions to one unitary on the same finite input/output space, and why safe-output orthogonality repairs the orthogonal-exclusive-input hypothesis.

**Dependencies and story role.** M03, M08, M14, M22. This identifies the geometric assumption that will control the accumulated fidelity change.

**Conceptual connection.** Compatibility is tested across the two devices’ safe maps, not merely within either map. It is a sufficient rate condition; its necessity is unestablished.

**Source pointers.** Anchor: [Watrous Lesson 3, §3.2, orthonormal bases and projections][w32]; [Lesson 10, §10.2, Stinespring representations][w102stinespring]. Project: [rate_geometry.md — Interpretation as a common unitary](../science/rate_geometry.md#interpretation-as-a-common-unitary); [Repair by safe-output orthogonality](../science/rate_geometry.md#repair-by-safe-output-orthogonality); [Notation and the environmental event](../science/rate_geometry.md#notation-and-the-environmental-event).

### M24

**Accumulation yields a sufficient inverse-N converse**

**Central question.** How does a one-call fidelity estimate constrain the event probability of every N-call strategy?

**Understanding target.** Follow the roles of loss gaps, first-event probabilities, telescoping through common controls and Cauchy–Schwarz. Explain the passage from no-event states to full accessible outputs and then to unconditional error. Interpret the inverse-N lower bound at fixed discrimination advantage, including its fixed-pair constants and the cases of a zero defect or a vanishing event effect.

**Dependencies and story role.** M07, M11, M12, M22, M23. This assembles the corrected local estimate into the general conditional rate theorem.

**Conceptual connection.** An information advantage forces cumulative overlap loss, and the compatibility condition ties that loss to an environmental-event budget.

**Source pointers.** Anchor: [Watrous Lesson 12, §12.2, monotonicity and fidelity/trace-distance bounds][w122properties]. Project: [rate_geometry.md — A sufficient inverse-N theorem](../science/rate_geometry.md#a-sufficient-inverse-n-theorem), [Proof: accumulation and unconditional outputs](../science/rate_geometry.md#proof-accumulation-and-unconditional-outputs) and [Zero-defect and zero-event cases](../science/rate_geometry.md#zero-defect-and-zero-event-cases). The primary fidelity-bound citation is retained in that proof.

### M25

**The physical resources behind low absorption**

**Central question.** Which physical resources decrease, stay fixed or grow as N increases?

**Understanding target.** Connect each common control to two passive mode rotations, and count one photon, three one-photon modes, N calls and N−1 inter-query controls. Explain why absorption falls while total sample-input passage approaches one and whole-apparatus query occupancy grows with N.

**Dependencies and story role.** M01, M18. This carries the ideal protocol from a channel formula to its physical resource account.

**Conceptual connection.** Low absorbed energy and a small environmental-event probability do not imply vanishing photon passage, elapsed interrogation or control effort.

**Source pointers.** Anchor: [Watrous Lesson 1, §1.2, Unitary operations][w12unitary]; [Lesson 3, §3.1, circuit composition][w31]. Project: [resources.md — Passive implementation](../science/resources.md#passive-implementation) and [Absorption and passage are different costs](../science/resources.md#absorption-and-passage-are-different-costs).

### M26

**What a sufficient precision budget guarantees**

**Central question.** Which operation errors must be controlled to preserve the exponentially small absorption and readout error?

**Understanding target.** Explain additive error accumulation using trace distance and ancillary-system channel distance, and why the general environmental-event bound uses flagged instruments. Recognize the separate passive absorbing case where final vacuum population records total photon loss. Interpret the order-$`2^{-N}/N`$ per-operation schedule as a conservative sufficient bound, not a necessary tolerance or an achieved calibration. Keep analysis flags inaccessible to the controller.

**Dependencies and story role.** M06, M07, M11, M12, M25. This makes the accuracy assumption behind the ideal performance explicit.

**Conceptual connection.** A small accessible-channel error and a small error in a specified environmental record are different statements. The proof must control the record itself or identify an output statistic that records the same event in the stated model.

**Source pointers.** Anchor tools: [Watrous Lesson 10, §10.1, channels acting on part of a larger system][w101]; [Lesson 11, §11.2, Kraus outcomes][w112kraus]. Project: [resources.md — A sufficient precision schedule](../science/resources.md#a-sufficient-precision-schedule), which supplies the half-diamond-distance and flagged-instrument extension.

### M27

**Uniform apparatus loss changes useful survival**

**Central question.** Why can exponentially small sample absorption coexist with a readout that becomes uninformative in a lossy loop?

**Understanding target.** Distinguish sample absorption from hypothesis-independent attenuation of every one-photon mode. Explain the survival factor $`\lambda^N(1-p_N)`$, why fixed $`\lambda\lt1`$ drives the unconditional error to one half, and why the best finite number of calls within this protocol balances the two effects.

**Dependencies and story role.** M04, M18, M25. This introduces a noise model that leaves the ideal normalized surviving evolution intact but changes its probability.

**Conceptual connection.** The final detector may see a common vacuum outcome even when the physical loss occurred in different places with different resource meanings.

**Source pointers.** Anchor: [Watrous Lesson 9, §9.2, mixtures][w92]; [Lesson 10, §10.2, Kraus representations][w102kraus]. Project: [resources.md — Uniform loss in the whole apparatus](../science/resources.md#uniform-loss-in-the-whole-apparatus).

### M28

**Leakage of the transparent modes changes feasibility**

**Central question.** What happens when the sample modes used as perfectly safe directions acquire a fixed nonzero loss?

**Understanding target.** Explain how imperfect transmission removes the exclusive safe directions and leaves only the common safe space. Connect the resulting arbitrary-strategy damage floor at fixed nontrivial accuracy to the intact one-block/no-go reasoning. Distinguish that converse from the displayed calibrated schedule, its transmission-dependent behavior and its unclaimed optimality.

**Dependencies and story role.** M08, M22, M24, M27. This contrasts loss that merely reduces survival with loss that changes the safe-space geometry supporting the mechanism.

**Conceptual connection.** Exact transparent directions are a structural assumption: perturbing them can replace an asymptotically vanishing cost by a positive floor.

**Source pointers.** Anchor: [Watrous Lesson 9, §9.1, positivity][w91]; [Lesson 12, §12.2, Fidelity][w122]. Project: [resources.md — Loss in the nominally transparent sample modes](../science/resources.md#loss-in-the-nominally-transparent-sample-modes), [A damage floor for arbitrary strategies](../science/resources.md#a-damage-floor-for-arbitrary-strategies) and [A calibrated schedule illustrates the floor](../science/resources.md#a-calibrated-schedule-illustrates-the-floor); inherited no-go attribution: [Related work — Hasenöhrl–Wolf](../references/RELATED_WORK.md#hasenoehrl-wolf).

### M29

**An empty-device reporting promise is a different task**

**Central question.** What changes if a conclusive device report must have exactly zero probability for an empty apparatus?

**Understanding target.** Distinguish the known binary promise from the additional empty-device-darkness condition. Explain how comparison with the identity device yields an inverse-N absorption requirement for a nonvanishing conclusive no-absorption A-report probability, and why this statistic is not the same as every possible average-success criterion.

**Dependencies and story role.** M09, M12, M18, M24. This connects the protocol to a neighboring operational task and identifies the promise responsible for the difference.

**Conceptual connection.** Changing which reports are permitted can change the resource bound even when the same physical channel pair is admitted by a general framework.

**Source pointers.** Anchor: [Watrous Lesson 11, §11.1, positive measurement effects][w111] and [§11.3, state discrimination][w113]; [Lesson 10, §10.2, dilations][w102stinespring]. Project: [resources.md — Requiring darkness on an empty device](../science/resources.md#requiring-darkness-on-an-empty-device); primary task comparison: [Related work — Multipath localization and general no-absorption combs](../references/RELATED_WORK.md#multipath-localization-and-general-no-absorption-combs).

### M30

**The complete mechanism, corrected boundary and physical scope**

**Central question.** What unified account explains both the exponential construction and the limits that remain?

**Understanding target.** Connect the paid initial separation, common safe control, changing cross overlap and full binary readout into the achieved exponential law. Reconcile that law with the finite exact-zero obstruction and the sufficient common-unitary inverse-N theorem. Explain which resource, calibration, loss and reporting assumptions support each conclusion, while leaving optimal rates and a complete geometry classification unestablished.

**Dependencies and story role.** M19, M21, M24, M25, M26, M27, M28, M29. This integrates the narrative into one scientific contribution with precise attribution and boundaries.

**Conceptual connection.** Feasibility, convergence rate and physical usefulness depend jointly on safe input/output actions, the measured cost and the operational promise; none alone determines the whole answer.

**Source pointers.** Anchor synthesis: [Watrous Lesson 10, §10.2, Channel representations][w102]; [Lesson 11, §11.3, state discrimination][w113]; [Lesson 12, §12.2, Fidelity][w122]. Project: [model.md — Exact claims and their homes](../science/model.md#exact-claims-and-their-homes); [exponential_protocol.md — Why the rate is possible](../science/exponential_protocol.md#why-the-rate-is-possible); [rate_geometry.md — Scope](../science/rate_geometry.md#scope); [resources.md — What the result does and does not settle](../science/resources.md#what-the-result-does-and-does-not-settle); [Related work](../references/RELATED_WORK.md).

[w12]: https://jhwatrous.github.io/UQIC.pdf#page=18
[w12unitary]: https://jhwatrous.github.io/UQIC.pdf#page=24
[w22]: https://jhwatrous.github.io/UQIC.pdf#page=49
[w31]: https://jhwatrous.github.io/UQIC.pdf#page=69
[w32]: https://jhwatrous.github.io/UQIC.pdf#page=79
[w91]: https://jhwatrous.github.io/UQIC.pdf#page=262
[w92]: https://jhwatrous.github.io/UQIC.pdf#page=268
[w94]: https://jhwatrous.github.io/UQIC.pdf#page=281
[w101]: https://jhwatrous.github.io/UQIC.pdf#page=294
[w102]: https://jhwatrous.github.io/UQIC.pdf#page=302
[w102stinespring]: https://jhwatrous.github.io/UQIC.pdf#page=303
[w102kraus]: https://jhwatrous.github.io/UQIC.pdf#page=310
[w111]: https://jhwatrous.github.io/UQIC.pdf#page=327
[w112non]: https://jhwatrous.github.io/UQIC.pdf#page=343
[w112kraus]: https://jhwatrous.github.io/UQIC.pdf#page=345
[w113]: https://jhwatrous.github.io/UQIC.pdf#page=347
[w121]: https://jhwatrous.github.io/UQIC.pdf#page=355
[w122]: https://jhwatrous.github.io/UQIC.pdf#page=368
[w122properties]: https://jhwatrous.github.io/UQIC.pdf#page=371
[w122uhlmann]: https://jhwatrous.github.io/UQIC.pdf#page=374
