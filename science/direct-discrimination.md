# Direct decoding of the collision-obstruction encoders

[Finite theorem](finite-guessing.md) · [Guessing theorem](guessing-bound.md) · [Verification](../verification/README.md)

The collision obstruction leaves a specific question: do its encoders also have unusually large **optimal** guessing probability? This bounded investigation separates that question from their pretty-good measurement (PGM) score. It gives exact fixed-encoder certificates and proves that restricting the decoder dual to diagonal matrices loses the relevant asymptotic scale. It does not improve the universal exponent $`1/6`$ or the three-input, one-qubit cap $`(2+7\sqrt2)/16`$.

Here $`k`$ is challenge length, $`r`$ is retained quantum dimension, and $`m=\log_2r`$ when $`r`$ is a power of two. These are ideal memory parameters, not noisy physical width or storage duration.

## 1. All basis choices reduce to one discrimination problem

Let $`B`$ be the real orthogonal matrix with columns the two eigenvectors of the Hadamard observable $`(X+Z)/\sqrt2`$:

```math
B=\begin{pmatrix}c&s\\s&-c\end{pmatrix},\qquad
c=\cos(\pi/8),\quad s=\sin(\pi/8),\quad
\beta=c^2=\frac{1+1/\sqrt2}{2}.
```

Choose a set $`S\subseteq\{0,1\}^k`$ and let $`P_S`$ project onto those product Breidbart vectors. Use the pure Schmidt state with reduced density matrix $`\rho=P_S/r`$, where $`r=|S|`$. The flagged-twirl construction in the [finite chapter](finite-guessing.md#1-arbitrary-states-and-the-preparation-experiment-have-the-same-optimum) makes this a permitted preparation strategy with quantum output dimension $`r`$ and unrestricted classical records.

In Breidbart coordinates, put $`U=B^{\otimes k}`$ and $`v_x=P_SU|x\rangle/\sqrt r`$. The subnormalized conditional states for the computational basis are

```math
\sigma_x=|v_x\rangle\langle v_x|,\qquad
\sum_x\sigma_x=I_S/r.
\qquad\text{(D1)}
```

Changing the basis on any input qubit applies its Hadamard. That operator is diagonal in the Breidbart basis and commutes with $`P_S`$. Consequently every product-basis ensemble is a unitary conjugate of (D1), with the same labels. The decoder may undo this known conjugation after basis disclosure. The averaged BB84 success for this fixed encoder therefore equals the ordinary minimum-error discrimination optimum

```math
p_S=\max_{M_x\geq0,\,\sum_xM_x=I_S}\sum_x\mathrm{Tr}(M_x\sigma_x)
=\min_{Y\geq\sigma_x\ \forall x}\mathrm{Tr}Y.
\qquad\text{(D2)}
```

The second equality is the standard state-discrimination SDP duality; strict dual feasibility, for example $`Y=2I_S`$, removes a duality gap. It does not make optimization over the encoder convex. In particular, an upper certificate for one $`S`$ is not an upper bound over arbitrary permitted encoders.

## 2. Exact fixed-encoder certificates

For the radius-one balls $`S=\{x:|x|\leq1\}`$, the [certificate file](../verification/direct_discrimination_results.json) and [standard-library verifier](../verification/verify_direct_discrimination.py) give:

| Challenge $`k`$ | Dimension $`r`$ | Stored qubits $`m`$ | Certified $`p_S`$ interval | Store-and-Breidbart at the same dimension |
|---|---:|---:|---|---:|
| 3 | 4 | 2 | $`[0.8010769969,\ 0.801080996]`$ | $`0.853553390593\ldots`$ |
| 7 | 8 | 3 | $`[0.4609687373,\ 0.460976740]`$ | $`0.530790042944955\ldots`$ |

These instances differ from the three-input, **one-qubit** theorem. Both encoders perform worse than storing designated qubits and measuring the remainder in the Breidbart basis. Their actual optimal scores are also strictly smaller than their generic square-root PGM upper bounds.

The lower certificates are projective measurements with columns of the rational orthogonal matrix

```math
W=\begin{pmatrix}
a&b\mathbf1^T\\
b\mathbf1&-I+(1-a)\mathbf1\mathbf1^T/k
\end{pmatrix},\qquad
a=\frac{1-kv^2}{1+kv^2},\quad b=\frac{2v}{1+kv^2}.
\qquad\text{(D3)}
```

The rational choices are $`v=4269593/20000000`$ for $`k=3`$ and $`v=4694709/20000000`$ for $`k=7`$. The measurement guesses the corresponding label in $`S`$; all other label effects are zero. The verifier checks $`W^TW=I`$ and evaluates its score exactly in $`\mathbb Q(\sqrt2)`$.

The upper certificates are rational symmetric matrices $`Y`$, included in full. Their traces are respectively $`200270249/250000000`$ and $`23048837/50000000`$. Every constraint $`Y-\sigma_x\succ0`$ is checked by exact LDL decomposition over $`\mathbb Q(\sqrt2)`$: eight constraints and 128 constraints. Numerical optimization only suggested the matrices; exact arithmetic supplies their feasibility and the displayed bounds. No numerical see-saw convergence is used as a certificate.

These two balls do not belong to the near-half, growing-deficit sequence used in the asymptotic collision obstruction. Their failure to outperform store-and-Breidbart cannot settle the universal exponent.

## 3. Diagonal decoder duals fail on the asymptotic obstruction

One tempting simplification of (D2) is to take $`Y`$ diagonal in the Breidbart basis. The following limitation explains why that simplification cannot resolve the original collision-obstruction family.

Let $`S=\{x:|x|\leq h\}`$, with $`h\leq k/2`$, and let $`U_{\mathrm{diag}}(k,h)`$ be the minimum trace among such diagonal feasible duals. Define $`L=\lceil\sqrt k\rceil`$ and assume $`h\geq3L+2`$ and

```math
t=\left\lfloor\frac{h-2L-(1-\beta)k}{2\beta-1}\right\rfloor\in\{0,\ldots,k\}.
```

Then the finite bound is

```math
U_{\mathrm{diag}}(k,h)\geq
\frac{7}{8(3L+2)(k+1)}
\left(\frac{h-3L}{k-h+3L+1}\right)^{3L+1}.
\qquad\text{(D4)}
```

This is a **lower bound on a restricted dual upper bound**, not a lower bound on the physical guessing probability.

To prove it, average a diagonal feasible dual over coordinate permutations. Feasibility and trace are preserved, so its entry on a word of weight $`w`$ can be written $`y_w/r`$. All entries are positive because every entry of $`U`$ is nonzero. The rank-one constraint in (D2) is equivalent to

```math
\sum_{s\in S}\frac{|U_{s,x}|^2}{y_{|s|}}\leq1.
\qquad\text{(D5)}
```

The squared entries $`|U_{s,x}|^2`$ are exactly transition probabilities of independent binary flips with flip probability $`1-\beta`$. For any input $`x`$ of weight $`t`$, the output weight $`W_t`$ is the sum of independent $`\mathrm{Bin}(t,\beta)`$ and $`\mathrm{Bin}(k-t,1-\beta)`$ variables. Its mean and variance obey

```math
h-2L-(2\beta-1)<\mathbb EW_t\leq h-2L,
\qquad\mathrm{Var}(W_t)=k\beta(1-\beta)=k/8.
```

Chebyshev gives probability at least $`7/8`$ to the interval $`h-3L-1\leq W_t\leq h`$. This interval contains at most $`3L+2`$ integers, so some $`w_*`$ in it has probability at least $`7/[8(3L+2)]`$. Group (D5) by weight. Nonnegativity of its other terms gives $`y_{w_*}\geq\Pr[W_t=w_*]`$. Therefore

```math
\mathrm{Tr}Y\geq
\frac{\binom{k}{w_*}}r\frac{7}{8(3L+2)}.
```

Finally, use $`r\leq(k+1)\binom{k}{h}`$, monotonicity of binomial coefficients up to $`k/2`$, and

```math
\frac{\binom{k}{h-3L-1}}{\binom{k}{h}}
=\prod_{j=h-3L}^{h}\frac{j}{k-j+1}
\geq\left(\frac{h-3L}{k-h+3L+1}\right)^{3L+1}.
```

This proves (D4) for every diagonal feasible dual, without assuming it is optimal.

Now take the original sequence: $`k`$ runs through multiples of eight, $`b=\lfloor k^{3/4}\rfloor`$, and $`h=k/2-b`$. Its hypotheses hold for all sufficiently large $`k`$. The logarithm of the right-hand side of (D4) is bounded below by $`-O(b/\sqrt k+\ln k)`$. Meanwhile the existing universal theorem and the Hamming-ball dimension estimate give

```math
\begin{aligned}
U_{\mathrm{diag}}(k,h)&\geq\exp[-O(k^{1/4}+\ln k)],\\
p_S&\leq(r/2^k)^{1/6}
=\exp[-k^{1/2}/3+O(\ln k)].
\end{aligned}
\qquad\text{(D6)}
```

There is also a finite certified separation. At $`k=2^{24}`$, $`b=2^{18}`$ and $`h=8126464`$, rational logarithm enclosures applied to (D4) give $`U_{\mathrm{diag}}>e^{-831}`$. The binomial Hoeffding bound $`r/2^k\leq e^{-2b^2/k}`$ and the existing guessing theorem give $`p_S\leq e^{-4096/3}`$. For completeness, the tail estimate follows from $`\mathbb E e^{-\lambda(W-k/2)}=\cosh(\lambda/2)^k\leq e^{k\lambda^2/8}`$ for $`W\sim\mathrm{Bin}(k,1/2)`$, choosing $`\lambda=4b/k`$. This deliberately large instance certifies the distinction of scales; it is not a practical encoder recommendation.

Thus restricting the dual to this diagonal algebra cannot recover even the already proved exponential decay. Off-diagonal dual entries are essential for a direct-decoding proof on these states. The statement does not prevent symmetry reductions that retain off-diagonal blocks, nor does it determine their actual optimal decoder.

## 4. What this investigation establishes

The SDP and its dual are inherited state-discrimination tools. The additions are the explicit basis reduction for the obstruction encoders, the exact fixed-encoder certificates, and the diagonal-dual limitation (D4)–(D6). Their significance is methodological: they locate genuine conversion slack and rule out a natural attempted simplification on the difficult asymptotic family.

No stronger universal guessing theorem, improved optimum over all encoders, tensorization claim, or sharper Hamming-acceptance theorem follows. The actual asymptotic success of the near-half Hamming-ball encoders remains open. A useful next result would have to control their off-diagonal discrimination structure or provide a different direct joint-discrimination inequality.
