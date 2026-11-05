# Delayed-basis guessing and continuing noisy-memory processing

[Science guide](README.md) · [Finite guessing theorem](guessing-bound.md) · [Authoritative dynamical proof](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/afba6ae9315ac415189d972fa604658168e5524b/science/guessing_processing.md)

Unconditional whole-string BB84 guessing success implies a continuing processing budget in a specified noisy-memory model. The finite guessing theorem supplies an information bottleneck; the Pauli-envelope contraction and processing ledger belong to [Measurement-Free-Memory-Cost](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost). This chapter states their composition and its operational limits. The prior recovery route implies both convenient mean-rank floors stated below. A further exponential-moment estimate retains the actual noise probabilities and strengthens the dynamical inference in the same model.

## Experiment and charged device model

Here $`k\geq1`$ is the number of challenge qubits, $`n`$ is the total noisy persistent physical width, and $`D`$ counts full noise rounds. This notation is local to the noisy application: in the [ideal dimension theorem](model.md), $`n`$ counts challenge qubits and $`D`$ denotes a quantum dimension.

Choose independent uniform $`X,\Theta\in\{0,1\}^k`$. Give the device only $`|X\rangle_\Theta`$. Keep $`X`$ secret and disclose only $`\Theta`$, after all charged storage operations have ended. The score is

```math
p=\Pr[\widehat X=X],\qquad d=2^k.
```

This is unconditional average exact whole-string success, including input randomness, noise and processing outcomes. Aborts count as failures. There is no conditioning on acceptance, successful noise histories or selected outcomes.

Each of the $`n`$ persistent qubits undergoes independent depolarizing noise in every round, with

```math
\mathcal N_\gamma=(1-\gamma)\mathrm{id}
+\gamma\mathcal R_{I/2},
\qquad q=1-\gamma\in(0,1),\qquad\kappa=-\ln q.
```

Every persistent data, syndrome, controller, resource and auxiliary record is noisy and included in $`n`$. The storage circuit has a fixed schedule. Its free interior primitives are ideal global Clifford operations and input-independent replacement resets, which may prepare arbitrary fixed magic states. Actual interior $`T`$ and $`T^\dagger`$ gates are charged. Any other primitive needs its actual implementation or a proved Pauli-rank growth charge. A nonlinear classical decision, controlled operation or data-dependent reset does not become free merely because its controller is counted.

Initial encoding and final basis-dependent decoding may be arbitrary free CPTP maps, using fresh uncorrelated endpoint workspace. No protected record or correlated side channel crosses the charged interval. Final decoding may include unrestricted nonlinear processing of the accumulated noisy records. These assumptions define the device class to which the inference applies.

## One full-output envelope gives a genuine quantum-plus-classical encoder

Initialize a single backward Pauli envelope at the full physical output, **before** basis-dependent readout. Its initial binary dimension is $`M=2n`$. The same envelope covers every final basis and every readout; an arbitrary endpoint decoder does not justify replacing $`M`$ by $`2k`$.

At a primitive cut $`t`$, average the earlier noise into a CPTP prefix $`\Pi_t`$. A realization $`b`$ of the future replacement-noise choices selects a CPTP full-output tail $`\mathcal S_{b,t}`$. Independent noise makes $`\Pi_t`$ independent of $`b`$. The simultaneous envelope $`V_{b,t}\leq\mathbb F_2^{2n}`$ satisfies

```math
\mathrm{range}\mathcal S_{b,t}^\dagger
\subseteq\mathcal A_{V_{b,t}},
\qquad r=\dim V_{b,t}.
```

If the symplectic form restricted to $`V_{b,t}`$ has rank $`2s`$, put $`c=r-2s`$. A Clifford change of coordinates gives

```math
\mathcal A_V\simeq
M_{2^s}\otimes\mathrm{Diag}_{2^c}\otimes I_G.
```

The trace-preserving conditional expectation onto this algebra is CPTP and self-adjoint. Thus $`\mathcal S_{b,t}=\mathcal S_{b,t}\circ\mathcal E_V`$. Moreover, $`\mathcal E_V=\mathcal J_V\circ\mathcal F_V`$: the CPTP map $`\mathcal F_V`$ changes coordinates, dephases the $`c`$-bit factor and traces out the gauge factor $`G`$; the CPTP map $`\mathcal J_V`$ reinserts $`I_G/\dim G`$ and reverses the coordinate change.

Consequently $`\mathcal F_V\circ\Pi_t`$ is a normalized CPTP encoder with an $`s`$-qubit quantum output and a classical register of $`2^c`$ values. Composing $`\mathcal J_V`$, the tail and the actual basis-dependent readout supplies a CPTP decoder reproducing the original output distribution. This factorization is what permits applying the guessing theorem at the cut.

The labels $`b`$ are mathematical noise flags, not information supplied physically. For an upper bound one may optimize the decoder separately for each branch. Here $`p_{b,t}`$ is the actual fixed endpoint decoder's score on the sampled channel; optimizing separately only upper-bounds it. Linearity still gives the actual score $`p=\mathbb E_b p_{b,t}`$ at every cut, on either side of every primitive. There is no branch postselection.

## Score-dependent expected-rank floor

Two bounds apply to that genuine encoder, independently:

```math
p_{b,t}\leq
\min\{1,2^{(s-k)/6},2^{s+c-k}\}.
\qquad\text{(N1)}
```

The first nontrivial term is [Theorem G](guessing-bound.md), allowing arbitrary classical information. For the second, fix a basis. Its $`d`$ equiprobable inputs give density matrices $`\rho_x\leq I_{QC}`$, so any POVM obeys $`d^{-1}\sum_x\mathrm{Tr}M_x\rho_x\leq\dim(QC)/d`$. Apply this finite-alphabet count before the optional classical pure-state refinement inside Theorem G's proof; its extra proof labels are not part of the physical $`c`$-bit register.

The immediate quantum-dimension term gives $`R_t\geq a_G`$ at every cut, where

```math
R_t=\mathbb E_b\dim V_{b,t},\qquad
a_G=2k\left[\frac{p-2^{-k/6}}{1-2^{-k/6}}\right]_+,
\qquad [x]_+=\max\{x,0\}.
```

Retaining both terms in (N1) gives a stronger floor. Maximizing over $`0\leq s\leq r/2`$, with $`r=2s+c`$, yields the branch upper curve

```math
h_k(r)=
\begin{cases}
2^{r-k},&0\leq r\leq5k/6,\\
2^{(r-2k)/7},&5k/6\leq r\leq2k,\\
1,&r\geq2k.
\end{cases}
```

Each exponential piece is convex. For $`k\geq8`$, its kink lies below the chord from $`(0,2^{-k})`$ to $`(2k,1)`$. Branchwise chord domination followed by averaging therefore gives

```math
R_t\geq a_k(p):=
2k\left[\frac{p-2^{-k}}{1-2^{-k}}\right]_+,
\qquad k\geq8.
\qquad\text{(N2)}
```

For completeness, put $`b_0=2^{-k}`$, $`H=2^{-k/6}`$, and $`t_0=5k/6`$. For $`1\leq k\leq7`$, use the concave polygon through $`(0,b_0),(t_0,H),(2k,1)`$. Its inverse gives the all-cut floor

```math
a_k(p)=
\begin{cases}
0,&p\leq b_0,\\
t_0(p-b_0)/(H-b_0),&b_0\lt p\leq H,\\
t_0+(2k-t_0)(p-H)/(1-H),&H\leq p\leq1.
\end{cases}
\qquad\text{(N3)}
```

These floors are positive for every score above random guessing, including scores at or below one half. The averaging concerns expected rank; it does not require every noise branch to retain that rank. The curves are necessary upper bounds, not claims of optimal attainable guessing. The [companion proof](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/afba6ae9315ac415189d972fa604658168e5524b/science/guessing_processing.md) supplies the envelope coupling, chord argument and finite checks.

## Gate budget and every contiguous interval

Use any proved positive floor $`a`$ above. Let $`b_g`$ be a valid upper bound on binary-envelope rank growth across charged gate $`g`$, and $`B=\sum_g b_g`$. Backward noise contracts expected rank by at least a factor $`q`$, free primitives do not increase it, and a charged gate increases it by at most $`b_g`$. The existing dynamical ledger then gives

```math
B\geq a\left[D\kappa-\ln(2n/a)\right]_+.
\qquad\text{(N4)}
```

A $`T`$ or $`T^\dagger`$ gate has charge one. Its actual count satisfies the sharper integer-gate inequality

```math
m_T\geq
\left\lceil
\frac{[D\kappa-\ln(2n/a)]_+}{\ln(1+1/a)}
\right\rceil.
\qquad\text{(N5)}
```

The exact continuous scalar injection relaxation gives another necessary bound,

```math
\begin{aligned}
B&\geq\mathcal L(D,2n,a,q),\\
\mathcal L(D,M,a,q)
&=\max\!\left\{0,\max_{1\leq\ell\leq D}
\left[\frac aq+(D-\ell)\frac{(1-q)a}{q}
-Mq^{\ell-1}\right]\right\}.
\end{aligned}
\qquad\text{(N6)}
```

Set $`\mathcal L(0,M,a,q)=0`$. For integer T count, round (N6) up and use the stronger applicable bound. Scalar optimality does not supply a matching physical circuit or a sufficient gate budget.

For **any contiguous interval** $`I`$ between primitive cuts, let $`D_I`$ count its full noise layers, let $`B_I`$ count only charges inside it, and let $`M_I`$ upper-bound the expected entering envelope rank at its later cut. One may always take $`M_I=2n`$. The same global score floor holds throughout, giving

```math
B_I\geq\mathcal L(D_I,M_I,a,q),\qquad
B_I\geq a[D_I\kappa-\ln(M_I/a)]_+.
\qquad\text{(N7)}
```

For individual T/T-dagger counts, (N5) also holds with $`m_T,D,2n`$ replaced by $`m_{T,I},D_I,M_I`$. Assign boundary gates consistently. The later suffix may determine the interval's entering random envelope, but its noise is independent of the interval's noise. Gates outside the interval cannot supply its continuing charge after the finite width reserve is exhausted. Any interval containing a noise layer also requires $`a\leq2nq`$ for feasibility.

For example, $`k=12`$, $`p=0.4`$, $`n=120`$, $`\gamma=0.01`$, and $`D=2000`$ give $`a\simeq9.59648`$. Equation (N5) requires at least **171** interior T/T-dagger gates. A 700-round contiguous interval requires at least **39** such gates by the interval form of (N5). The scalar injection bound in (N7) alone gives $`B_I\geq36.8048`$, or 37 gates after rounding. These are necessary conditions in the model; feasibility is a separate question.

## Existing recovery reductions already cover low scores

The comparison must include the finite BB84 recovery reduction of [Dupuis, Fawzi and Wehner](../references/RELATED_WORK.md#recovery-comparison-for-the-noisy-processing-application). For one channel, let $`F_{\mathrm{rec}}`$ be optimum squared Bell recovery fidelity, $`F_{\mathrm{pg}}`$ its pretty-good value, and $`u`$ average pretty-good guessing success. Write $`p_*\geq\max\{p,1/d\}`$ for optimal average guessing success. Renes's finite-alphabet discrimination bound, applied to each basis and averaged by convexity, gives

```math
g_d(p_*):=p_*^2+\frac{(1-p_*)^2}{d-1}\leq u.
```

DFW's threshold estimate is $`u\leq S_\ell F_{\mathrm{pg}}+\tau_\ell`$, where $`S_\ell=\sum_{j=0}^{\ell}\binom kj`$ and $`\tau_\ell=2^{-\ell-1}\mathbf1_{\ell\lt k}`$. Retaining the normalization of the spectral weights in the same argument strengthens it to

```math
\begin{aligned}
u&\leq\tau_\ell+A_\ell F_{\mathrm{pg}},\\
A_\ell&=\sum_{j=0}^{\ell}\binom kj(1-2^j\tau_\ell),
\qquad 0\leq\ell\leq k.
\end{aligned}
```

Indeed, DFW's normalized spectral weights satisfy $`w_v\geq0`$, $`\sum_vw_v=1`$ and $`w_v\leq F_{\mathrm{pg}}`$. The BB84 spectrum has coefficient $`2^{-j}`$ on $`2^j\binom kj`$ Pauli labels of weight $`j`$, and zero on labels containing $`Y`$. Subtracting $`\tau_\ell\sum_vw_v`$, discarding nonpositive terms and bounding the remaining weights by $`F_{\mathrm{pg}}`$ yields the displayed coefficient $`A_\ell\leq S_\ell`$. The [companion comparison](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/afba6ae9315ac415189d972fa604658168e5524b/science/guessing_processing.md) gives the source equations and complete derivation.

Since $`F_{\mathrm{rec}}\geq F_{\mathrm{pg}}`$, this implies

```math
F_{\mathrm{rec}}\geq
\max_{0\leq\ell\leq k}
\frac{[g_d(p_*)-\tau_\ell]_+}{A_\ell}.
```

One may substitute any certified score $`p\geq1/d`$ because $`g_d`$ is increasing on that range. The bound remains useful at or below one half. A measure-and-prepare decoder also gives $`F_{\mathrm{rec}}\geq p_*/d`$, above replacement fidelity $`1/d^2`$ for every above-random score. The case $`\ell=0`$ gives the complementary-pair bound $`u\leq(1+F_{\mathrm{pg}})/2`$. It also follows from the Berta–Coles–Wehner complete-MUB identity applied separately to each complementary product stabilizer-basis pair. The entire product-BB84 collection is not itself a complete MUB set or a 2-design.

For each noise branch, every recovered logical CPTP channel factors through $`\mathcal E_V`$, so the companion channel-rank bound gives $`F_{\mathrm{rec},b}\leq\min\{1,2^{r-2k}\}`$. Applying the prior recovery reductions **branchwise before averaging** already yields (N2) for every $`k\geq8`$. The companion proves this analytically for $`k\geq11`$ and checks the remaining 54 integer ranks at $`k=8,9,10`$ with exact rational certificates. For $`1\leq k\leq7`$, the same spectral bounds imply the polygon floor (N3): 49 exact rational certificates cover the interior integer ranks, with the zero-rank and full-rank endpoints handled directly. The direct quantum-plus-classical factorization therefore adds no gate or interval consequence from either displayed floor, for any $`k\geq1`$. This comparison concerns (N2) and (N3); it does not assert that the recovery bounds dominate every possible refinement or determine optimal guessing.

## Exponential moments strengthen the dynamical inference

The mean-rank floors above replace the sampled ranks by an arbitrary mixture with the same expectation. The actual product-noise process contains more information. The [companion theorem](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/afba6ae9315ac415189d972fa604658168e5524b/science/moment_processing.md) retains, for a fixed $`z\gt 1`$,

```math
X_{z,t}=\log_z\mathbb E_b[z^{r_{b,t}}],
\qquad
\alpha_z=\frac{\ln(1-q+qz^2)}{2\ln z}.
```

At a noise layer, choose independent binary coordinate pivots for the incoming envelope. The surviving subspace can use only pivots on retained qubits. Each site has at most two pivots, and pairing the one-pivot factors gives

```math
\mathbb E[z^{r'}\mid V]\le(1-q+qz^2)^{r/2}.
```

Independent noise and Jensen's inequality imply $`X_z'\le\alpha_zX_z`$. A T/T-dagger gate gives $`X_z'\le X_z+1`$; Clifford operations and input-independent resets do not increase it. These are updates of the same full-output envelope, without supplying any branch flag to the device.

### Direct score floor

For $`1\lt z\le2^{1/7}`$, the two exponential pieces of $`h_k(r)`$ above are convex functions of $`Y=z^r`$. Put $`b=2^{-k}`$, $`H=2^{-k/6}`$, and let $`P_z`$ be the least concave polygon above the three knots

```math
(1,b),\qquad (z^{5k/6},H),\qquad(z^{2k},1),
```

continued constantly after $`z^{2k}`$. Keep the middle knot if it lies above the endpoint chord; otherwise use that chord. Convexity of each piece proves $`h_k(r)\le P_z(z^r)`$. Averaging the actual branch scores and applying Jensen gives

```math
p\le P_z(\mathbb E[z^r]),\qquad
X_{z,t}\ge a_{z,\mathrm{dir}}:=\log_z[P_z^{-1}(p)]
```

at every primitive cut. The inverse is the increasing piecewise-linear inverse on $`b\le p\le1`$; set the floor to zero for $`p\le b`$. Thus every above-chance score supplies a positive floor. This direct route combines Lattice's finite guessing theorem with the actual noise distribution. In the limit $`z\downarrow1`$, it recovers the preceding convenient mean-rank floors.

### Complementary recovery floor

For $`1\lt z\le2`$, let $`F_0\ge4^{-k}`$ be a certified lower bound on optimum squared Bell recovery fidelity of the averaged full channel. For $`p\ge2^{-k}`$, the preceding recovery inequalities supply such a value, for example

```math
F_0=\max\left\{4^{-k},\frac{p}{2^k},
\max_{0\le\ell\le k}\frac{[g_{2^k}(p)-\tau_\ell]_+}{A_\ell}\right\}.
```

Choose one CPTP recovery attaining at least this bound and keep it fixed across future-noise branches. The branchwise superoperator-rank cap and linearity of Bell fidelity then give, at every primitive cut,

```math
X_{z,t}\ge a_{z,\mathrm{rec}},\qquad
a_{z,\mathrm{rec}}=\log_z\left[1+w(z^{2k}-1)\right],\qquad
w=\frac{F_0-4^{-k}}{1-4^{-k}}.
```

The secant of the convex power $`(z^r)^{\ln2/\ln z}`$ proves this floor from $`F_{\mathrm e,b}\le\min\{1,2^{r-2k}\}`$. The recovery tools remain inherited inputs. These two moment floors concern a stronger dynamical statistic than the convenient mean-rank floors compared above; no claim of an optimum pointwise guessing curve is needed.

### Gate and interval consequences

Use either valid positive floor $`a_z`$, and put $`\kappa_z=-\ln\alpha_z`$. The full-output terminal potential is $`X_z=2n`$, so the same scalar ledger yields

```math
m_T\ge\left\lceil
\frac{[D\kappa_z-\ln(2n/a_z)]_+}{\ln(1+1/a_z)}
\right\rceil,\qquad
m_T\ge\left\lceil\mathcal L(D,2n,a_z,\alpha_z)\right\rceil.
```

Optimize over the valid $`z`$ ranges and retain the strongest applicable bound, including the preceding mean-rank laws. For a contiguous interval, replace $`2n`$ by a proved upper bound on its entering $`X_z`$, or retain $`2n`$. A bound only on entering $`\mathbb E[r]`$ cannot be substituted, since a logarithmic moment can exceed the mean.

A certified finite illustration uses $`k=12`$, $`p=2/5`$, $`n=120`$, $`q=99/100`$ and $`z=27/25`$. Combining the direct quantum-dimension, output-dimension and established classical-memory caps gives a concave moment polygon with knots $`(1,1/4096)`$, $`(z^{11},1/4)`$ and $`(z^{24},1)`$. Exact certificates check all 169 integer quantum-plus-classical pairs with $`0\le2s+c\le24`$; higher ranks use the constant cap one. Its inverse gives

```math
\mathbb E[z^r]\ge\frac{4z^{11}+z^{24}}5,
\qquad a_z\simeq14.84083.
```

For $`D=2000`$, the individual-T bound requires at least **244** gates, compared with 171 from the convenient mean-rank ledger. A 700-round interval with entering potential bounded by $`2n=240`$ requires at least **58**, compared with 39. These are verified necessary counts, without a claim that the parameter choices are physically attainable or that the chosen moment polygon is globally optimal. The companion proof and its [canonical verifier](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/afba6ae9315ac415189d972fa604658168e5524b/verification/verify_moment_processing.py) give the exact rational certificates and logarithmic enclosures.

For fixed $`p\ge p_0\gt 0`$ and fixed $`q\in(0,1)`$, the direct profile gives $`a_z=2k-o(k)`$ for a suitable sequence $`z\downarrow1`$, while $`\alpha_z=q+o(1)`$. The complementary recovery route gives the same leading conclusion. Along $`n\ge k`$, $`k\to\infty`$, $`D\to\infty`$ and $`\ln(n/k)=o(D)`$, the discrete ledger implies

```math
m_T\ge(2-o(1))\,kD\,\frac{1-q}{q}.
```

The convenient score-only mean-rank floor has leading coefficient $`2p`$ in the same comparison. Thus the moment estimate strengthens the fixed-score coefficient, while preserving the weak-noise order $`k\gamma D`$. If the normalized processing count stays strictly below the displayed limiting coefficient, unconditional whole-string success must tend to zero. This is a necessary converse, not a matching physical circuit or verification of the device premises.

## Explicit quantitative decay

Retain the companion notation $`k`$ challenge qubits, $`n`$ total noisy width, $`D`$ rounds, $`q=1-\gamma`$, and prescribed gate count $`m_T`$. For $`1\lt z\le2^{1/7}`$, put $`\alpha=\alpha_z`$ as above and $`M=2n`$. The [companion finite inversion](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/afba6ae9315ac415189d972fa604658168e5524b/science/guessing_decay.md) gives, for $`D\ge1`$,

```math
U_z=\min\left\{M\alpha,\;\min_{1\le\ell\le D}
\frac{\alpha(m_T+M\alpha^{\ell-1})}
{1+(D-\ell)(1-\alpha)}\right\},
\qquad p\le\min\{1,z^{U_z-2k}\}.
```

The term $`M\alpha^{\ell-1}`$ retains the initial width allowance. Any established nondecreasing concave branch-score majorant $`P_z`$ also gives the stronger finite consequence $`p\le P_z(z^{U_z})`$. The [three-input finite bound](finite-guessing.md) supplies one such improvement before concavification; its rational certificate survives arbitrary branch averaging.

Fix $`q\in(0,1)`$ and finite $`\rho\ge0`$. Along any family with $`k,D\to\infty`$, $`n\ge k`$, $`\ln(n/k)=o(D)`$ and $`\limsup m_T/(kD)\le\rho`$,

```math
\liminf\frac{-\ln p}{k}\ge E_q(\rho),\qquad
E_q(\rho)=\sup_{1\lt z\le2^{1/7}}
(\ln z)\left[2-\rho\frac{\alpha_z}{1-\alpha_z}\right]_+.
```

This exponent is positive exactly when $`0\le\rho\lt2(1-q)/q`$. The proof fixes $`z`$ first, coasts for $`o(D)`$ rounds to reduce the reserve to at most $`k`$, applies the finite inverse, and only then takes the supremum. At $`p=0`$ use $`-\ln p=+\infty`$. This is an explicit decay guarantee under the same device premises, not an achievable processing capacity or a simultaneous weak-noise limit.

### Keeping the full generating function

Write $`M_z=\mathbb E_b[z^{r_{b,t}}]`$ for the rank generating function at a cut. A stronger consequence keeps the transition before Jensen:

```math
M_{e^\lambda}'\le M_{\sqrt{1-q+qe^{2\lambda}}},\qquad
\phi_j(\lambda)=\frac12\ln\bigl(1+q^j(e^{2\lambda}-1)\bigr).
```

The complete branch profile gives $`p\le e^{-kA(\lambda)}M_{e^\lambda}`$ for every $`\lambda\ge0`$, where

```math
A(\lambda)=\min\{2\lambda,(\ln2+5\lambda)/6,\ln2\}.
```

At the $`D`$ backward cuts immediately after noise, each prescribed gate has distinct positive noise ages. For $`1\le L\le D`$ and $`T=D-L+1`$, summing the logarithmic moment bounds gives

```math
\frac{-\ln p}{k}\ge
\left[A(\lambda)-
\frac{2n\sum_{d=L}^{D}\phi_d(\lambda)
+m_T\sum_{j=1}^{T}\phi_j(\lambda)}{kT}\right]_+.
```

This retains the initial width and is valid for every fixed gate schedule. Under the same fixed-$`q`$ growing-family hypotheses, choosing $`L=o(D)`$ to dissipate that allowance yields

```math
\liminf\frac{-\ln p}{k}\ge\mathcal E_q(\rho),
\qquad
\mathcal E_q(\rho)=\sup_{0\le\lambda\le\ln2}
\left[A(\lambda)-\rho\sum_{j\ge1}\phi_j(\lambda)\right]_+.
```

The infinite sum converges geometrically. This exponent is positive exactly below $`2(1-q)/q`$ and strictly improves $`E_q`$ throughout that subcritical range. In particular $`\mathcal E_q(0)=\ln2`$, the chance-level exponent, instead of $`E_q(0)=2\ln2/7`$. Finite sums with rigorous tail bounds provide certified optimization. The companion's [complete proof and certificates](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/afba6ae9315ac415189d972fa604658168e5524b/science/guessing_decay.md) own this refinement. Its critical rate remains a necessary threshold; physical achievability is not established.

## Survival of the envelope gives a reliability-dependent budget

A fixed nonchance score also constrains how often the sampled channel may lose **all** input dependence. This gives a different bound from the mean-rank and exponential-moment floors above. The companion owns the [complete extinction and processing proof](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/afba6ae9315ac415189d972fa604658168e5524b/science/reliability_processing.md); the score-based consequence is stated and derived here.

Keep the same full physical output before basis-dependent readout, the same independent identity/replacement noise coupling, and the same counted fixed Clifford+T/reset circuit. For $`D\ge1`$ and an unconditional score $`2^{-k}\lt p\lt1`$, define

```math
\delta_p=\frac{1-p}{1-2^{-k}},\qquad
b_p=1-\delta_p=\frac{p-2^{-k}}{1-2^{-k}}.
```

Both numbers lie strictly between zero and one. Then

```math
m_T\ge\left\lceil
\left[
\frac{\gamma D b_p}{\ln(1/\gamma)}
\left[\ln\frac{D b_p}{\delta_p}\right]_+
-2n
\right]_+\right\rceil.
\qquad\text{(R1)}
```

This necessary condition may be combined with every earlier valid ledger. It retains a finite initial-width allowance, rather than assuming the width can be held fixed indefinitely. At $`p=1`$, any positive number of noise rounds and finite width are incompatible with the model: complete replacement of every physical slot has positive probability and leaves only chance success. At or below chance, this argument imposes no positive processing requirement.

### Why the same physical score controls extinction

Choose the envelope updates so that the zero space is absorbing. Clifford operations and resets already have this property. At a T/T-dagger slot, keep $`V`$ unchanged when all labels commute with its Pauli axis; otherwise use $`V+\langle w\rangle`$. In particular, a zero envelope stays zero, while every slot still increases rank by at most one. Merely adding the gate axis at every slot would introduce an artificial resurrection and would not justify this argument.

An incoming rank-$`r`$ space has $`r`$ binary coordinate pivots whose restriction is injective. They occupy at most $`r`$ physical qubits. If all those qubits are replaced in the next noise layer, the surviving subspace is zero. Conditional on the sampled suffix, the current noise choices are independent, so the conditional extinction probability is at least $`\gamma^r`$. These choices are mathematical variables, not flags supplied to the controller.

A branch with zero envelope represents a CPTP tail whose full output is independent of the input. No basis-dependent endpoint readout can then correlate its guess with the uniformly hidden $`X`$. Its exact-string score is at most $`2^{-k}`$; aborts can only reduce it. If $`e`$ is the probability of eventual extinction, unconditional averaging gives

```math
p\le 2^{-k}e+(1-e),\qquad e\le\delta_p.
\qquad\text{(R2)}
```

Let $`r_j`$ be the envelope rank immediately before the $`j`$th backward noise layer, and let $`S_j`$ indicate that it is nonzero. First extinction at different noise layers is disjoint; a reset that extinguishes the envelope only consumes more of the same probability budget. Therefore

```math
\sum_{j=1}^{D}\mathbb E[S_j\gamma^{r_j}]\le\delta_p,
\qquad
A:=\sum_{j=1}^{D}\Pr[S_j=1]\ge D b_p.
\qquad\text{(R3)}
```

Apply Jensen's inequality to $`e^{-r\ln(1/\gamma)}`$ with the alive cut-time weights of total mass $`A`$. Since $`r_j=0`$ when $`S_j=0`$, this yields

```math
\sum_{j=1}^{D}\mathbb E[r_j]
\ge \frac{A}{\ln(1/\gamma)}\left[\ln\frac{A}{\delta_p}\right]_+
\ge \frac{D b_p}{\ln(1/\gamma)}
\left[\ln\frac{D b_p}{\delta_p}\right]_+.
\qquad\text{(R4)}
```

For the final inequality use nonnegativity when $`D b_p\le\delta_p`$; otherwise $`A\ln(A/\delta_p)`$ is increasing for $`A\ge D b_p>\delta_p`$. The expected-rank decrease at noise layer $`j`$ is at least $`\gamma\mathbb E[r_j]`$. Free primitives do not increase rank and all T/T-dagger increases sum to at most $`m_T`$. Telescoping from terminal rank $`2n`$ gives

```math
m_T\ge\gamma\sum_{j=1}^{D}\mathbb E[r_j]-2n.
\qquad\text{(R5)}
```

Equations (R4) and (R5) prove (R1). No independent controller record, postselection or branch-dependent physical gate choice is introduced.

The same global score gives a bound inside every contiguous interval with $`D_I\ge1`$ noise layers. Let $`M_I`$ be a proved bound on the expected rank of the actual globally propagated suffix envelope entering that interval in backward order. Then

```math
m_{T,I}\ge\left\lceil\left[
\frac{\gamma D_I b_p}{\ln(1/\gamma)}
\left[\ln\frac{D_I b_p}{\delta_p}\right]_+-M_I
\right]_+\right\rceil.
\qquad\text{(R6)}
```

Always $`M_I=2n`$ is safe. Do not restart a newly chosen envelope at the interval boundary. Global extinction still bounds the zero probability at every cut, and first-extinction events within this interval have total probability at most $`\delta_p`$. Thus the same hazard/Jensen argument uses $`D_I`$ layers, while its cumulative-rank balance subtracts $`M_I`$. Gates on interval boundaries are assigned once to the selected primitive cuts. When $`D_I=0`$, this theorem adds only a nonnegative count.

For fixed $`k`$, fixed $`\gamma>0`$ and fixed $`p>2^{-k}`$, widths $`n=O(\ln D)`$ therefore require $`m_T=\Omega(D\ln D)`$ as $`D\to\infty`$. This strengthens the continuing-processing inference for small challenges. In the companion's construction range $`0<\gamma\le1/20`$, its reference-stable Tanner construction has the same processing order at that width for a fixed error target. This is a fixed-noise order statement; the factor $`1/\ln(1/\gamma)`$ prevents a claim of uniform weak-noise sharpness.

The use of first extinction and Jensen is a rank-dependent adaptation of the established complete-erasure/spacetime argument of [Bharti, Haug and Tanggara](https://arxiv.org/abs/2608.26272). The additional step tracks the backward Pauli-envelope rank rather than all live physical qubits and converts its cumulative contraction into the specifically charged T count while Clifford/reset processing remains free. It is not the first reliability logarithm in a quantum-memory resource law.

## A matching-order coherent construction in the companion model

The companion [Tanner construction](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/afba6ae9315ac415189d972fa604658168e5524b/science/tanner_memory.md) compiles an inherited constant-iteration current-syndrome decoder into a fixed coherent circuit. Syndrome and scratch registers remain in the counted noisy pool and are reset before each ideal recovery; nonlinear decisions are implemented and charged. A fixed-level five-qubit inner code extends its physical-noise range to $`0\lt\gamma\le1/20`$. With this inner code it proves

```math
n=O\!\left(k+\ln\frac{J_+}{\epsilon}\right),\qquad
m_T=O(nJ),\qquad J=O(\gamma D+1).
```

```math
\frac12\|\Lambda-\mathrm{id}\|_\diamond\le\epsilon,
\qquad J_+=\max\{1,J\}.
```

Here $`n`$ includes the Tanner data block and all controller/workspace qubits. The endpoint decoder is free, fixed and reference-safe. Independent spatial depolarization gives separate marginal tails for $`X`$ and $`Z`$ components; a union bound handles their correlation. When $`k=\Omega(\ln(J_+/\epsilon))`$ and duration is long enough for the earlier converse width allowance, the construction has $`n=O(k)`$ and $`m_T=O(k\gamma D)`$. The extinction-based fidelity converse in the companion extends the fixed-noise matching order to every payload scaling: for fixed $`0<\gamma\le1/20`$, errors $`0<\epsilon\le\epsilon_0<1/2`$ and a width allowance $`n\le C[k+\ln(D/\epsilon)]`$, sufficiently long storage requires $`\Omega_\gamma(D[k+\ln(D/\epsilon)])`$ T slots. A sufficiently large constant width factor permits the Tanner construction to achieve the same order. This statement restricts the width class; it does not optimize over arbitrarily large memories. The inner concatenation level depends only on the fixed Tanner family, so its width and prescribed gate overhead remain constant in $`k,D,\epsilon,\gamma`$ throughout that range. Existing outer residual Paulis leave the inner syndrome unchanged; fresh logical errors remain independent across inner blocks, while their X/Z components may be correlated. Its constants may be extremely large and grow further with the inner code. It changes no quantum-memory guessing exponent and supplies no cryptographic preparation compilation or hardware gate-time theorem.

## Boundaries and ownership

Discarding the input and guessing uniformly achieves $`p=2^{-k}`$ with zero interior processing for every $`D`$. No positive charge follows at or below that baseline. At fixed finite width there is also an absolute ceiling, regardless of gate supply:

```math
p\leq2^{-k}+(1-2^{-k})(1-\gamma^n)^D.
```

A complete replacement of all $`n`$ registers in any round destroys all input dependence. The continuing-charge result therefore concerns feasible parameter families and does not guarantee indefinite constant-score storage at fixed width. Its information-bearing algebra can include classical records; an above-random score alone is not a demonstration of quantum storage.

The guessing score does not verify the noise strength or independence, counted-controller restrictions, fixed primitive schedule or absence of side channels. Those remain model premises. It supplies no automatic LWE or remote-preparation compilation: such a reduction would have to preserve the joint state, chronology, controller model and charged resources separately. Statistical estimation of the unconditional score is also separate from the inference made here.

Lattice owns the [finite guessing theorem](guessing-bound.md). Measurement-Free owns the envelope contraction, gate ledger and [full dynamical composition proof](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/afba6ae9315ac415189d972fa604658168e5524b/science/guessing_processing.md). The CPTP compatibility and score-based composition form their shared corollary; the recovery reductions remain attributed to the prior sources. The sister relationship does not merge the projects or alter their distinct ideal and noisy models.
