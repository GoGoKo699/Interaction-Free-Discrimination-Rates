# The optimal interaction rate

Two known channels can agree whenever both are safe to use and still be distinguishable with exponentially small damage. The optimal rate depends on a linear map that combines their actions on safe inputs.

## Classification

Consider two fixed memoryless channels on the same finite-dimensional space $` \mathcal H `$ with a designated common pure input vacuum $`v`$. Under each channel the vacuum has a pure output, and its induced environmental vacuum defines a single no-event contraction $`K_X`$. All other Kraus branches count as an event. The discriminator can make at most $`N`$ forward calls and use arbitrary finite protected memory and common adaptive controls, with no access to the device environment. See the [event convention](rate_geometry.md#notation-and-the-environmental-event).

Let $`e`$ be the unconditional equal-prior error and $`p=\max(p_A,p_B)`$ the worst-case probability of at least one event. For fixed $`0<\epsilon<1/2`$, define $`p_N^*(\epsilon)`$ as the infimum of $`p`$ subject to $`e\le\epsilon`$. Write

```math
S_X=\ker(I-K_X^\dagger K_X),\qquad V=S_A\cap S_B.
```

Each restriction $`K_X|_{S_X}`$ is isometric. If the physical vacuum outputs coincide, align phases so $`K_Av=K_Bv=u`$. If the two restrictions agree on $`V`$, the linear map extending both is

```math
L:S_A+S_B\longrightarrow\mathcal H,\qquad
L(a-b)=K_Aa-K_Bb,\qquad \sigma=\|L\|,
```

for $`a\in S_A,b\in S_B`$. Two representations of $`a-b`$ differ by a vector in $`V`$, so agreement makes the definition unambiguous. Since $`Lv=u`$, $`\sigma\ge1`$.

| Channel pair | Optimal worst-case interaction probability |
|---|---|
| The vacuum outputs differ, or the aligned safe actions differ on $`V`$. | Exactly zero for sufficiently large $`N`$. |
| The aligned safe actions agree on $`V`$ and $`\sigma>1`$. | $`\Theta(\sigma^{-2N})`$. The same construction attains unconditional error $`O(\sigma^{-2N})`$. |
| The aligned safe actions agree on $`V`$, $`\sigma=1`$, and $`S_A\ne S_B`$. | $`\Theta(1/N)`$. |
| The aligned actions agree on the same safe space and the channels are distinct. | $`\Theta(1)`$. |
| The channels are identical. | The target error is infeasible for every $`N`$. |

The constants depend on the fixed pair and, for the lower bounds, the error target. The condition $`\sigma=1`$ is equivalent to preserving all cross inner products between the two safe spaces. In one direction $`I-L^\dagger L`$ is positive and has zero quadratic form on both spaces. It thus vanishes on their sum. In the other direction preservation of the cross products and individual norms preserves the norm of every $`a-b`$. This recovers the [common-unitary condition](rate_geometry.md#interpretation-as-a-common-unitary).

Different vacuum outputs can be tested by repeating a vacuum call at zero event cost. For aligned actions differing on $`V`$, there is a distinct output on some pure state in $`V`$. Indeed, the channel sends $`|v\rangle\langle z|`$ to $`|u\rangle\langle K_Xz|`$. Different actions on this matrix element imply different actions on some state supported on $`V`$. Independent repetitions of that safe test achieve the fixed error.

For unequal safe spaces choose labels so some $`a\in S_A`$ lies outside $`S_B`$. Channel $`A`$ is isometric on $`S_A`$. The images of $`|v\rangle\langle a|`$ differ because $`\|K_Aa\|=\|a\|>\|K_Ba\|`$. Thus [Hasenöhrl and Wolf, Theorem 2.5](../references/RELATED_WORK.md#hasenoehrl-wolf) applies to the singleton channel alternatives with subspace $`S_A`$. It gives zero interaction under one hypothesis, $`O(1/N)`$ under the other and $`O(1/N^2)`$ unconditional error. The converse below matches that cost when $`\sigma=1`$.

## Converse for arbitrary adaptive controls

Pad a stopped branch with vacuum calls while keeping its output in protected memory. These calls add no events. Purify the initial state and represent each common control by a Stinespring isometry, keeping its purifying registers untouched after their creation. This also represents classical control. Tracing out the extra registers recovers the original accessible output. In this larger space each all-no-event trajectory is a single subnormalized vector. The full lifted output consists of that rank-one contribution plus the positive event part of trace $`p_X`$.

Let $`x_t,y_t`$ be the two no-event vectors before query $`t+1`$, with the last common control included in $`x_N,y_N`$. Write $`d_t=\|x_t-y_t\|`$, so $`d_0=0`$. Let $`P_X`$ project onto $`S_X`$ and $`Q_X=I-P_X`$. Query operators are tensored with identity on the controller memory. The loss at this call is

```math
\ell_{A,t}=\langle x_t|(I-K_A^\dagger K_A)|x_t\rangle,\qquad
\ell_{B,t}=\langle y_t|(I-K_B^\dagger K_B)|y_t\rangle.
```

The losses sum to $`p_X=\sum_{t=0}^{N-1}\ell_{X,t}`$. In finite dimension $`I-K_X^\dagger K_X\ge\gamma_X Q_X`$ for some $`\gamma_X>0`$. If $`Q_X=0`$, take $`\gamma_X=1`$. Apply $`L`$ to the difference of the safe projections and use that each $`K_X`$ is contractive on the remainder:

```math
\begin{aligned}
d_{t+1}
&\le \sigma\|P_Ax_t-P_By_t\|+\|Q_Ax_t\|+\|Q_By_t\|\\
&\le \sigma d_t+(1+\sigma)
   \left(\sqrt{\ell_{A,t}/\gamma_A}+\sqrt{\ell_{B,t}/\gamma_B}\right).
\end{aligned}
```

Tensoring with identity preserves the norm of $`L`$. Iteration and Cauchy–Schwarz give

```math
d_N\le(1+\sigma)(\gamma_A^{-1/2}+\gamma_B^{-1/2})
\sqrt p\left(\sum_{j=0}^{N-1}\sigma^{2j}\right)^{1/2}.
```

The two survivor vectors have norm at most one, so the trace distance between their rank-one contributions is at most $`d_N`$. Restoring the event parts puts the full trace distance at most $`d_N+(p_A+p_B)/2`$. The target error requires trace distance at least $`1-2\epsilon`$. Either $`p`$ already exceeds $`(1-2\epsilon)/2`$, or that error target forces $`d_N\ge(1-2\epsilon)/2`$. The displayed sum yields $`\Omega(\sigma^{-2N})`$ for $`\sigma>1`$ and $`\Omega(1/N)`$ for $`\sigma=1`$.

For identical safe spaces $`S`$ and agreement there, $`D=I-K_A^\dagger K_B`$ annihilates $`S`$ on both sides. The one-query change in overlap is $`-\langle x_t|D|y_t\rangle`$. Each term is bounded in modulus by $`\|D\|\sqrt{\ell_{A,t}\ell_{B,t}/(\gamma_A\gamma_B)}`$. Consequently

```math
1-\operatorname{Re}\langle x_N|y_N\rangle
\le \frac{\|D\|}{\sqrt{\gamma_A\gamma_B}}\sqrt{p_Ap_B}.
```

This makes $`d_N=O(\sqrt p)`$, uniformly in $`N`$. The full output bound now forces positive $`p`$. Any distinct channels give different outputs on some input, so ordinary repeated tests can reach the fixed error at cost at most one. This recovers the floor in [Hasenöhrl and Wolf, Theorem 2.9](../references/RELATED_WORK.md#hasenoehrl-wolf).

## Constructing the optimal exponential protocol

Suppose the aligned actions agree on $`V`$ and $`\sigma>1`$. The experimenter knows the two candidate channels and can calculate all controls in advance.

### One weak seed

Choose unit $`z`$ with $`K_Az\ne K_Bz`$. Otherwise a common contraction would extend both actions, contradicting $`\sigma>1`$. Prepare the same input under both hypotheses,

```math
\sqrt{1-q_0}\,|v\rangle|r\rangle+\sqrt{q_0}\,|z\rangle|b_0\rangle,
```

using orthogonal protected labels $`r,b_0`$. The seed event probability under $`X`$ is $`q_0(1-\|K_Xz\|^2)`$. Divide the no-event inner product $`1-q_0+q_0\langle K_Az|K_Bz\rangle`$ by the product of the two survival norms. Taking the modulus gives the deficit from one

```math
s_{\mathrm{seed}}(q_0)=\frac{q_0}{2}\|K_Az-K_Bz\|^2+O(q_0^2).
```

The derivative is positive. Any sufficiently small positive deficit can therefore be prepared at event cost proportional to that deficit.

### Amplification without further events on surviving histories

Choose $`a\in S_A,b\in S_B`$ such that $`a-b`$ is a nonzero maximizing direction of $`L`$. Their norms may differ. For small $`q\ge0`$, the following normalized inputs are safe for their respective channels:

```math
\begin{aligned}
h_A(q)&=\sqrt{1-q\|a\|^2}|v\rangle|r\rangle+\sqrt q\,|a\rangle|b_0\rangle,\\
h_B(q)&=\sqrt{1-q\|b\|^2}|v\rangle|r\rangle+\sqrt q\,|b\rangle|b_0\rangle.
\end{aligned}
```

Their overlap is $`\sqrt{(1-q\|a\|^2)(1-q\|b\|^2)}+q\langle a|b\rangle`$. The same formula at the output has $`u`$ as reference and the two safe images in the overlap. Expanding the moduli gives

```math
s_{\rm in}(q)=\frac{q}{2}\|a-b\|^2+O(q^2),\qquad
s_{\rm out}(q)=\frac{q}{2}\|L(a-b)\|^2+O(q^2).
```

Therefore the analytic map $`f=s_{\rm out}\circ s_{\rm in}^{-1}`$ satisfies $`f(s)=\sigma^2s+O(s^2)`$. Its local inverse $`g`$ is increasing with $`g(s)=\sigma^{-2}s(1+O(s))`$. Fix a sufficiently small positive final deficit $`s_*`$. The initial deficit for $`m`$ amplification queries is $`g^m(s_*)`$. The backward iterates shrink geometrically, so the deviations of the relative factors $`1+O(g^j(s_*))`$ are absolutely summable and each factor stays positive. Their product is bounded above and away from zero independently of $`m`$. Thus $`g^m(s_*)=\Theta(\sigma^{-2m})`$, with the exact exponential factor.

At each step the current normalized survivor pair and the chosen next input pair have equal overlap modulus. Rephase the representatives of the pure-state rays so their Gram matrices coincide. The isometry between these two pairs extends to a unitary on the full space. This gives one scheduled control that works under either hypothesis. The construction never reads the environment.

### A finite suffix makes the survivors orthogonal

Choose unit $`a'\in S_A,b'\in S_B`$ with a changed safe cross inner product. Rephase $`b'`$ so $`c_{\rm in}-c_{\rm out}=\Delta>0`$ is real, where $`c_{\rm in}=\langle a'|b'\rangle`$ and $`c_{\rm out}=\langle K_Aa'|K_Bb'\rangle`$. Let $`r_0\in[0,1-s_*]`$ be the survivor overlap after a phase choice. Use next inputs composed of a vacuum component of weight $`1-q`$ and the flagged safe components $`a',b'`$ of weight $`q`$. Choose the two vacuum reference states in a two-dimensional protected space orthogonal to the flag. Give them inner product $`t=(r_0-qc_{\rm in})/(1-q)`$. For $`q\le s_*/4`$, $`|t|\le (r_0+q)/(1-q)\le1`$.

The input overlap is $`r_0`$ and the output overlap is $`r_0-q\Delta`$. As before one common unitary maps the current pair to these inputs. Set $`q=\min(s_*/4,r_0/\Delta)`$ to reach zero in a number of safe queries depending only on the fixed pair and $`s_*`$. A protected space of dimension three suffices for the seed, amplification and suffix.

The seed and suffix take a fixed number of calls. Allocate the remaining calls to amplification. All events are charged, but only the seed can cause the first one. Therefore $`p=O(\sigma^{-2N})`$. Since the final measurement can distinguish the no-event states perfectly, the unconditional error satisfies $`e\le(p_A+p_B)/2\le p`$.

## Optical example and scope

For the [original optical pair](model.md), the exclusive safe inputs $`a,b`$ are orthogonal while their outputs are $`a,-a`$. On those two input directions $`L`$ has row $`(1,-1)`$, and it sends the common safe space isometrically into an orthogonal output space. Thus $`\sigma^2=2`$. The three-mode optical construction attains $`p=(2^N+1)^{-1}`$ and $`e=p/2`$, so its $`2^{-N}`$ order is optimal even against arbitrary causal controllers.

If each safe space contributes one direction orthogonal to the shared space, and these two directions are orthogonal to each other, their unit output overlap $`c`$ gives $`\sigma^2=1+|c|`$. For nonorthogonal exclusive directions use the largest generalized eigenvalue of the output Gram matrix relative to the input Gram matrix on those directions. The [finite checks](../verification/README.md) exercise both input geometries.

The cost is the probability of an environmental event, such as photon absorption. The query model supplies known candidate channels, noiseless protected memory and exact pair-calibrated common controls. The [optical resource account](resources.md) separately treats passage, precision and loss for the original implementation. The constants are pointwise in the channel pair and can change as the safe-space dimensions change.
