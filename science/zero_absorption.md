# Why exactly zero absorption gives no information

The exponential construction approaches zero damage. It does not reach an informative zero-damage protocol at a finite query count. This statement is stronger than a restriction on the explicit controls: it permits arbitrary common causal controls and ancillary memory.

## General finite-query obstruction

Let each channel have a specified no-event operation $`\rho\mapsto K_X\rho K_X^\dagger`$ and other event Kraus operators. Define its safe space by $`S_X=\ker(I-K_X^\dagger K_X)`$. Suppose that the two full channels agree on every operator supported in $`S=S_A\cap S_B`$.

**Proposition.** For any finite number of queries, any initial state independent of the unknown hypothesis, any ancillary memory and any sequence of common causal controls, zero probability of an event under both hypotheses implies identical final accessible states. For equal priors, the minimum binary error is one half.

### Proof

At the first call the two input states are identical. Let that joint state on system and memory be $`\omega`$. A zero event probability under X means

```math
\mathrm{tr}\,\big[((I-K_X^\dagger K_X)\otimes I)\omega\big]=0.
```

Both factors inside this positive expectation are positive semidefinite. Therefore the support of $`\omega`$ lies in $`S_X\otimes\mathcal H_M`$. Requiring this for both hypotheses places it in $`S\otimes\mathcal H_M`$. Agreement of the channels on all operators supported in S implies agreement after tensoring with the identity on the memory, so the two post-call states are equal.

Any common control preserves that equality. Before the second call the joint states are again equal; zero total event probability forces zero event probability at this call too, since the event probabilities are nonnegative and no earlier event has occurred. The same support argument applies. Induction through all N calls proves identical outputs. The final measurement, including any classical processing, cannot distinguish identical states.

Purifying a mixed preparation or representing intermediate measurements by a larger memory does not change the argument. The number of queries is finite, but the allowed finite memory dimension is unrestricted. ∎

## Application to the optical pair

For the [two devices](model.md), the common safe space is $`\mathrm{span}\{f,r\}`$, and both channels act as the identity on it. The proposition therefore applies. It even allows controls more general than the passive, number-preserving ones used in the construction.

There is no contradiction between this statement and

```math
p_N=\frac{1}{2^N+1}\longrightarrow0,\qquad
e_N=\frac{1}{2(2^N+1)}\longrightarrow0.
```

Each member of this sequence has a strictly positive first-query absorption probability, and its preparation and controls depend on N. The limiting sequence is not a single finite experiment with zero absorption.

## Relation to general feasibility theory

Hasenöhrl and Wolf's [channel framework](../references/RELATED_WORK.md#hasenoehrl-wolf) distinguishes asymptotically interaction-free discrimination from finite exact zero interaction. Their general feasibility characterization and Zeno constructions are credited background. The counterexample in this project concerns a particular claimed rate lower bound; it does not contradict the feasibility of making both error and interaction arbitrarily small for this pair.

The proposition above is a direct finite-query support argument. It does not assert that every pair failing its premise has a zero-cost finite discriminator. That converse is neither needed nor claimed.
