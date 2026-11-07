# Safe-action geometry and discrimination rates

The [exponential protocol](exponential_protocol.md) depends on how the two devices transform inner products between their respective safe inputs. Orthogonality of those inputs alone does not impose an inverse-N absorption law. This page isolates the missing cross term in a published bound and proves a sufficient condition under which an inverse-N law does hold.

The condition has a direct geometric meaning: the two safe actions must be restrictions of one common unitary. The quantitative bound allows arbitrary finite ancillary memory, measurements, classical records and adaptive common controls, and it uses the unconditional binary error.

## Notation and the environmental event

Consider two fixed memoryless channels on the same finite-dimensional input and output space $`\mathcal H`$:

```math
\begin{aligned}
\mathcal T_X(\rho)
 &=K_X\rho K_X^\dagger
   +\sum_\alpha L_{X,\alpha}\rho L_{X,\alpha}^\dagger,\\
K_X^\dagger K_X
 &+\sum_\alpha L_{X,\alpha}^\dagger L_{X,\alpha}=I,
\qquad X\in\{A,B\}.
\end{aligned}
```

The single Kraus operator $`K_X`$ describes no environmental event; the other Kraus operators describe an event. Each call uses a fresh environment, and the discriminator has no access to it. In the [physical model](model.md), the event is absorption, $`K_A=A_0`$ and $`K_B=B_0`$.

This event convention is fixed by the vacuum, as in [Hasenöhrl–Wolf, Definitions 3.2–3.3](../references/RELATED_WORK.md#hasenoehrl-wolf). If a Stinespring isometry maps the physical vacuum f to a product $`e_X\otimes u`$, projecting its environment onto $`e_X`$ gives $`K_X`$. Choose the vector phases so that

```math
K_A|f\rangle=K_B|f\rangle=|u\rangle.
```

For the explicit pair, $`u=f`$. This alignment removes the otherwise arbitrary relative phase of the no-event Kraus operators. All cross-inner-product conditions below refer to that alignment. If the two vacuum outputs differ as states, the sufficient condition below cannot hold.

Define the event effects, safe projectors and cross defect by

```math
\begin{aligned}
G_X&=I-K_X^\dagger K_X,\\
S_X&=\ker G_X,\qquad P_X=\Pi_{S_X},\qquad Q_X=I-P_X,\\
D&=I-K_A^\dagger K_B.
\end{aligned}
```

The restriction of $`K_X`$ to $`S_X`$ is an isometry. Here D denotes an operator; trace distance will be written explicitly as a trace norm.

For positive, possibly subnormalized operators, use the root fidelity

```math
F(R,S)=\|\sqrt R\sqrt S\|_1.
```

Thus F is not squared, and no failure-probability term is added to this definition.

## The published multiblock step

[Hasenöhrl–Wolf, Proposition 5.2](../references/RELATED_WORK.md#hasenoehrl-wolf) states a one-call root-fidelity bound with a sum of same-block population products. Its proof passes from Eq. (5.7) to Eq. (5.8) by dropping blocks between distinct orthogonal subspaces. The following example violates that bound.

For the fixed four-dimensional pair,

```math
\begin{aligned}
S_A&=\mathrm{span}\{f,r,a\},&
S_B&=\mathrm{span}\{f,r,b\},\\
V&=S_A\cap S_B=\mathrm{span}\{f,r\},&
V^\perp&=\mathrm{span}\{a,b\}.
\end{aligned}
```

Take $`0\lt q\lt1/2`$ and normalized pure inputs

```math
\begin{aligned}
|x_A\rangle&=\sqrt{1-q}|r\rangle+\sqrt q\,|a\rangle,\\
|x_B\rangle&=\sqrt{1-q}|r\rangle+\sqrt q\,|b\rangle,\\
R&=|x_A\rangle\langle x_A|,\qquad
S=|x_B\rangle\langle x_B|.
\end{aligned}
```

Each input is safe for its corresponding device. Their outputs are

```math
\begin{aligned}
K_A|x_A\rangle&=\sqrt{1-q}|r\rangle+\sqrt q\,|a\rangle,\\
K_B|x_B\rangle&=\sqrt{1-q}|r\rangle-\sqrt q\,|a\rangle.
\end{aligned}
```

Consequently,

```math
\begin{aligned}
F(R,S)&=1-q,\\
F(K_AR K_A^\dagger,K_BS K_B^\dagger)&=1-2q.
\end{aligned}
```

The fidelity decreases by q. However, for $`P_a=|a\rangle\langle a|`$ and $`P_b=|b\rangle\langle b|`$,

```math
\begin{aligned}
\mathrm{tr}(P_aR)&=q,&
\mathrm{tr}(P_aS)&=0,\\
\mathrm{tr}(P_bR)&=0,&
\mathrm{tr}(P_bS)&=q.
\end{aligned}
```

Every same-block product vanishes. No finite coefficient multiplying their sum can bound the positive decrease q.

These two inputs test a fidelity inequality that permits different states under the two hypotheses. They are not a hypothesis-dependent initial preparation. The [N-call construction](exponential_protocol.md) creates such different intermediate states using a common initial preparation and common controls.

The missing term is explicit:

```math
\begin{aligned}
D&=|a\rangle\langle a|+|b\rangle\langle b|
    +|a\rangle\langle b|,\\
P_aDP_b&=|a\rangle\langle b|\ne0.
\end{aligned}
```

The operator D vanishes on the common safe space $`\mathrm{span}\{f,r\}`$. Although $`P_aP_b=0`$, this does not imply $`P_aDP_b=0`$. Retaining the cross block gives the missing contribution q exactly.

### Consequence for the written rate theorem

[Theorem 5.9 of the same paper](../references/RELATED_WORK.md#hasenoehrl-wolf) assumes equal channel actions on the intersection of the maximal vacuum subspaces and orthogonal exclusive parts of those subspaces. It concludes that a fixed positive C bounds every strategy by

```math
p_{\max}\ge C\,\frac{(1-2e)^4}{N}.
```

The present pair satisfies those written hypotheses: its event effects are $`G_A=|b\rangle\langle b|`$ and $`G_B=|a\rangle\langle a|`$, its maximal vacuum subspaces are the displayed $`S_A,S_B`$, both channels act identically on V, and its exclusive safe directions a and b are orthogonal.

For the explicit protocol, $`p_{\max}=p_N=(2^N+1)^{-1}`$ and $`e_*=p_N/2`$. Therefore

```math
\frac{Np_N}{(1-2e_*)^4}
=\frac{N(2^N+1)^3}{2^{4N}}
\longrightarrow0.
```

No fixed $`C\gt0`$ can satisfy the claimed inequality for this pair. This disproves the stated general rate conclusion, rather than only a proposed extension to nonorthogonal exclusive safe spaces.

## A corrected all-cross-block fidelity bound

The following lemma keeps all blocks. It also allows ancillary systems and subnormalized inputs.

**Lemma.** Let $`W_A,W_B:\mathcal H\to\mathcal E\otimes\mathcal H_{\rm out}`$ be contractions, and define

```math
\mathcal E_X(R)=\mathrm{tr}_{\mathcal E}(W_XRW_X^\dagger).
```

Suppose that on a subspace V with projector P they agree and are isometric:

```math
W_AP=W_BP,\qquad PW_X^\dagger W_XP=P.
```

Put $`D_W=I-W_A^\dagger W_B`$. Let $`P_1,\ldots,P_m`$ be pairwise orthogonal projectors summing to $`I-P`$. For arbitrary positive R, S on $`\mathcal H\otimes\mathcal Z`$, let $`R_{\mathcal H},S_{\mathcal H}`$ be their reduced operators and write $`\widehat{\mathcal E}_X=\mathcal E_X\otimes{\rm id}_{\mathcal Z}`$. Then

```math
\begin{aligned}
&F(R,S)-F(\widehat{\mathcal E}_A(R),
          \widehat{\mathcal E}_B(S))\\
&\quad\le
\sum_{k,l=1}^m\|P_kD_WP_l\|\,
\sqrt{\mathrm{tr}(P_kR_{\mathcal H})\,
      \mathrm{tr}(P_lS_{\mathcal H})}.
\end{aligned}
```

The one-block version is

```math
\begin{aligned}
&F(R,S)-F(\widehat{\mathcal E}_A(R),
          \widehat{\mathcal E}_B(S))\\
&\quad\le\|D_W\|
\sqrt{\mathrm{tr}[(I-P)R_{\mathcal H}]\,
      \mathrm{tr}[(I-P)S_{\mathcal H}]}.
\end{aligned}
```

**Proof.** Positivity of $`I-W_X^\dagger W_X`$ and its zero quadratic form on V give $`(I-W_X^\dagger W_X)P=0`$. Together with $`W_AP=W_BP`$, this implies

```math
D_WP=PD_W=0.
```

Choose purifications $`\Psi,\Phi`$ of R, S satisfying $`\langle\Psi|\Phi\rangle=F(R,S)`$, real and nonnegative. Purifications of subnormalized operators have norms equal to the square roots of their traces. Applying $`W_A,W_B`$ gives purifications of the respective outputs, so, with identity operators on the other registers understood,

```math
\begin{aligned}
F(\widehat{\mathcal E}_A(R),\widehat{\mathcal E}_B(S))
 &\ge
 |\langle\Psi|W_A^\dagger W_B|\Phi\rangle|,\\
F(R,S)-F(\widehat{\mathcal E}_A(R),\widehat{\mathcal E}_B(S))
 &\le|\langle\Psi|D_W|\Phi\rangle|.
\end{aligned}
```

Insert $`\sum_kP_k`$ on both sides of $`D_W`$. Each term obeys

```math
\begin{aligned}
|\langle\Psi|P_kD_WP_l|\Phi\rangle|
&\le\|P_kD_WP_l\|\,\|(P_k\otimes I)\Psi\|\,
                         \|(P_l\otimes I)\Phi\|\\
&=\|P_kD_WP_l\|\,
\sqrt{\mathrm{tr}(P_kR_{\mathcal H})\,
      \mathrm{tr}(P_lS_{\mathcal H})}.
\end{aligned}
```

Summing proves the first inequality; inserting only $`I-P`$ proves the second. The argument is unchanged for any finite ancillary dimension. ∎

The lemma applies directly to the no-event contractions by taking $`W_X=K_X`$. It also applies to aligned projected Stinespring dilations $`W_X=(R_X\otimes I)V_X`$, for which

```math
W_A^\dagger W_B
=V_A^\dagger(R_AR_B\otimes I)V_B.
```

Here $`R_X`$ are environmental projectors, distinct from input operators R, S. A diagonal-only estimate follows if the off-diagonal blocks $`P_kD_WP_l`$ actually vanish for $`k\ne l`$. Orthogonality of the projectors alone is insufficient. The one-block inequality requires no such extra condition.

## A sufficient inverse-N theorem

For the no-event contractions, impose

```math
\boxed{P_ADP_B=0,\qquad D=I-K_A^\dagger K_B.}
```

Equivalently, the safe actions preserve every cross inner product:

```math
\langle K_Ax,K_By\rangle=\langle x,y\rangle
\quad
\text{for all }x\in S_A,\ y\in S_B.
```

For $`G_X\ne0`$, let $`\gamma_X`$ be its smallest strictly positive eigenvalue. Set $`\gamma_X=1`$ when $`G_X=0`$. In both cases,

```math
G_X\ge\gamma_XQ_X.
```

When the event effect is zero, $`Q_X=0`$ and the convention does not introduce a physical loss gap.

**Theorem.** Suppose $`P_ADP_B=0`$ after the vacuum phase alignment, and $`D\ne0`$. Consider any N-call causal strategy with a common initial state, arbitrary finite ancillary memory, and common CPTP controls, including measurements and feedback. Let e be its unconditional equal-prior binary error, with $`0\le e\le1/2`$, and let $`p_X`$ be the probability of at least one environmental event under hypothesis X. Then

```math
\boxed{
p_{\max}\ge
\frac{\bigl[1-2\sqrt{e(1-e)}\bigr]^2}
 {N\|D\|^2
  \bigl(\gamma_A^{-1/2}+\gamma_B^{-1/2}\bigr)^2}
},\qquad
p_{\max}=\max(p_A,p_B).
```

In particular, with $`\gamma_{\min}=\min(\gamma_A,\gamma_B)`$,

```math
\boxed{
p_{\max}\ge
\frac{\gamma_{\min}(1-2e)^4}{64N}
}.
```

The constants depend only on the fixed channel pair. The stronger asymmetric form is

```math
1-2\sqrt{e(1-e)}
\le\|D\|\sqrt N
\left(\sqrt{\frac{p_A}{\gamma_A}}+
      \sqrt{\frac{p_B}{\gamma_B}}\right).
```

A strategy with a hard cap of N calls is covered by padding stopped branches with common-vacuum calls. The statement does not replace N by an expected number of calls.

### Proof: one call

The cross-inner-product condition gives the operator decomposition

```math
D=Q_AD+P_ADQ_B.
```

For positive joint inputs R, S with trace at most one, use the purifications in the lemma. Denote their reduced system operators by $`R_{\mathcal H},S_{\mathcal H}`$. The same purification estimate, followed by the decomposition above, gives

```math
\begin{aligned}
&F(R,S)-F(K_AR K_A^\dagger,K_BS K_B^\dagger)\\
&\quad\le\|D\|
\left[
\sqrt{\mathrm{tr}(Q_AR_{\mathcal H})\,\mathrm{tr}\,S}
+
\sqrt{\mathrm{tr}\,R\,\mathrm{tr}(Q_BS_{\mathcal H})}
\right]\\
&\quad\le\|D\|
\left[
\sqrt{\frac{\mathrm{tr}(G_AR_{\mathcal H})}{\gamma_A}}
+
\sqrt{\frac{\mathrm{tr}(G_BS_{\mathcal H})}{\gamma_B}}
\right].
\end{aligned}
```

The no-event operators in this display act as the identity on every ancillary register. The last inequality uses the loss gaps and the trace upper bounds. If $`G_X=0`$, the corresponding projector and contribution vanish.

### Proof: accumulation and unconditional outputs

Let $`\tau_{X,j}`$ be the subnormalized joint input to call j obtained by applying the no-event operation at every earlier call. These are analysis objects; the experiment does not observe or select them. The first-event probability at that call is

```math
\ell_{X,j}=\mathrm{tr}[(G_X\otimes I)\tau_{X,j}].
```

Because all common controls are trace preserving,

```math
p_X=\sum_{j=1}^N\ell_{X,j}
   =1-\mathrm{tr}\,\tau_{X,\mathrm{fin}}.
```

Root fidelity cannot decrease under a common CPTP control, also for subnormalized states. The initial shared normalized state has fidelity one with itself. Telescope the one-call estimate through the strategy and apply Cauchy–Schwarz:

```math
\begin{aligned}
1-F(\tau_{A,\mathrm{fin}},\tau_{B,\mathrm{fin}})
&\le\|D\|\sum_{j=1}^N
\left(\sqrt{\ell_{A,j}/\gamma_A}
     +\sqrt{\ell_{B,j}/\gamma_B}\right)\\
&\le\|D\|\sqrt N
\left(\sqrt{p_A/\gamma_A}+\sqrt{p_B/\gamma_B}\right).
\end{aligned}
```

The full accessible outputs include every event history. Since the difference between the full channel and its no-event operation is CP, induction through the common controls yields the operator inequalities

```math
\rho_X\ge\tau_{X,\mathrm{fin}}.
```

Root fidelity is monotone in each positive argument in the Loewner order. For example, $`S'\ge S`$ implies

```math
\mathrm{tr}\,\sqrt{\sqrt R\,S'\sqrt R}
\ge
\mathrm{tr}\,\sqrt{\sqrt R\,S\sqrt R},
```

and symmetry gives monotonicity in R. Consequently,

```math
F(\rho_A,\rho_B)
\ge F(\tau_{A,\mathrm{fin}},\tau_{B,\mathrm{fin}}).
```

This is the step that connects the no-event calculation to the actual unconditional error.

For any final binary measurement with equal-prior error e,

```math
1-2e
\le\frac12\|\rho_A-\rho_B\|_1
\le\sqrt{1-F(\rho_A,\rho_B)^2}.
```

The last inequality is the [Fuchs–van de Graaf fidelity bound](https://arxiv.org/abs/quant-ph/9712042v2). It also follows by choosing purifications with overlap F, evaluating their pure-state trace distance, and tracing out the purifying register. Thus

```math
F(\rho_A,\rho_B)\le2\sqrt{e(1-e)}.
```

Combining the preceding inequalities proves the asymmetric bound. Replacing both probabilities by $`p_{\max}`$ and squaring proves the first displayed theorem bound.

Finally,

```math
\begin{aligned}
\|D\|&\le2,\\
\gamma_A^{-1/2}+\gamma_B^{-1/2}
&\le2/\sqrt{\gamma_{\min}},\\
1-2\sqrt{e(1-e)}
&=1-\sqrt{1-(1-2e)^2}\\
&\ge\tfrac12(1-2e)^2.
\end{aligned}
```

These inequalities give the constant 64 in the simpler bound. ∎

### Zero-defect and zero-event cases

If $`D=0`$, then $`K_A^\dagger K_B=I`$. For every vector x,

```math
\|x\|^2
=\langle K_Ax,K_Bx\rangle
\le\|K_Ax\|\,\|K_Bx\|
\le\|x\|^2.
```

Equality forces $`K_Ax=K_Bx`$ and $`\|K_Xx\|=\|x\|`$. On the same finite input and output space, both contractions are therefore the same unitary. All event Kraus operators vanish, the full channels coincide, and the equal-prior error is $`1/2`$. No division by a zero defect norm is used.

If only $`G_A=0`$, then $`p_A=0`$. Under the theorem's condition and $`D\ne0`$, its asymmetric form gives

```math
p_B\ge
\frac{\gamma_B\bigl[1-2\sqrt{e(1-e)}\bigr]^2}
     {N\|D\|^2}.
```

The corresponding statement holds with A and B exchanged. If both event effects vanish and the condition holds, the zero-defect case applies.

## Interpretation as a common unitary

**Proposition.** For contractions on the same finite-dimensional input and output space, $`P_ADP_B=0`$ is equivalent to the existence of a unitary U satisfying

```math
UP_A=K_AP_A,\qquad UP_B=K_BP_B.
```

**Proof.** A common unitary preserves all cross inner products. Conversely, preservation of those inner products implies that for $`x\in S_A\cap S_B`$,

```math
\|K_Ax-K_Bx\|^2
=2\|x\|^2-2\mathrm{Re}\,\langle K_Ax,K_Bx\rangle=0.
```

It therefore defines a well-defined linear map on the sum:

```math
W(x+y)=K_Ax+K_By,
\qquad x\in S_A,\ y\in S_B.
```

The individual safe restrictions are isometric, and the cross inner products are preserved, so $`\|W(x+y)\|=\|x+y\|`$. Thus W is an isometry on $`S_A+S_B`$. Extending orthonormal bases of its domain and range to bases of the same finite space gives the required unitary U. ∎

The inverse-N condition does not require orthogonality of the exclusive safe inputs. For example, $`K_A=P_A`$ and $`K_B=P_B`$ have the common extension $`U=I`$ for any two self-adjoint projection operators, even when their ranges are not mutually orthogonal.

## Repair by safe-output orthogonality

Suppose the two safe actions agree on $`V=S_A\cap S_B`$, and decompose

```math
S_A=V\oplus U_A,\qquad S_B=V\oplus U_B.
```

A sufficient repair of a rate statement based on orthogonal exclusive inputs is to require orthogonality of their outputs as well:

```math
U_A\perp U_B,\qquad K_AU_A\perp K_BU_B.
```

Indeed, inner products involving V are preserved because the maps agree there and are isometric on their safe spaces. The remaining cross products vanish on both sides. Thus $`P_ADP_B=0`$, and the inverse-N theorem follows. Equality of all cross inner products is the more general sufficient condition; separate vanishing is unnecessary.

For the exponential pair,

```math
U_A=\mathrm{span}\{a\},\qquad
U_B=\mathrm{span}\{b\},\qquad
K_Aa=a,\qquad K_Bb=-a.
```

Its exclusive safe inputs are orthogonal, but their output inner product is minus one. Equivalently,

```math
P_ADP_B=|a\rangle\langle b|\ne0.
```

That is precisely the cross action used to increase the overlap deficit without further absorption.

## Scope

The theorem is sufficient, not a complete rate classification. Failure of its cross-inner-product condition does not establish an exponential protocol for every pair. The constants are not claimed optimal, and the bound concerns a fixed number or hard cap of causal calls rather than an expected call count.

The counterexample concerns the multiblock estimate and the rate claim that uses it. It does not invalidate the one-block fidelity estimate, the general feasibility criterion for interaction-free discrimination, or the inverse-N constructions in [Hasenöhrl–Wolf](../references/RELATED_WORK.md#hasenoehrl-wolf). Scalar-transmission and other more restricted models require their own comparison; see [Related work](../references/RELATED_WORK.md).

The mathematical boundary established here is concrete: when the two safe actions extend to one common unitary, fixed discrimination advantage costs at least order $`1/N`$ in environmental-event probability. The explicit fixed pair violates that compatibility condition and achieves exponential decay while retaining the [finite-call zero-absorption obstruction](zero_absorption.md).
