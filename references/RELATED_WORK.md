# Attribution and closest-work comparison

This literature comparison records the original source inspections made on **2026-10-23** and the noisy-processing recovery comparison checked on **2026-11-04**. The [bibliography](references.bib) supplies stable identifiers; the [scientific account](../science/README.md) states the exact models, claims and proofs.

## BK02: discrimination

H. Barnum and E. Knill, *Reversing quantum dynamics with near-optimal quantum and classical fidelity*, Journal of Mathematical Physics **43**, 2097–2106 (2002), [DOI](https://doi.org/10.1063/1.1459754), [arXiv](https://arxiv.org/abs/quant-ph/0004088).

The discrimination inequality $`P_{\mathrm{opt}}^2\leq P_{\mathrm{pgm}}`$ is inherited. The inspected arXiv version is v2, dated 2026-01-18, which records a correction to the original main-theorem proof for ensembles of multiple density matrices. [Lemma D](../science/guessing-bound.md) proves the required finite-ensemble inequality directly by Cauchy–Schwarz, with the support and probability conventions used in this project.

## M12: hypercontractivity

A. Montanaro, *Some applications of hypercontractive inequalities in quantum information theory*, Journal of Mathematical Physics **53**, 122206 (2012), [arXiv:1208.0161](https://arxiv.org/abs/1208.0161). Theorem 13 on printed page 10 explicitly uses normalized Schatten norms and tensor powers of qubit depolarization. The proof here uses only its $`p=3/2`$, $`q=2`$, $`\eta=1/\sqrt2`$ instance.

The convention is the normalized Schatten norm

```math
\lVert A\rVert_{p,\mathrm{n}}
=\left(2^{-n}\mathrm{Tr}|A|^p\right)^{1/p}
```

for an operator on $`n`$ qubits and $`p\geq1`$. The roman $`\mathrm{n}`$ marks normalization; traces outside these norms are ordinary traces. Applying the theorem to $`\sqrt\rho`$ at $`p=3/2`$ and $`q=2`$ preserves the dimension factor needed for the storage-deficit estimate.

Montanaro attributes the qubit theorem to A. Montanaro and T. J. Osborne, *Quantum boolean functions*, Chicago Journal of Theoretical Computer Science, 2010, no. 1, [arXiv:0810.2435v5](https://arxiv.org/abs/0810.2435v5). The local argument combines this imported theorem with classical pure-state refinement, its Schmidt-rank bound and the BB84 quadratic-form comparison.

## DFW15: finite comparison

F. Dupuis, O. Fawzi and S. Wehner, *Entanglement sampling and applications*, IEEE Transactions on Information Theory **61**, 1093–1112 (2015), [arXiv:1305.1316](https://arxiv.org/abs/1305.1316). The inspected full-text PDF contains Theorem 10 and Corollary 11 on printed pages 17–19. Their high-order uncertainty relation already allows bounded quantum storage rates approaching one. Rate-one feasibility is therefore not a new claim of this project.

For retained dimension $`D\leq2^m`$, the dimension-only substitution $`H_{\min}(A\mid CQ)\geq-\log_2D\geq-m`$ in Corollary 11 gives

```math
H_{\min}(X\mid CQ\Theta)
\geq\frac{n\gamma(-m/n)-1}{2}.
```

For the arguments used here, $`\gamma(u)`$ is the inverse of $`g(a)=h_2(a)+a-1`$ on $`0\leq a\leq1/2`$, with $`h_2`$ binary entropy. Set $`t=n-m`$. Then

```math
h_2\big(\gamma(-1+t/n)\big)+\gamma(-1+t/n)=t/n.
```

To make the displayed entropy bound at least $`\log_2(1/\delta)`$ for an ideal exact-string target $`0<\delta<1`$, set

```math
a_*=\frac{1+2\log_2(1/\delta)}{n}.
```

When $`a_*\leq1/2`$ and the resulting gap is feasible, the sufficient integer gap from that displayed bound is

```math
t_{\mathrm{DFW}}=
\left\lceil n\big(h_2(a_*)+a_*\big)\right\rceil.
```

At fixed $`\delta`$, this particular sufficient gap grows logarithmically with $`n`$, whereas the present sufficient gap $`\lceil6\log_2(1/\delta)\rceil`$ is independent of block length. The [finite comparison table](../science/lower-bounds-and-resources.md) evaluates the two formulas, and the [analytic figure](../verification/Graph/README.md) displays the achieved strategy and present universal bound. The comparison fixes the dimension-only specialization and unsmoothed exact-string target; additional state information, smoothing and other cryptographic error notions lead to different comparisons.

## Recovery comparison for the noisy-processing application

The [noisy-device application](../science/noisy-processing.md) uses a different premise from an ideal dimension bound: a fixed storage circuit with independent depolarization, noisy counted persistent controllers, charged interior primitives and arbitrary free endpoint decoding. Its dynamical envelope proof and gate ledger have their authoritative home in [Measurement-Free-Memory-Cost, *Delayed-basis guessing and continuing processing*](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/87296f795359b0b66e0c49d20555634fd0d3d3ae/science/guessing_processing.md). Lattice contributes its finite BB84 guessing theorem. Their CPTP compatibility and composition are a shared corollary, with independent source ownership retained.

The strongest checked recovery comparison includes DFW15's finite threshold estimate, Eq. (27), and its Appendix C operational interpretation, rather than using only the dimension substitution from the preceding section. In the noisy application's notation, let $`d=2^k`$, let $`u`$ be basis-averaged pretty-good guessing success, and let $`F_{\mathrm{pg}}`$ be squared pretty-good Bell recovery fidelity. With $`S_\ell=\sum_{j=0}^{\ell}\binom kj`$, the estimate reads

```math
u\leq S_\ell F_{\mathrm{pg}}
+2^{-\ell-1}\mathbf1_{\ell\lt k},
\qquad0\leq\ell\leq k.
```

Joseph M. Renes, *Better bounds on optimal measurement and entanglement recovery, with applications to uncertainty and monogamy relations*, Physical Review A **96**, 042328 (2017), [DOI](https://doi.org/10.1103/PhysRevA.96.042328), [arXiv:1707.01114](https://arxiv.org/abs/1707.01114), Eq. (12), gives $`p^2+(1-p)^2/(d-1)\leq u`$ for optimal guessing success $`p`$. Together these imply useful recovery-fidelity bounds at and below score one half. The elementary measure-and-prepare decoder additionally gives $`F_{\mathrm{rec}}\geq p/d`$, exceeding replacement fidelity for every above-random score.

Mario Berta, Patrick J. Coles and Stephanie Wehner, *Entanglement-assisted guessing of complementary measurement outcomes*, Physical Review A **90**, 062127 (2014), [DOI](https://doi.org/10.1103/PhysRevA.90.062127), [arXiv:1302.5902v2](https://arxiv.org/abs/1302.5902v2), Eqs. (14), (15) and Appendix B Eq. (B23), supply an additional complementary-pair pretty-good recovery bound. Each product basis and its bitwise complementary basis form a mutually unbiased pair that extends to a complete stabilizer MUB set. The complete-MUB identity can be used on those pairs; the entire product-BB84 collection is not itself a complete MUB set or a 2-design.

Joseph M. Renes, *Uncertainty relations and approximate quantum error correction*, Physical Review A **94**, 032314 (2016), [DOI](https://doi.org/10.1103/PhysRevA.94.032314), [arXiv:1605.01420v2](https://arxiv.org/abs/1605.01420v2), Eq. (3), gives another constructive complementary-observable recovery route. Using only an averaged pair score loses information and creates a high-score threshold; that threshold is not a limit of the stronger DFW-based comparison.

Apply the prior recovery inequalities to each CPTP future-noise branch before averaging. The companion superoperator-rank cap $`F_{\mathrm{rec},b}\leq\min\{1,2^{r-2k}\}`$ then yields the same straight-chord expected-rank floor as the direct quantum-plus-classical dimension argument for every $`k\geq9`$. The companion proof treats $`k\geq11`$ analytically and $`k=9,10`$ by exact rational finite certificates. Thus no additional asymptotic gate or contiguous-interval law is established by the operational transfer. Smaller-block differences concern the explicitly compared reduction family and do not establish optimality or an independent new contribution.

The comparison concerns unconditional exact whole-string success when the device receives only the quantum challenge and learns the basis after charged storage. It does not verify noise or controller assumptions and imports no remote-preparation or LWE wrapper.

## HMOY25 and Z25: classical preparation

M. Hhan, T. Morimae, Y. Okinaka and T. Yamakawa, *Proofs of Quantum Memory*, [arXiv:2510.04159v1](https://arxiv.org/html/2510.04159v1), 2025. The material directly used is Definition 2.8, Lemma 2.9, Theorem 4.3, and its Hybrid 0–2 proof. Their polynomial-hardness construction certifies an $`m`$-qubit threshold using $`\lceil9.1m\rceil`$ honest stored qubits, with inverse-polynomial soundness in its stated asymptotic regime. Their independent constant-round result uses stronger hardness and has a different tradeoff.

J. Zhang, *Formulations and Constructions of Remote State Preparation with Verifiability, with Applications*, ITCS 2025, LIPIcs **325**, 96:1–96:19, [primary proceedings source](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.96). This supplies background and underlying verifiable-preparation results. The exact compilation interface used here is the one formulated in HMOY25.

The finite ideal bound replaces the storage estimate inside their existing simulation reduction. For total soundness target $`0<\varepsilon<1`$ and preparation simulation error at most $`\varepsilon/2`$, the sufficient storage is

```math
n=m+\left\lceil6\log_2(2/\varepsilon)\right\rceil.
```

The [reduction](../science/cryptographic-certification.md) preserves pass weighting and the output-register dimension at the storage cut. Remote preparation, the wrapper and the hardness assumption remain inherited. The efficient guarantee uses the imported nonuniform quantum-polynomial-time convention and holds for sufficiently large security parameter, polynomial output length and inverse-polynomial simulation error. The algebraic storage formula alone supplies no stronger preparation guarantee.

## Scored discrimination

H. K. Mishra, L. Lami and M. M. Wilde, *Near-optimal performance of square-root measurement for general score functions and quantum ensembles*, [arXiv:2505.20447](https://arxiv.org/abs/2505.20447), 2025. This existing work extends the Barnum–Knill approach to general scoring. The present repository derives its required finite-list inequality directly and applies it to this memory test's error and erasure rules. The comparison here covers the abstract and bibliographic record, rather than a theorem-by-theorem analysis of the full general-score framework.

## Context and evidence boundary

P. J. Coles, M. Berta, M. Tomamichel and S. Wehner, *Entropic uncertainty relations and their applications*, Reviews of Modern Physics **89**, 015002 (2017), [DOI](https://doi.org/10.1103/RevModPhys.89.015002), [arXiv:1511.04857](https://arxiv.org/abs/1511.04857), reviews uncertainty with quantum memory and bounded-storage cryptography. It is a background review, not a substitute for the proof dependencies above.

The recorded comparison covers the closest identified BB84 uncertainty and LWE memory-verification statements, together with rank-, hypercontractivity-, and finite-memory-deficit variants. That search found no matching finite deficit-only theorem. It is a scoped source comparison, not an exhaustive classification of neighboring noisy-storage, non-local-game or scored-discrimination results. The contribution is the explicit finite theorem and its conditional certification corollary, with the imported ingredients identified above.

## Educational anchor: Watrous 2018

J. Watrous, *The Theory of Quantum Information*, Cambridge University Press (2018), [DOI](https://doi.org/10.1017/9781316848142), [author's book page](https://jhwatrous.github.io/books-and-courses.html). This is the project's single educational anchor. In particular, §3.1.2 and Theorem 3.10 give the discrimination inequality used as Lemma D; §1.1.3 supplies the Schmidt and operator-norm foundations. The [source bridge](../learning/WATROUS_BRIDGE.md) records selected sections, notation, version conventions and the ingredients supplied outside the book. The author copy and its errata were inspected for these pointers; the book itself is not redistributed.

