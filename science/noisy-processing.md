# Delayed-basis guessing and continuing noisy-memory processing

[Science guide](README.md) · [Finite guessing theorem](guessing-bound.md) · [Authoritative dynamical proof](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/a7d29a5c6e18e0dc363b62227591274dd43296f3/science/guessing_processing.md)

Unconditional whole-string BB84 guessing success implies a continuing processing budget in a specified noisy-memory model. The finite guessing theorem supplies an information bottleneck; the Pauli-envelope contraction and processing ledger belong to [Measurement-Free-Memory-Cost](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost). This chapter states their composition and its operational limits. The prior recovery route already implies both score-dependent rank floors stated below. The composition provides an operational proof of the processing implication, with no additional gate or interval consequence from those floors.

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

These floors are positive for every score above random guessing, including scores at or below one half. The averaging concerns expected rank; it does not require every noise branch to retain that rank. The curves are necessary upper bounds, not claims of optimal attainable guessing. The [companion proof](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/a7d29a5c6e18e0dc363b62227591274dd43296f3/science/guessing_processing.md) supplies the envelope coupling, chord argument and finite checks.

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

Indeed, DFW's normalized spectral weights satisfy $`w_v\geq0`$, $`\sum_vw_v=1`$ and $`w_v\leq F_{\mathrm{pg}}`$. The BB84 spectrum has coefficient $`2^{-j}`$ on $`2^j\binom kj`$ Pauli labels of weight $`j`$, and zero on labels containing $`Y`$. Subtracting $`\tau_\ell\sum_vw_v`$, discarding nonpositive terms and bounding the remaining weights by $`F_{\mathrm{pg}}`$ yields the displayed coefficient $`A_\ell\leq S_\ell`$. The [companion comparison](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/a7d29a5c6e18e0dc363b62227591274dd43296f3/science/guessing_processing.md) gives the source equations and complete derivation.

Since $`F_{\mathrm{rec}}\geq F_{\mathrm{pg}}`$, this implies

```math
F_{\mathrm{rec}}\geq
\max_{0\leq\ell\leq k}
\frac{[g_d(p_*)-\tau_\ell]_+}{A_\ell}.
```

One may substitute any certified score $`p\geq1/d`$ because $`g_d`$ is increasing on that range. The bound remains useful at or below one half. A measure-and-prepare decoder also gives $`F_{\mathrm{rec}}\geq p_*/d`$, above replacement fidelity $`1/d^2`$ for every above-random score. The case $`\ell=0`$ gives the complementary-pair bound $`u\leq(1+F_{\mathrm{pg}})/2`$. It also follows from the Berta–Coles–Wehner complete-MUB identity applied separately to each complementary product stabilizer-basis pair. The entire product-BB84 collection is not itself a complete MUB set or a 2-design.

For each noise branch, every recovered logical CPTP channel factors through $`\mathcal E_V`$, so the companion channel-rank bound gives $`F_{\mathrm{rec},b}\leq\min\{1,2^{r-2k}\}`$. Applying the prior recovery reductions **branchwise before averaging** already yields (N2) for every $`k\geq8`$. The companion proves this analytically for $`k\geq11`$ and checks the remaining 54 integer ranks at $`k=8,9,10`$ with exact rational certificates. For $`1\leq k\leq7`$, the same spectral bounds imply the polygon floor (N3): 49 exact rational certificates cover the interior integer ranks, with the zero-rank and full-rank endpoints handled directly. The direct quantum-plus-classical factorization therefore adds no gate or interval consequence from either displayed floor, for any $`k\geq1`$. This comparison concerns (N2) and (N3); it does not assert that the recovery bounds dominate every possible refinement or determine optimal guessing.

## Boundaries and ownership

Discarding the input and guessing uniformly achieves $`p=2^{-k}`$ with zero interior processing for every $`D`$. No positive charge follows at or below that baseline. At fixed finite width there is also an absolute ceiling, regardless of gate supply:

```math
p\leq2^{-k}+(1-2^{-k})(1-\gamma^n)^D.
```

A complete replacement of all $`n`$ registers in any round destroys all input dependence. The continuing-charge result therefore concerns feasible parameter families and does not guarantee indefinite constant-score storage at fixed width. Its information-bearing algebra can include classical records; an above-random score alone is not a demonstration of quantum storage.

The guessing score does not verify the noise strength or independence, counted-controller restrictions, fixed primitive schedule or absence of side channels. Those remain model premises. It supplies no automatic LWE or remote-preparation compilation: such a reduction would have to preserve the joint state, chronology, controller model and charged resources separately. Statistical estimation of the unconditional score is also separate from the inference made here.

Lattice owns the [finite guessing theorem](guessing-bound.md). Measurement-Free owns the envelope contraction, gate ledger and [full dynamical composition proof](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/a7d29a5c6e18e0dc363b62227591274dd43296f3/science/guessing_processing.md). The CPTP compatibility and score-based composition form their shared corollary; the recovery reductions remain attributed to the prior sources. The sister relationship does not merge the projects or alter their distinct ideal and noisy models.
