# Attribution and closest-work comparison

Source inspection date: **2026-10-23**. These are comparisons of particular statements and models, not an exhaustive priority certificate. The [bibliography](references.bib) supplies stable identifiers. The scientific claims are stated and proved under [science](../science/README.md).

## BK02: discrimination

H. Barnum and E. Knill, *Reversing quantum dynamics with near-optimal quantum and classical fidelity*, Journal of Mathematical Physics **43**, 2097–2106 (2002), [DOI](https://doi.org/10.1063/1.1459754), [arXiv](https://arxiv.org/abs/quant-ph/0004088).

The relation $P_{\mathrm{opt}}^2\leq P_{\mathrm{pgm}}$ is inherited. The current arXiv record is v2, dated 2026-01-18, and reports a correction to the original main-theorem proof for ensembles of multiple density matrices. Our [Lemma D](../science/guessing-bound.md) gives a direct finite-ensemble Cauchy–Schwarz proof of exactly the discrimination inequality needed here; it does not rely on an unchecked broader recovery statement from an older version.

## M12: hypercontractivity

A. Montanaro, *Some applications of hypercontractive inequalities in quantum information theory*, Journal of Mathematical Physics **53**, 122206 (2012), [arXiv:1208.0161](https://arxiv.org/abs/1208.0161). Theorem 13 on printed page 10 explicitly uses normalized Schatten norms and tensor powers of qubit depolarization. The proof here uses only its $p=3/2$, $q=2$, $\eta=1/\sqrt2$ instance.

That paper attributes the qubit theorem to A. Montanaro and T. J. Osborne, *Quantum boolean functions*, Chicago Journal of Theoretical Computer Science, 2010, no. 1, [arXiv:0810.2435v5](https://arxiv.org/abs/0810.2435v5). Hypercontractivity is an imported result. The local contribution is its use on $\sqrt\rho$ after the Schmidt-rank refinement and BB84 quadratic-form comparison. Finite matrix checks do not re-prove the imported theorem.

## DFW15: finite comparison

F. Dupuis, O. Fawzi and S. Wehner, *Entanglement sampling and applications*, IEEE Transactions on Information Theory **61**, 1093–1112 (2015), [arXiv:1305.1316](https://arxiv.org/abs/1305.1316). The inspected full-text PDF contains Theorem 10 and Corollary 11 on printed pages 17–19. Their high-order uncertainty relation already allows bounded quantum storage rates approaching one. Rate-one feasibility is therefore not a new claim of this project.

For the dimension-only substitution $H_{\min}(A\mid CQ)\geq-m$, Corollary 11 gives

```math
H_{\min}(X\mid CQ\Theta)
\geq\frac{n\gamma(-m/n)-1}{2}.
```

For the arguments used here, $\gamma(u)$ is the inverse of $g(a)=h_2(a)+a-1$ on $0\leq a\leq1/2$, with $h_2$ binary entropy. Set $t=n-m$. Then

```math
h_2\big(\gamma(-1+t/n)\big)+\gamma(-1+t/n)=t/n.
```

This specializes an existing inequality; it is not a new entropy theorem. The following algebra makes its finite overhead explicit. To obtain ideal success at most $\delta$, set

```math
a_*=\frac{1+2\log_2(1/\delta)}{n}.
```

When $a_*\leq1/2$ and the resulting gap is feasible, the sufficient integer gap from that displayed bound is

```math
t_{\mathrm{DFW}}=
\left\lceil n\big(h_2(a_*)+a_*\big)\right\rceil.
```

At fixed $\delta$ this specialization grows logarithmically with $n$, whereas the new bound's sufficient gap $\lceil6\log_2(1/\delta)\rceil$ does not. The [finite comparison table](../science/lower-bounds-and-resources.md) evaluates this formula. It does **not** establish that every conceivable use of their framework is weaker, nor that the new bound is uniformly stronger at every memory rate. Smoothed entropy guarantees for different cryptographic tasks are not being equated to unsmoothed exact-string guessing.

## HMOY25 and Z25: classical preparation

M. Hhan, T. Morimae, Y. Okinaka and T. Yamakawa, *Proofs of Quantum Memory*, [arXiv:2510.04159v1](https://arxiv.org/html/2510.04159v1), 2025. The material directly used is Definition 2.8, Lemma 2.9, Theorem 4.3, and its Hybrid 0–2 proof. Their polynomial-hardness construction certifies an $m$-qubit threshold using $\lceil9.1m\rceil$ honest stored qubits, with inverse-polynomial soundness in its stated asymptotic regime. Their independent constant-round result uses stronger hardness and has a different tradeoff.

J. Zhang, *Formulations and Constructions of Remote State Preparation with Verifiability, with Applications*, ITCS 2025, LIPIcs **325**, 96:1–96:19, [primary proceedings source](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.96). This supplies background and underlying verifiable-preparation results. The exact compilation interface used here is the one formulated in HMOY25.

The local addition is the proved finite ideal bound and its parameter substitution in the existing simulation reduction. Neither remote state preparation nor the classical-verifier wrapper is claimed as new. The quantum-hardness assumption, polynomial-round guarantee, and supported simulation-error regime are inherited. The [reduction](../science/cryptographic-certification.md) explicitly preserves pass weighting and the dimension at the storage cut.

## Scored discrimination

H. K. Mishra, L. Lami and M. M. Wilde, *Near-optimal performance of square-root measurement for general score functions and quantum ensembles*, [arXiv:2505.20447](https://arxiv.org/abs/2505.20447), 2025. Its stated scope extends the Barnum–Knill approach to more general scoring. We do not claim the broad idea of scored square-root-measurement bounds as new. The repository proves its required finite-list inequality directly and uses it to quantify this particular memory test's error and erasure boundaries. The abstract and bibliographic record were checked; no claim of theorem-by-theorem comparison with its full general-score framework is made.

## Context and evidence boundary

P. J. Coles, M. Berta, M. Tomamichel and S. Wehner, *Entropic uncertainty relations and their applications*, Reviews of Modern Physics **89**, 015002 (2017), [DOI](https://doi.org/10.1103/RevModPhys.89.015002), [arXiv:1511.04857](https://arxiv.org/abs/1511.04857), reviews uncertainty with quantum memory and bounded-storage cryptography. It is a background review, not a substitute for the proof dependencies above.

The comparison checks the closest identified BB84 uncertainty and LWE memory-verification statements and searches for rank-, hypercontractivity-, and finite-memory-deficit variants. No matching finite deficit-only theorem was located in that search. This observation is not proof of priority. The full generality of all neighboring noisy-storage, non-local-game, or scored-discrimination results has not been exhaustively classified. The present research claim is the explicit theorem and the conditional corollary as written, with imported ingredients credited.
