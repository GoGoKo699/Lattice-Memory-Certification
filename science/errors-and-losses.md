# Errors, lists and losses

[Model](model.md) · [Exact proof](guessing-bound.md)

Exact-string recovery is consequential. This page proves a controlled extension rather than silently transferring its soundness to a different acceptance rule.

## 1. Lemma DL: list discrimination

Use the ensemble and notation of Lemma D. A POVM outcome $y$ specifies a list $\mathcal L_y$ of at most $L$ candidate labels. Define

```math
F_x=\sum_{y:x\in\mathcal L_y}M_y.
```

Then $0\leq F_x\leq I$ and $\sum_xF_x\leq L I$. With $A_x=S^{-1/4}\sigma_xS^{-1/4}$ as before, set $B_x=S^{1/4}F_xS^{1/4}$. Now $0\leq B_x\leq S^{1/2}$, so

```math
\sum_x\operatorname{Tr}B_x^2
\leq\sum_x\operatorname{Tr}(B_xS^{1/2})
=\operatorname{Tr}\left(S\sum_xF_x\right)\leq L.
```

Cauchy–Schwarz therefore yields

```math
P_{\mathrm{list}}^2\leq L P_{\mathrm{pgm}}.
```

Apply this to every basis and pure classical branch in the exact proof. Its same quadratic-form and hypercontractive bounds imply Theorem L:

```math
P_{\mathrm{list}}
\leq\min\{1,\sqrt L\,2^{-(n-m)/6}\}.
```

This is an elementary scored-discrimination extension. The broader literature on generalized square-root-measurement score bounds is credited in [related work](../references/RELATED_WORK.md#scored-discrimination); no general scored-measurement priority is claimed here.

## 2. Hamming errors

If acceptance allows at most $r$ wrong bits, each returned string defines a Hamming ball of size

```math
V(n,r)=\sum_{j=0}^{r}\binom nj.
```

Consequently the ideal cheating probability is at most

```math
\min\{1,\sqrt{V(n,r)}\,2^{-(n-m)/6}\}.
```

With an RSP error budget $\varepsilon/2$, the sufficient condition is

```math
n-m\geq3\log_2V(n,r)+6\log_2(2/\varepsilon).
```

This is a sufficient bound, not an optimal error-tolerant tradeoff. For $r\leq n/2$, $V(n,r)\leq2^{n h_2(r/n)}$ gives the convenient conservative condition $n-m\geq3n h_2(r/n)+6\log_2(2/\varepsilon)$. A fixed positive error fraction therefore introduces an extensive penalty in this bound, which can become vacuous.

There is also an exact obstruction in this protocol: a prover that stores $m=n-r$ designated qubits can guess all remaining $r$ bits arbitrarily and **always** make at most $r$ errors. Hence accepting a fixed fraction of errors cannot certify a deficit of only logarithmic size in this unmodified test. This is a counterexample for this acceptance rule, not a no-go theorem for every noise-tolerant memory-verification protocol.

For the store-and-Breidbart witness, a sharper achieved probability is

```math
\sum_{j=0}^{\min(r,t)}\binom tj(1-\beta)^j\beta^{t-j},
\qquad t=n-m.
```

It is a lower-bound strategy, not the claimed optimal attack.

## 3. Erasures committed before basis disclosure

Suppose the prover declares the discarded set before learning $\Theta$, with at most $\ell$ positions removed, and the verifier tests exact correctness on the remainder. Condition on that classical declaration in the EPR formulation and discard the untested Alice systems. The remaining premeasurement state is arbitrary, but its basis choices are still independent and uniform. Theorem G on at least $n-\ell$ positions gives

```math
P_{\mathrm{accept}}^{\mathrm{ideal}}
\leq\min\{1,2^{-(n-\ell-m)/6}\}.
```

The declaration may depend on the prover's earlier measurement record. No uniform-outcome assumption on the conditional remaining state is required. With additional tolerance of $r$ errors, the conditional list argument adds the corresponding Hamming volume for the actual surviving length.

## 4. Erasures chosen after basis disclosure

An output containing a string on specified positions and at most $\ell$ erasures accepts at most $2^\ell$ full strings. The general list theorem, which allows basis-dependent lists, therefore gives

```math
P_{\mathrm{accept}}^{\mathrm{ideal}}
\leq\min\{1,2^{\ell/2}2^{-(n-m)/6}\}.
```

For exactly $\ell$ erased positions and at most $r$ wrong surviving bits, the list size is $2^\ell V(n-\ell,r)$. For a variable erasure count, use the largest actual list size allowed by the rule. The stronger pre-basis erasure formula must not be used after adaptive basis-dependent selection.

## 5. Honest noise and source perturbations

If the honest recovered bits have independent error probability $e$, exact-string completeness is $(1-e)^n$. More generally, a union bound gives failure at most $\sum_i e_i$ without independence. To keep this contribution to failure below $\eta$, it suffices to have $\sum_i e_i\leq\eta$; uniform $e_i\leq\eta/n$ is one option. A fixed positive independent error rate makes exact-string completeness decay exponentially with $n$.

If a preparation state, including the verifier's labels, differs from an ideal joint state by trace distance at most $\xi$, every fixed acceptance probability changes by at most $\xi$. This elementary robustness fact may be added to a physically specified error model. It must not be substituted for the malicious-prover RSP guarantee, which is computational and pass-weighted rather than a universal trace-distance approximation.

These statements quantify model boundaries. They do not supply an error-correction implementation, assert independent physical errors, or establish a fixed-noise-rate version of the logarithmic-overhead exact-string theorem.
