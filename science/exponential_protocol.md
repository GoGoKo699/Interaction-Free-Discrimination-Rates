# An explicit exponential protocol

This page proves the achieved absorption and error law for the fixed [channel pair](model.md). Three one-photon modes suffice for every N. The no-event branch is a device for analysis; the implemented experiment never selects that branch.

## Theorem

For each integer $`N\ge1`$, one photon, N forward device calls, $`N-1`$ common passive controls and a final measurement produce

```math
\begin{aligned}
p_A=p_B=p_N&=\frac{1}{2^N+1},\qquad s_N=1-p_N,\\
\rho_A&=s_N|+\rangle\langle+|+p_N|f\rangle\langle f|,\\
\rho_B&=s_N|-\rangle\langle-|+p_N|f\rangle\langle f|,\\
|\pm\rangle&=\frac{|r\rangle\pm|a\rangle}{\sqrt2},\qquad
e_* = \frac{p_N}{2}.
\end{aligned}
```

Absorption is counted under either hypothesis, and the equal-prior error includes every run. If a photon is detected, its output mode identifies the device without error. On vacuum, a fair binary guess gives error one half. Equivalently, vacuum can be called an inconclusive outcome with probability $`p_N`$, but the binary-error claim does not discard it.

## 1. Seed a small separation

Prepare the one-photon state

```math
|\psi_N\rangle=
\frac{\sqrt{2^N-1}|r\rangle+|a\rangle+|b\rangle}{\sqrt{2^N+1}}.
```

The first call absorbs the photon with probability $`p_N`$ in either case. Conditional only for the purpose of calculation on no absorption, the normalized output is

```math
|y_\pm(q_1)\rangle=\sqrt{1-q_1}|r\rangle\pm\sqrt{q_1}|a\rangle,
\qquad q_1=2^{-N}.
```

Its unnormalized squared norm is $`s_N=2^N/(2^N+1)`$. Thus the physical state after this call is already a mixture of a surviving photon and the absorbing vacuum. No survival observation is used to decide the next control.

## 2. A common control sends both possibilities to their own safe spaces

For $`0\lt q\le1/4`$, put

```math
|w\rangle=\frac{|a\rangle+|b\rangle}{\sqrt2},\qquad
|z\rangle=\frac{|a\rangle-|b\rangle}{\sqrt2},\qquad
\alpha_q=\sqrt{\frac{1-2q}{1-q}},\quad
\beta_q=\sqrt{\frac{q}{1-q}}.
```

Define the control by its action on the basis:

```math
\begin{aligned}
U_q|f\rangle&=|f\rangle,\\
U_q|r\rangle&=\alpha_q|r\rangle+\beta_q|w\rangle,\\
U_q|a\rangle&=|z\rangle,\\
U_q|b\rangle&=-\beta_q|r\rangle+\alpha_q|w\rangle.
\end{aligned}
```

These four columns are orthonormal because $`\alpha_q^2+\beta_q^2=1`$ and w, z are orthonormal and orthogonal to r. Hence $`U_q`$ is unitary and preserves photon number.

Direct substitution gives the decisive two identities:

```math
\begin{aligned}
U_q|y_+(q)\rangle&=\sqrt{1-2q}|r\rangle+\sqrt{2q}|a\rangle,\\
U_q|y_-(q)\rangle&=\sqrt{1-2q}|r\rangle+\sqrt{2q}|b\rangle.
\end{aligned}
```

The first state is safe for A; the second is safe for B. The same control accomplishes both transformations because the two input pairs have the same Gram matrix. No classical knowledge of which state is present is required.

Applying the unknown channel now incurs no absorption on either surviving history and gives

```math
A_0U_q|y_+(q)\rangle=|y_+(2q)\rangle,\qquad
B_0U_q|y_-(q)\rangle=|y_-(2q)\rangle.
```

The squared excitation q, or equivalently the overlap deficit, doubles. The trace distance itself does not double.

## 3. Iterate and include all branches

After call j the normalized surviving states have

```math
q_j=2^{j-N-1},\qquad j=1,\ldots,N.
```

For each $`j\lt N`$, apply the predetermined $`U_{q_j}`$ and make the next call. All later no-event survival probabilities are one. At the last call $`q_N=1/2`$, so the surviving states are the orthogonal pair $`|+\rangle,|-\rangle`$.

Any photon absorbed at the first call remains in f: both channels and all controls fix f. Consequently the full normalized outputs are exactly the two states in the theorem. Their difference has eigenvalues $`s_N,-s_N,0,0`$, so its trace norm is $`2s_N`$ and the Helstrom formula gives $`e_*=p_N/2`$.

For $`N=1`$ there are no intermediate controls; the same proof gives absorption one third and error one sixth. The general argument uses exact identities rather than a numerical limiting extrapolation.

## Why the rate is possible

The first weak interrogation pays for a small hypothesis-dependent separation. Subsequent calls see different safe input states, while the controls remain common. The safe actions change the cross overlap between these states, allowing that separation to grow without further absorption. This mechanism is ruled out by the cross-inner-product condition in the [inverse-N theorem](rate_geometry.md), but is not ruled out merely by orthogonality of the exclusive safe input spaces.

The physical-vacuum branch is populated only when the photon is lost, and all subsequent operations fix it. The mode r in the coherent seed is an occupied reference mode, not vacuum. Equating these two states would erase the distinction between an absorbed photon and a surviving reference photon and would give the wrong physical model.

The [resource account](resources.md) supplies a two-rotation implementation of each control, sample passage totals and the accuracy assumptions. The [zero-absorption theorem](zero_absorption.md) explains why the exponentially decreasing sequence cannot be replaced by a finite exactly absorption-free discriminator.
