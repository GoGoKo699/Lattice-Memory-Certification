# Attribution and closest-work comparison

This literature comparison records the original source inspections made on **2026-10-23** the noisy-processing recovery comparison checked on **2026-11-04**, and the rank-sensitive finite investigation checked on **2026-11-05**. The [bibliography](references.bib) supplies stable identifiers; the [scientific account](../science/README.md) states the exact models, claims and proofs.

## BK02: discrimination

H. Barnum and E. Knill, *Reversing quantum dynamics with near-optimal quantum and classical fidelity*, Journal of Mathematical Physics **43**, 2097–2106 (2002), [DOI](https://doi.org/10.1063/1.1459754), [arXiv](https://arxiv.org/abs/quant-ph/0004088).

The discrimination inequality $`P_{\mathrm{opt}}^2\leq P_{\mathrm{pgm}}`$ is inherited. The inspected arXiv version is v2, dated 2026-01-18, which records a correction to the original main-theorem proof for ensembles of multiple density matrices. [Lemma D](../science/guessing-bound.md) proves the required finite-ensemble inequality directly by Cauchy–Schwarz, with the support and probability conventions used in this project.

## M12: hypercontractivity

A. Montanaro, *Some applications of hypercontractive inequalities in quantum information theory*, Journal of Mathematical Physics **53**, 122206 (2012), [arXiv:1208.0161](https://arxiv.org/abs/1208.0161). Theorem 13 on printed page 10 explicitly uses normalized Schatten norms and tensor powers of qubit depolarization. The proof here uses only its $`p=3/2`$, $`q=2`$, $`\eta=1/\sqrt2`$ instance.

The convention is the normalized Schatten norm

```math
\lVert A\rVert_{p,\mathrm{n}}
=\left(2^{-k}\mathrm{Tr}|A|^p\right)^{1/p}
```

for an operator on $`k`$ qubits and $`p\geq1`$. The roman $`\mathrm{n}`$ marks normalization; traces outside these norms are ordinary traces. Applying the theorem to $`\sqrt\rho`$ at $`p=3/2`$ and $`q=2`$ preserves the dimension factor needed for the storage-deficit estimate.

Montanaro attributes the qubit theorem to A. Montanaro and T. J. Osborne, *Quantum boolean functions*, Chicago Journal of Theoretical Computer Science, 2010, no. 1, [arXiv:0810.2435v5](https://arxiv.org/abs/0810.2435v5). The local argument combines this imported theorem with classical pure-state refinement, its Schmidt-rank bound and the BB84 quadratic-form comparison.

## DFW15: finite comparison

F. Dupuis, O. Fawzi and S. Wehner, *Entanglement sampling and applications*, IEEE Transactions on Information Theory **61**, 1093–1112 (2015), [arXiv:1305.1316](https://arxiv.org/abs/1305.1316). The inspected full-text PDF contains Theorem 10 and Corollary 11 on printed pages 17–19. Their high-order uncertainty relation already allows bounded quantum storage rates approaching one. Rate-one feasibility is therefore not a new claim of this project.

For retained dimension $`d_Q\leq2^m`$, the dimension-only substitution $`H_{\min}(A\mid CQ)\geq-\log_2d_Q\geq-m`$ in Corollary 11 gives

```math
H_{\min}(X\mid CQ\Theta)
\geq\frac{k\gamma(-m/k)-1}{2}.
```

For the arguments used here, $`\gamma(u)`$ is the inverse of $`g(a)=h_2(a)+a-1`$ on $`0\leq a\leq1/2`$, with $`h_2`$ binary entropy. Set $`t=k-m`$. Then

```math
h_2\big(\gamma(-1+t/k)\big)+\gamma(-1+t/k)=t/k.
```

To make the displayed entropy bound at least $`\log_2(1/\delta)`$ for an ideal exact-string target $`0\lt \delta\lt 1`$, set

```math
a_*=\frac{1+2\log_2(1/\delta)}{k}.
```

When $`a_*\leq1/2`$ and the resulting gap is feasible, the sufficient integer gap from that displayed bound is

```math
t_{\mathrm{DFW}}=
\left\lceil k\big(h_2(a_*)+a_*\big)\right\rceil.
```

At fixed $`\delta`$, this particular sufficient gap grows logarithmically with $`k`$, whereas the present sufficient gap $`\lceil6\log_2(1/\delta)\rceil`$ is independent of block length. The [finite comparison table](../science/lower-bounds-and-resources.md) evaluates the two formulas, and the [analytic figure](../verification/Graph/README.md) displays the achieved strategy and present universal bound. The comparison fixes the dimension-only specialization and unsmoothed exact-string target; additional state information, smoothing and other cryptographic error notions lead to different comparisons.

## Rank-sensitive small-challenge refinements

The [three-input theorem](../science/finite-guessing.md) concerns three independently based BB84 inputs, quantum memory dimension two, unrestricted classical records, and arbitrary joint encoding and basis-dependent POVMs. The inherited normalized DFW spectral constraints give basis-averaged PGM success at most $`5/8`$. Renes (2017), Eq. (12), then gives $`P^*_{3,1}\leq(1+2\sqrt7)/8\simeq0.7864378278`$.

A two-copy linear-entropy constraint strengthens the PGM value to the tight $`9/16`$, giving the certified upper bound $`(2+7\sqrt2)/16\simeq0.7437184335`$. Store-and-Breidbart achieves $`(3+2\sqrt2)/8\simeq0.7285533906`$. The finite-alphabet discrimination inequality is inherited and allows nonuniform priors. Linear-entropy subadditivity is an established tool, with a self-contained positive swap-operator certificate supplied in the proof. The addition is its explicit rank-sensitive evaluation and compatible finite moment composition, rather than a new discrimination theorem.

For four and five inputs with one retained qubit, positive local-swap sectors give exact maximal averaged PGM scores $`27/64`$ and $`81/256`$. The same Renes conversion yields guessing caps $`(2+\sqrt{345})/32`$ and $`(4+\sqrt{4526})/128`$. Hypercontractivity followed by that conversion gives approximately $`0.702934`$ and $`0.626376`$, compared with the improved $`0.642943`$ and $`0.556840`$. The certificates attain their PGM bounds on a stored qubit and real product pure factors; they do not establish optimal guessing or tensorization. The four-input cap also improves a specified finite noisy-envelope profile.

Local-swap positivity and its weight-enumerator interpretation are established machinery. E. M. Rains, *Quantum shadow enumerators*, [quant-ph/9611001v2](https://arxiv.org/html/quant-ph/9611001v2), Corollary 7 and Theorem 8, prove positivity and the enumerator transform for arbitrary positive operators. F. Shi, K. Guo, X. Zhang and Q. Zhao, *Exploring Quantum Weight Enumerators From the k-Qubit Parallelized SWAP Test*, [arXiv:2406.18280v2](https://arxiv.org/html/2406.18280v2), Proposition 6 and Theorem 8, identify the local-SWAP outcome probabilities. d_Q. Miller et al., *Experimental measurement and a physical interpretation of quantum shadow enumerators*, [arXiv:2408.16914v2](https://arxiv.org/pdf/2408.16914v2), Theorem 3, give the related two-copy Bell-sampling interpretation.

In Rains's unnormalized convention, $`A_j=A_j(R,R)`$ and $`S_{k-h}(R,R)=2^k\mathrm{Tr}[(R\otimes R)E_h]`$. Thus the [finite proof](../science/finite-guessing.md) uses $`H_4=8S_2`$, $`H_{52}=16S_3`$ and $`H_{55}=32S_0`$. Its additions are the explicit sharp BB84 rank-two evaluations and their operational consequences, not a new general positivity, shadow transform or discrimination theorem. The bounded comparison did not identify these numerical BB84 evaluations in the cited sources; it does not establish exhaustive publication priority.

The arbitrary-state/premeasurement optimum equals the original preparation optimum by a flagged Pauli-twirl Choi construction. This does not prove attainability of the guessing upper bounds. The bounded prior audit covered DFW, Renes, and [Tomamichel–Fehr–Kaniewski–Wehner's BB84 monogamy theorem](https://arxiv.org/abs/1210.4359); the latter is a two-recipient problem, and its dimension-lifting bound is weaker in the three-input instance. No stronger applicable three-input/qubit bound was identified within that audit; no exhaustive priority claim is made.

The finite result does not improve the universal $`1/6`$ exponent. A Breidbart-diagonal Hamming-ball construction proves that no universal PGM rank power above $`1/3`$ is possible, even with a fixed multiplicative constant. The elementary type proof and its power-of-two dimension rounding are in the finite chapter. This is an obstruction to a collision-only argument followed by the generic square-root or Renes conversion. It does not rule out a stronger joint-discrimination argument or establish the optimal guessing exponent.

## Direct discrimination beyond collision bounds

The [direct-discrimination investigation](../science/direct-discrimination.md) uses the standard minimum-error state-discrimination primal/dual SDP, as developed in the selected Watrous source. For a fixed encoder, a feasible decoder POVM lower-bounds its optimal score and a dual matrix dominating every conditional state upper-bounds it. These are inherited convex-optimization tools. They do not jointly optimize the encoder, and see-saw convergence supplies no universal certificate.

For Breidbart-diagonal projector encoders, all product-BB84 basis ensembles are unitarily equivalent. Exact finite certificates enclose the optimal decoder for Hamming radius-one projectors with three inputs/rank four and seven inputs/rank eight. Both specified encoders perform worse than store-and-Breidbart at the same retained dimension. The finite certificates establish those encoder-specific facts, without improving the global three-input/one-qubit bound.

The additional all-size limitation concerns the Breidbart-diagonal dual ansatz. For the large Hamming balls used in the earlier collision obstruction, its best trace cannot decay fast enough to reproduce even the established universal score bound. Thus restricting the dual to that diagonal algebra loses essential discrimination information. Off-diagonal dual entries are required for a competitive certificate along this route. This is an analytic limitation of a specified ansatz, rather than a stronger uncertainty theorem, an optimal-exponent claim or an exhaustive obstruction to direct discrimination.

## Recovery comparison for the noisy-processing application

The [noisy-device application](../science/noisy-processing.md) uses a different premise from an ideal dimension bound: a fixed storage circuit with independent depolarization, noisy counted persistent controllers, charged interior primitives and arbitrary free endpoint decoding. Its dynamical envelope proof and gate ledger have their authoritative home in [Measurement-Free-Memory-Cost, *Delayed-basis guessing and continuing processing*](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/4b5ae9a75658bc44106b07fbb6deb2330e806df8/science/guessing_processing.md). Lattice contributes its finite BB84 guessing theorem. Their CPTP compatibility and composition are a shared corollary, with independent source ownership retained.

The recovery comparison uses DFW15's spectral constraints, Eqs. (13)–(15), and Appendix C's operational interpretation. In the noisy application's notation, let $`d=2^k`$, let $`u`$ be basis-averaged pretty-good guessing success, and let $`F_{\mathrm{pg}}`$ be squared pretty-good Bell recovery fidelity. Keeping the normalized spectral weights gives

```math
\begin{aligned}
u&\leq\tau_\ell+A_\ell F_{\mathrm{pg}},\\
\tau_\ell&=2^{-\ell-1}\mathbf1_{\ell\lt k},\\
A_\ell&=\sum_{j=0}^{\ell}\binom kj(1-2^j\tau_\ell),
\qquad0\leq\ell\leq k.
\end{aligned}
```

This follows by subtracting $`\tau_\ell`$ from the spectral average and bounding only positive residual coefficients; the [application](../science/noisy-processing.md#existing-recovery-reductions-already-cover-low-scores) explains the step. Since $`A_\ell\leq\sum_{j=0}^{\ell}\binom kj`$, it strengthens the coarser threshold estimate printed as DFW15 Eq. (27). The refinement uses the cited spectral constraints and does not posit an additional uncertainty relation.

Joseph M. Renes, *Better bounds on optimal measurement and entanglement recovery, with applications to uncertainty and monogamy relations*, Physical Review A **96**, 042328 (2017), [DOI](https://doi.org/10.1103/PhysRevA.96.042328), [arXiv:1707.01114](https://arxiv.org/abs/1707.01114), Eq. (12), gives $`p^2+(1-p)^2/(d-1)\leq u`$ for optimal guessing success $`p`$. Together these imply useful recovery-fidelity bounds at and below score one half. The elementary measure-and-prepare decoder additionally gives $`F_{\mathrm{rec}}\geq p/d`$, exceeding replacement fidelity for every above-random score.

Mario Berta, Patrick J. Coles and Stephanie Wehner, *Entanglement-assisted guessing of complementary measurement outcomes*, Physical Review A **90**, 062127 (2014), [DOI](https://doi.org/10.1103/PhysRevA.90.062127), [arXiv:1302.5902v2](https://arxiv.org/abs/1302.5902v2), Eqs. (14), (15) and Appendix B Eq. (B23), supply an additional complementary-pair pretty-good recovery bound. Each product basis and its bitwise complementary basis form a mutually unbiased pair that extends to a complete stabilizer MUB set. The complete-MUB identity can be used on those pairs; the entire product-BB84 collection is not itself a complete MUB set or a 2-design.

Joseph M. Renes, *Uncertainty relations and approximate quantum error correction*, Physical Review A **94**, 032314 (2016), [DOI](https://doi.org/10.1103/PhysRevA.94.032314), [arXiv:1605.01420v2](https://arxiv.org/abs/1605.01420v2), Eq. (3), gives another constructive complementary-observable recovery route. Using only an averaged pair score loses information and creates a high-score threshold; that threshold is not a limit of the stronger DFW-based comparison.

Apply the prior recovery inequalities to each CPTP future-noise branch before averaging. The companion superoperator-rank cap $`F_{\mathrm{rec},b}\leq\min\{1,2^{r-2k}\}`$ then yields the same straight-chord expected-rank floor as the direct quantum-plus-classical dimension argument for every $`k\geq8`$. The companion proof treats $`k\geq11`$ analytically and all 54 remaining integer ranks at $`k=8,9,10`$ by exact rational certificates. For $`1\leq k\leq7`$, 49 additional exact rational certificates show that the same normalized spectral bounds imply the displayed polygon floor. Thus the recovery route already supplies the gate and contiguous-interval consequences of both convenient floors for every challenge length. This comparison concerns those mean-rank floors. The companion's [moment theorem](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/4b5ae9a75658bc44106b07fbb6deb2330e806df8/science/moment_processing.md) combines the same inherited recovery tools with the actual product-noise law: a pivot injection bounds exponential rank moments and Jensen yields a contracting logarithmic potential. Fixing one recovery of the averaged channel then provides its all-cut floor. This stronger dynamical consequence improves the fixed-score processing coefficient in long growing-block families, rather than claiming a new pointwise guessing inequality or optimal physical gate cost. The comparison does not assert dominance over all possible refined score bounds.

The comparison concerns unconditional exact whole-string success when the device receives only the quantum challenge and learns the basis after charged storage. It does not verify noise or controller assumptions and imports no remote-preparation or LWE wrapper.

## HMOY25 and Z25: classical preparation

M. Hhan, T. Morimae, Y. Okinaka and T. Yamakawa, *Proofs of Quantum Memory*, [arXiv:2510.04159v1](https://arxiv.org/html/2510.04159v1), 2025. The material directly used is Definition 2.8, Lemma 2.9, Theorem 4.3, and its Hybrid 0–2 proof. Their polynomial-hardness construction certifies an $`m`$-qubit threshold using $`\lceil9.1m\rceil`$ honest stored qubits, with inverse-polynomial soundness in its stated asymptotic regime. Their independent constant-round result uses stronger hardness and has a different tradeoff.

J. Zhang, *Formulations and Constructions of Remote State Preparation with Verifiability, with Applications*, ITCS 2025, LIPIcs **325**, 96:1–96:19, [primary proceedings source](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.96). This supplies background and underlying verifiable-preparation results. The exact compilation interface used here is the one formulated in HMOY25.

The finite ideal bound replaces the storage estimate inside their existing simulation reduction. For total soundness target $`0\lt \varepsilon\lt 1`$ and preparation simulation error at most $`\varepsilon/2`$, the sufficient storage is

```math
k=m+\left\lceil6\log_2(2/\varepsilon)\right\rceil.
```

The [reduction](../science/cryptographic-certification.md) preserves pass weighting and the output-register dimension at the storage cut. Remote preparation, the wrapper and the hardness assumption remain inherited. The efficient guarantee uses the imported nonuniform quantum-polynomial-time convention and holds for sufficiently large security parameter, polynomial output length and inverse-polynomial simulation error. The algebraic storage formula alone supplies no stronger preparation guarantee.

## Scored discrimination

H. K. Mishra, L. Lami and M. M. Wilde, *Near-optimal performance of square-root measurement for general score functions and quantum ensembles*, [arXiv:2505.20447](https://arxiv.org/abs/2505.20447), 2025. This existing work extends the Barnum–Knill approach to general scoring. The present repository derives its required finite-list inequality directly and applies it to this memory test's error and erasure rules. The comparison here covers the abstract and bibliographic record, rather than a theorem-by-theorem analysis of the full general-score framework.

## Context and evidence boundary

P. J. Coles, M. Berta, M. Tomamichel and S. Wehner, *Entropic uncertainty relations and their applications*, Reviews of Modern Physics **89**, 015002 (2017), [DOI](https://doi.org/10.1103/RevModPhys.89.015002), [arXiv:1511.04857](https://arxiv.org/abs/1511.04857), reviews uncertainty with quantum memory and bounded-storage cryptography. It is a background review, not a substitute for the proof dependencies above.

The recorded comparison covers the closest identified BB84 uncertainty and LWE memory-verification statements, together with rank-, hypercontractivity-, and finite-memory-deficit variants. That search found no matching finite deficit-only theorem. It is a scoped source comparison, not an exhaustive classification of neighboring noisy-storage, non-local-game or scored-discrimination results. The contribution is the explicit finite theorem and its conditional certification corollary, with the imported ingredients identified above.

## Educational anchor: Watrous 2018

J. Watrous, *The Theory of Quantum Information*, Cambridge University Press (2018), [DOI](https://doi.org/10.1017/9781316848142), [author's book page](https://jhwatrous.github.io/books-and-courses.html). This is the project's single educational anchor. In particular, §3.1.2 and Theorem 3.10 give the discrimination inequality used as Lemma D; §1.1.3 supplies the Schmidt and operator-norm foundations. The [source bridge](../learning/WATROUS_BRIDGE.md) records selected sections, notation, version conventions and the ingredients supplied outside the book. The author copy and its errata were inspected for these pointers; the book itself is not redistributed.



The companion's reliability-sensitive processing consequence adapts the complete-erasure/Jensen spacetime mechanism of Bharti, Haug and Tanggara, [arXiv:2608.26272v1](https://arxiv.org/abs/2608.26272), to absorbing backward Pauli rank and then to charged T/T-dagger slots. The additive reliability logarithm for physical-location cost is established prior work. The companion owns the rank-dependent conversion and fixed-noise processing comparison; the ideal BB84 guessing exponent and finite arbitrary-encoder bounds here are unchanged. A score above chance can witness continuing processing of noisy classical or quantum input dependence without by itself certifying quantum storage.
