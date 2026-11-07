# Resources and imperfections

The [exponential law](exponential_protocol.md) concerns absorption by the unknown sample. This page counts the other resources and makes the idealization explicit. It also supplies two noise models whose different effects should not be conflated.

## Passive implementation

On the one-photon subspace, let $`R_{rb}(\theta)`$ rotate r toward b and let Q fix r while sending a to $`(a-b)/\sqrt2`$ and b to $`(a+b)/\sqrt2`$. Both operations fix the physical vacuum f. The inter-query control factors as

```math
U_q=Q R_{rb}(\theta_q),\qquad
\sin\theta_q=\sqrt{\frac{q}{1-q}},\qquad
\cos\theta_q=\sqrt{\frac{1-2q}{1-q}}.
```

Thus each control is exactly two passive two-mode rotations, one fixed and one adjusted with the query number. The seed can likewise be prepared with a reference-to-sample rotation followed by the fixed Q. Mixing r and a on a balanced interferometer resolves the final plus/minus states. These are ideal mode transformations; this statement does not supply a fabrication tolerance or experimental demonstration.

The apparatus uses one photon, three available modes, a classical list of predetermined angles, N calls and $`N-1`$ inter-query controls. The vacuum adds a fourth basis state but no occupied mode. No quantum workspace grows with N in this construction.

## Absorption and passage are different costs

Let $`p=p_N`$, $`s=1-p`$ and $`\Pi=|a\rangle\langle a|+|b\rangle\langle b|`$. Define sample-input passage as the sum of the expectation of $`\Pi`$ immediately before all device calls, counting all runs. Define transmitted passage by the same sum immediately after the calls. The ideal protocol has

```math
\begin{aligned}
\mathbb E[\text{absorbed photons}]&=p,\\
\text{sample-input passage}&=1-p,\\
\text{transmitted passage}&=1-2p,\\
\text{whole-apparatus query occupancy}&=N-(N-1)p.
\end{aligned}
```

To verify the first two passage identities, the first input has sample weight $`2p`$. The later inputs have weights $`s q_j`$ for $`j=2,\ldots,N`$, while every output has transmitted sample weight $`s q_j`$ for $`j=1,\ldots,N`$. Summing the geometric sequence $`q_j=2^{j-N-1}`$ gives the stated totals. The first apparatus input contains a photon with probability one and each subsequent input with probability s.

The sample-input total tends to one as N grows. Absorption tends to zero exponentially. Time, apparatus occupancy and the number of controls grow with N. The result establishes low absorbed energy and low environmental disturbance in the stated model; it does not establish vanishing traversal or the absence of all photon–sample coupling.

## A sufficient precision schedule

Use half trace distance for state errors and half diamond distance for channel errors. Suppose the prepared state differs from the intended state by at most $`\delta_0`$, the common controls by at most $`\delta_j`$, and the device uses by at most $`\kappa_j`$. For the last quantity, compare the **flagged instruments** that retain an absorption/no-absorption record, not only the channels after that record is discarded. This record is introduced for the error analysis and remains unavailable to the controller.

Set

```math
\Delta=\delta_0+\sum_{j=1}^{N-1}\delta_j+\sum_{j=1}^N\kappa_j.
```

For either hypothesis, contractivity and a telescoping replacement of the preparation, controls and instruments give total final trace distance at most $`\Delta`$. Every final event probability therefore changes by at most this amount. In particular, with the original final measurement,

```math
|p_X^{\mathrm{actual}}-p_N|\le\Delta,\qquad
|e^{\mathrm{actual}}-p_N/2|\le\Delta.
```

A final binary effect error of at most $`\mu`$ in operator norm adds at most $`\mu`$ to the error bound. An operator-norm error $`\|\widetilde U-U\|\le\epsilon`$ in a unitary gives half diamond distance at most $`\epsilon`$, by applying the triangle inequality to the two terms in $`\widetilde U\rho\widetilde U^\dagger-U\rho U^\dagger`$ and allowing an arbitrary ancillary identity.

Consequently, an absolute error budget of order $`2^{-N}/N`$ per operation is a sufficient conservative schedule for retaining overall absorption and error of order $`2^{-N}`$. Specifying each angle to that absolute resolution requires order $`N+\log N`$ binary digits. This is an upper bound on sufficient accuracy, not a lower bound on necessary accuracy or a claim that a physical calibration realizes those digits. At fixed nonzero error per operation the bound does not establish an exponential advantage. For this same linear bound on a specified environmental record, control the flagged instrument; unflagged channel distance cannot simply replace it without an additional argument. In the passive absorbing model with no photon reinjection, total photon loss is final vacuum population and is controlled by unflagged channel distance.

## Uniform loss in the whole apparatus

Let a photon survive an additional, hypothesis-independent attenuation step with probability $`\lambda`$ after each query. The attenuation acts equally on r, a and b, and a lost photon becomes f permanently. Keep the ideal preparation and controls. Surviving photons undergo exactly the ideal normalized evolution, so

```math
S_N=\lambda^N(1-p_N),\qquad
e_N^{\mathrm{loop}}=\frac{1-\lambda^N(1-p_N)}{2}.
```

The sample still absorbs only at the first query, with probability $`p_N`$, because this model places apparatus loss after each query. The remaining vacuum probability $`(1-p_N)(1-\lambda^N)`$ comes from apparatus loss. The two kinds of loss are physically distinct even when the final detector cannot distinguish them.

For every fixed $`\lambda\lt1`$, the error tends to one half as N grows. The best finite N balances decreasing sample absorption against increasing apparatus loss. Its survival ratio is

```math
\frac{S_{N+1}}{S_N}
=\lambda\,\frac{2(2^N+1)}{2^{N+1}+1}.
```

Near unit survival the maximizing query count is of order $`\log(1/(1-\lambda))`$. This conclusion follows from the explicit ratio, not from applying a universal loss formula outside its hypotheses. Nearby loss-limited sensing models are compared in [Related work](../references/RELATED_WORK.md).

## Loss in the nominally transparent sample modes

Now let $`0\lt\eta\lt1`$ be the intensity transmission of each previously transparent sample mode. Set $`C=|f\rangle\langle f|+|r\rangle\langle r|`$ and take no-event operators

```math
K_A=C+\sqrt\eta\,|a\rangle\langle a|,\qquad
K_B=C-\sqrt\eta\,|a\rangle\langle b|.
```

The missing norm is absorbed into f. For A the event Kraus operators are $`|f\rangle\langle b|`$ and $`\sqrt{1-\eta}|f\rangle\langle a|`$; for B they are $`|f\rangle\langle a|`$ and $`\sqrt{1-\eta}|f\rangle\langle b|`$. The only safe input space is now the common space $`\mathrm{span}\{f,r\}`$. The qualitative impossibility of asymptotically zero-damage discrimination in this situation is already part of Hasenöhrl–Wolf's feasibility/no-go theory. The following direct specialization gives an explicit bound for this model.

### A damage floor for arbitrary strategies

For any finite-query strategy, arbitrary ancillary memory and common causal controls, let $`p_A,p_B`$ be the probabilities of ever absorbing and let $`0\le e\le1/2`$ be the unconditional binary error. Then

```math
\sqrt{p_Ap_B}\ \ge
\frac{1-\eta}{m_\eta}\left(1-2\sqrt{e(1-e)}\right),\qquad
m_\eta=\frac{\sqrt{4+\eta^2}+\eta}{2}.
```

**Proof.** The event effects satisfy $`G_X=I-K_X^\dagger K_X\ge(1-\eta)\Pi`$. The overlap defect is

```math
M=I-K_A^\dagger K_B=\Pi+\eta|a\rangle\langle b|,
\qquad M=\Pi M\Pi,\quad \|M\|=m_\eta.
```

Purify the preparation and all common controls. The latter are then common isometries on an enlarged memory and preserve overlaps. Immediately before call j, denote the unnormalized no-event vectors by $`\alpha_j,\beta_j`$ and their first-event probabilities by $`\ell_{A,j},\ell_{B,j}`$. The change of their overlap at that call has absolute value at most

```math
|\langle\alpha_j|(M\otimes I)|\beta_j\rangle|
\le\frac{m_\eta}{1-\eta}\sqrt{\ell_{A,j}\ell_{B,j}}.
```

The initial overlap is one, the event probabilities sum to $`p_X`$, and Cauchy–Schwarz therefore gives $`|1-z_N|\le m_\eta\sqrt{p_Ap_B}/(1-\eta)`$ for the final no-event overlap. Root fidelity of the full accessible outputs is at least $`|z_N|`$, because the full states include the positive event branches. It is at most $`2\sqrt{e(1-e)}`$ by the fidelity/trace-distance inequality. Combining these statements proves the bound. The general fidelity steps are detailed in [Rate geometry](rate_geometry.md). ∎

At any fixed nonzero transmission loss, a fixed nontrivial discrimination accuracy therefore requires positive damage independent of the number of queries. This is a genuine boundary of the ideal construction.

### A calibrated schedule illustrates the floor

There is also a simple achievable schedule in this lossy model. Put $`g=2\eta`$ and

```math
t_N=\left(2+\eta\sum_{k=0}^{N-1}g^k\right)^{-1},\qquad
|\psi\rangle=\sqrt{1-2t_N}|r\rangle+\sqrt{t_N}(|a\rangle+|b\rangle).
```

After the first call, the unnormalized reference and excitation weights are $`R_1=1-2t_N`$ and $`E_1=\eta t_N`$. Use the same algebraic control formula with $`q_j=E_j/(R_j+E_j)`$; its formula is unitary throughout $`0\le q_j\le1/2`$. The next call gives

```math
R_{j+1}=R_j-E_j,\qquad E_{j+1}=gE_j.
```

The definition of $`t_N`$ gives $`R_N=E_N`$, so the surviving final states are again orthogonal. For $`j\lt N`$, the identity $`R_j=\sum_{k=j}^{N-1}E_k+E_N`$ ensures $`R_j\ge E_j`$, making every control well defined. The total survival and error are

```math
S_N=g^Nt_N,\qquad p_N^{(\eta)}=1-S_N,\qquad
e_N^{(\eta)}=(1-S_N)/2.
```

For $`\eta\gt1/2`$, $`p_N^{(\eta)}\to(1-\eta)/\eta`$. For $`\eta\le1/2`$, survival tends to zero. These are properties of this explicit compensated schedule; no optimality claim is made for it.

## Requiring darkness on an empty device

The binary promise in this project differs from a task in which conclusive reports must also be impossible for an empty device. The latter condition appears in [Chaturvedi et al.'s multipath benchmark](../references/RELATED_WORK.md#multipath-localization-and-general-no-absorption-combs). For the natural empty channel equal to the identity, that additional requirement prevents the present near-certain reporting performance from retaining exponentially low absorption.

Here is a direct task-specific bound. Device A's no-event operator is the projector $`P=I-|b\rangle\langle b|`$, while the empty device has no-event operator I. Purify the preparation and common controls, retaining all their discarded registers for analysis. Denote the final unnormalized no-event A vector by $`\alpha_{A,N}`$ and the normalized empty-device vector by $`\alpha_{\emptyset,N}`$. At call j, let $`\ell_j`$ be the squared norm removed by $`I-P`$ from A's no-event input. These are first-absorption probabilities, so $`\sum_j\ell_j=p_A`$.

In a telescoping product expansion, replace each A projector by the identity, one query at a time. Each difference term has norm $`\sqrt{\ell_j}`$ and is propagated through the later empty-device controls, which are isometries. Hence

```math
\|\alpha_{A,N}-\alpha_{\emptyset,N}\|
\le\sum_{j=1}^N\sqrt{\ell_j}
\le\sqrt{Np_A}.
```

Let $`0\le E_A\le I`$ be a conclusive A-report effect that is exactly dark for the empty device. Positivity implies $`\sqrt{E_A}\alpha_{\emptyset,N}=0`$, and therefore

```math
\begin{aligned}
\Pr(A\text{ report, no absorption}\mid A)
&=\|\sqrt{E_A}(\alpha_{A,N}-\alpha_{\emptyset,N})\|^2\\
&\le Np_A.
\end{aligned}
```

Thus maintaining an A-report probability bounded away from zero under that condition requires absorption at least of order $`1/N`$. If reports on absorption branches are counted too, their contribution is at most $`p_A`$, giving $`(N+1)p_A`$ instead. The no-absorption statistic is the one used in the cited comb benchmark. The statement does not bound every possible average-success task by this same constant, nor does it exclude the pair from the general CP-map framework.

For the explicit ideal protocol, changing only the final measurement is even more restrictive. Put $`p=p_N`$ and let W be the product of its common controls and let $`\alpha_1=\sqrt{1-2p}|r\rangle+\sqrt p|a\rangle`$ be its first no-event A vector. All subsequent A queries act as the identity on that history. Consequently,

```math
\alpha_{A,N}=W\alpha_1,\qquad
\alpha_{\emptyset,N}=W\alpha_1+\sqrt p\,W|b\rangle.
```

The two terms on the right are orthogonal, $`\|\alpha_{A,N}\|^2=1-p`$, and $`\langle\alpha_{\emptyset,N}|\alpha_{A,N}\rangle=1-p`$. Projection onto the complement of the empty output shows that any empty-dark A-report effect has no-absorption A-report probability at most $`p(1-p)`$. The ordinary plus-state report instead occurs with probability $`1-p`$ for the empty device. Exact empty-device darkness is therefore a substantive task constraint, not a free modification of the binary readout.

## What the result does and does not settle

The exact exponential construction, the finite zero-absorption obstruction, the sufficient inverse-N condition and the displayed resource/noise bounds are proved at their stated scope. The optimal rate over all protocols, a complete classification of safe-action geometries, and an experimental demonstration remain separate questions. The fixed known binary pair and its calibrated transparent actions are essential to the present conclusion.
