# Related work and attribution

The contribution is the explicit exponential absorption law for the fixed [channel pair](../science/model.md), together with the role of the channels' safe output geometry. It is not a new definition of a quantum channel, a new framework for causal discrimination, or a new Gram-matrix completion theorem. The achieved base is not asserted to be optimal. The [construction](../science/exponential_protocol.md), [zero-absorption obstruction](../science/zero_absorption.md), [rate geometry](../science/rate_geometry.md), and [resource account](../science/resources.md) give the precise mathematical claims.

Bibliographic records, including the preprint versions used below, are in [references.bib](references.bib). The literature comparison was last checked on 6 November 2026. It supports the stated contribution boundaries; it is not a claim of exhaustive novelty clearance.

## Interaction-free measurement and the physical cost

The interferometric detection of a fragile object originates with [Elitzur and Vaidman (1993)](https://doi.org/10.1007/BF00736012). [Kwiat et al. (1995)](https://doi.org/10.1103/PhysRevLett.74.4763) introduced repeated weak interrogation using the quantum Zeno effect, and their [1999 experiment](https://doi.org/10.1103/PhysRevLett.83.4725) demonstrated increased efficiency and the importance of optical loss. These are the foundations of reducing absorption through coherent repeated interrogation.

Here, damage means an absorbed photon, or equivalently a recorded environmental event in the specified channel dilation. A transmitted photon may change phase or polarization without producing that record. This is weaker than requiring that the photon never traverse the sample, a distinction discussed in [Vaidman's review](https://arxiv.org/abs/quant-ph/0103081v1). The present protocol has exponentially small absorption but order-one integrated sample passage, calculated in [Resources and imperfections](../science/resources.md). No exponentially small traversal claim is made.

<a id="hasenoehrl-wolf"></a>

## Hasenöhrl–Wolf: framework, feasibility and the rate statement

[Hasenöhrl and Wolf, “Interaction-Free” Channel Discrimination](https://doi.org/10.1007/s00023-022-01175-z), *Annales Henri Poincaré* 23, 3331–3390 (2022), is the closest general framework. Its environment-based interaction definition, maximal vacuum subspaces, general feasibility criterion and Zeno constructions are credited background. The comparison here uses the **published version of record, 1 April 2022**, particularly Definition 5.1, Proposition 5.2 and Theorem 5.9. The [published PDF](https://link.springer.com/content/pdf/10.1007/s00023-022-01175-z.pdf) is the authoritative text for equation numbering.

Theorem 5.9 states an inverse-N interaction lower bound when the channels coincide on their common maximal vacuum subspace and their exclusive safe-input subspaces are orthogonal. The optical pair in this repository satisfies those written hypotheses. Its attained exponential law contradicts that rate statement.

The local proof issue occurs on **printed page 3377, from Eq. (5.7) to the first line of Eq. (5.8)**. Expanding the complement projection into orthogonal blocks produces both diagonal and off-diagonal terms. Orthogonality of the projections alone does not remove a matrix between them. The proof omits the off-diagonal terms without a supporting assumption in Definition 5.1. A one-query counterexample to Proposition 5.2, including a valid common dilation, is given in [the published multiblock step](../science/rate_geometry.md#the-published-multiblock-step).

This correction concerns the block inequality and the dependent rate statement. It does not establish that the paper's general feasibility criterion is false; the corresponding whole-complement argument does not make this particular block omission. The last paragraph of Section 2.1 and the open questions in Section 7 already identify faster-than-inverse-N behavior as a question requiring further understanding.

A bounded search by exact title, DOI, authors, “correction,” and “erratum” found no correction as of 6 November 2026. This is a search result, not certification that no correction exists or that the authors were unaware of the issue.

## Scalar transparency, polarimetry and recursive interferometers

| Source | Established setting and relation to this project |
|---|---|
| [Mitchison and Massar (2001)](https://doi.org/10.1103/PhysRevA.63.032105) | Discrimination between objects with scalar transmission and absorption amplitudes. Their limits for two partially transparent alternatives are not contradicted by a pair with different safe polarization subspaces and nontrivial safe output actions. |
| [Massar, Mitchison and Pironio (2001)](https://doi.org/10.1103/PhysRevA.64.062303) | Minimal-absorption measurements relate the discrimination of nearby transparencies and imaging sensitivity to absorbed photons. Absorption-budget reasoning is established prior work; the present result is a specific binary partial-isometry construction. |
| [Zhou and Yung (2017)](https://doi.org/10.1103/PhysRevA.96.062129) | A channel-discrimination formulation and input-state optimization for finite-cycle, Zeno-like detection of a semitransparent object's presence or absence. The fact that interaction-free measurement is channel discrimination is not a new claim here. |
| [Hance and Rarity (2022), v2](https://arxiv.org/abs/2207.13539v2) | Section II restricts the polarimetry analysis to diattenuators; Section III uses polarization heralding and conventional path-Zeno cycles. The present pair includes a transmitted-mode rotation and uses a different recurrence. |
| [Wang, Pitt and Milgie (2016)](https://doi.org/10.1088/0953-4075/49/4/045501) | Polarization toggles an ordinary absorber's presence in a chain of interferometers, and a recursive phase model includes loss and misalignment. That recursion is distinct from the repeated safe-output realignment used here. [Author-hosted full text](https://www-personal.umd.umich.edu/~jinwang/8.pdf). |

## Multipath localization and general no-absorption combs

[Chaturvedi et al., *Optimal Interaction Free Localization with Multipath Interferometers*](https://arxiv.org/abs/2607.26293v1), **v1, 28 July 2026**, is a close recent comparison. Section V, Eq. (21), and Appendix C allow general completely positive trace-nonincreasing no-absorption maps, including mode mixing and polarization changes. Their general process framework can accommodate the pair studied here; it must not be described as restricted to projectors.

Their exact examples use ideal projector absorbers. The two-use optimum is 27/128 without an empty reference rail and 25/72 with one, under their localization task. Appendix E also realizes coherent intermediate controls by matching Gram matrices. Neither the comb formalism nor this realization technique is claimed as new here. The additional result in this repository is the explicit repeated safe-subspace construction and its exact exponentially decreasing absorption law.

The operational tasks also differ. Their Eq. (23) requires every conclusive report to be impossible for a specified empty-device process. The present task is binary discrimination between the two promised devices and has no third, empty-device hypothesis. For the natural empty channel equal to the identity, adding their exact darkness condition changes the achievable rate.

Specifically, for device A, a hybrid argument between its no-event projector and the identity gives

```math
\|\alpha_{A,N}-\alpha_{\emptyset,N}\|
\leq\sum_{k=1}^{N}\sqrt{\ell_k}
\leq\sqrt{N p_A}.
```

Here the first vector is the unnormalized no-event output, the second is the normalized empty-device output, and the nonnegative losses sum to $p_A$. Any conclusive effect that annihilates the empty output therefore has **no-absorption** A-report probability at most $N p_A$. A-report success bounded away from zero then requires inverse-N absorption. Counting reports on absorption branches instead adds at most $p_A$, giving an upper bound of $(N+1)p_A$ unless the report effect also annihilates that sector. The [resource account](../science/resources.md#requiring-darkness-on-an-empty-device) supplies the task-boundary derivation. This is a statement about this pair and the identity empty device, not a universal exclusion from the general comb framework.

## Recent scalar-loss sensing comparisons

[Wildfeuer, *Counterfactual Quantum Sensing: What Interaction-Free Measurement Can and Cannot Buy*](https://arxiv.org/abs/2607.25699v1), **v1, 28 July 2026**, treats scalar transmission amplitude equal to the square root of T. Its fixed multipass theorem, Eqs. (20)–(25), couples a fixed object mode to fresh environment modes and bounds Fisher information about T per absorbed photon. Its Zeno-chain discrimination analysis also concerns scalar transparency alternatives. The present protocol uses precomputed controls too; absence of intermediate measurement feedback is not the distinguishing assumption. The distinction is the binary promise of different multidimensional partial isometries and their safe output geometry.

[Wildfeuer, *A universal loss-limited optimum for fixed multi-pass quantum sensing per absorbed photon*](https://arxiv.org/abs/2608.25534v1), **v1, 26 August 2026**, assumes in Section III.A a particular quadratic payoff, constant survival probability per pass and a geometric surviving-path cost. The present ideal construction, with absorption risk only on the first query, does not satisfy those payoff and survival assumptions. The paper is relevant to later apparatus-loss comparisons; it is not a general bound on this construction.

## Inherited mathematical tools

Equal Gram matrices permit one common isometry between two finite families of vectors; after completing bases, this extends to a unitary on the ambient space. This is standard pure-state transformation machinery, stated explicitly in [Chefles, Jozsa and Winter (2004), Section 2, Property 3](https://arxiv.org/html/quant-ph/0307227v1). The explicit control matrix here makes that ordinary completion concrete for the useful recursive pair.

Purification overlap and fidelity are established tools of [Uhlmann (1976)](https://doi.org/10.1016/0034-4877(76)90060-4) and [Jozsa (1994)](https://doi.org/10.1080/09500349414552171); fidelity–trace-distance comparisons are due to [Fuchs and van de Graaf (1999)](https://doi.org/10.1109/18.761271). [Watrous's *The Theory of Quantum Information* (2018), Chapters 2–3](https://jhwatrous.github.io/books-and-courses.html) gives a systematic account of channel representations, the Holevo–Helstrom discrimination formula, fidelity and channel distance. These standard results support the proofs and are not counted as new contributions.

The treatment of arbitrary causal strategies by quantum memory and combs is established by [Chiribella, D'Ariano and Perinotti (2009)](https://doi.org/10.1103/PhysRevA.80.022339). This repository's general-control bounds use that ordinary operational class; the explicit protocol needs only the stated single-photon controls.

## Source versions and inspection limits

The 2026 comparisons above are based on the actual primary PDFs, not solely their abstracts. For Chaturvedi et al., the inspected material includes Sections III and V, Appendix C, and the relevant exact two-use and Gram-matrix constructions in Appendix E. For the first Wildfeuer paper, the inspected material includes the scalar model, Eqs. (20)–(25), and the scope discussion on pages 7–8. For the second, it includes the Section III.A theorem and its stated hypotheses. Obtaining a full text does not mean that every theorem in it was independently verified.

Hance–Rarity v2 and Wang–Pitt–Milgie were inspected in full text. The compact descriptions of the earlier scalar-transparency and Zhou–Yung works above use their primary abstracts and stated models; they do not purport to revalidate those complete proofs. The Hasenöhrl–Wolf comparison uses the published definitions, statement and proof step identified above. No earlier realization of this exact exponential absorption recurrence was located in the targeted search, and that bounded observation should not be strengthened into an exhaustive priority claim.
