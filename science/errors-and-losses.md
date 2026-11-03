# Errors, lists and losses

[Model](model.md) · [Exact proof](guessing-bound.md)

Changing the acceptance rule changes how much information the prover must preserve. A list of candidate strings gives a common way to analyse tolerated errors and erasures.

## 1. Lemma DL: list discrimination

Use the ensemble and notation of Lemma D. A POVM outcome $`y`$ specifies a list $`\mathcal L_y`$ of at most $`L\geq1`$ candidate labels. Define

```math
F_x=\sum_{y:x\in\mathcal L_y}M_y.
```

Then $`0\leq F_x\leq I`$ and $`\sum_xF_x\leq L I`$. With $`A_x=S^{-1/4}\sigma_xS^{-1/4}`$ as before, set $`B_x=S^{1/4}F_xS^{1/4}`$. Now $`0\leq B_x\leq S^{1/2}`$, so

```math
\sum_x\mathrm{Tr}B_x^2
\leq\sum_x\mathrm{Tr}(B_xS^{1/2})
=\mathrm{Tr}\left(S\sum_xF_x\right)\leq L.
```

Cauchy–Schwarz therefore yields

```math
P_{\mathrm{list}}^2\leq L P_{\mathrm{pgm}}.
```

The list can depend on the disclosed bases and the prover's available information. Apply this inequality separately to every basis and refined pure branch. The quadratic-form and hypercontractive estimates from the exact proof imply Theorem L:

```math
P_{\mathrm{list}}
\leq\min\{1,\sqrt L\,(D/2^n)^{1/6}\}.
```

For $`D\leq2^m`$, this becomes $`P_{\mathrm{list}}\leq\min\{1,\sqrt L\,2^{-(n-m)/6}\}`$. Randomized lists are included among the POVM outcomes. The broader square-root-measurement score framework is credited in [related work](../references/RELATED_WORK.md#scored-discrimination).

## 2. Hamming errors

Suppose acceptance allows at most $`h`$ wrong bits, for an integer $`0\leq h\leq n`$. Each returned string defines a Hamming ball of size

```math
V(n,h)=\sum_{j=0}^{h}\binom nj.
```

Consequently the ideal cheating probability is at most

```math
\min\{1,\sqrt{V(n,h)}\,2^{-(n-m)/6}\}.
```

For target total soundness $`\varepsilon\in(0,1)`$ and preparation error at most $`\varepsilon/2`$, a sufficient condition is

```math
n-m\geq3\log_2V(n,h)+6\log_2(2/\varepsilon).
```

For $`h\leq n/2`$, the binary-entropy estimate $`V(n,h)\leq2^{n h_2(h/n)}`$ gives the conservative sufficient condition $`n-m\geq3n h_2(h/n)+6\log_2(2/\varepsilon)`$. Here $`h_2(a)=-a\log_2a-(1-a)\log_2(1-a)`$, with $`0\log_2 0=0`$. A fixed positive error fraction introduces an extensive penalty in this bound, which can become vacuous. No optimal error-tolerant tradeoff is established by this estimate.

There is also a direct obstruction: a prover that stores $`m=n-h`$ designated qubits can guess the remaining $`h`$ bits arbitrarily and **always** make at most $`h`$ errors. More generally, if the allowed error budget is at least the actual deficit $`n-m`$, ideal acceptance can be one. Thus this unmodified acceptance rule cannot certify a merely logarithmic deficit while allowing a fixed fraction of wrong answers. Other noise-tolerant protocols require their own analysis.

For the [store-and-Breidbart strategy](lower-bounds-and-resources.md#1-explicit-store-and-measure-witness), only the $`t=n-m`$ measured positions can be wrong. Their error indicators are independent with probability $`1-\beta`$, where $`\beta=(1+1/\sqrt2)/2`$. Its achieved error-tolerant probability is

```math
\sum_{j=0}^{\min(h,t)}\binom tj(1-\beta)^j\beta^{t-j},
\qquad t=n-m.
```

This gives an achieved lower bound on the optimal acceptance probability.

## 3. Erasures committed before basis disclosure

Let $`0\leq\ell\leq n`$ be an integer. Suppose the prover declares the discarded set $`S`$ before learning $`\Theta`$, with $`|S|\leq\ell`$, and the verifier tests exact correctness on the remainder. Condition on the declaration and any earlier classical record in the EPR formulation. Let $`k=n-|S|`$ be the actual surviving length, and trace out the verifier's untested systems. The remaining premeasurement state may be arbitrary and mixed, but its basis choices are independent and uniform. For $`k\geq1`$, the stronger form of Theorem G gives

```math
P_{\mathrm{pre}\mid S}
\leq\min\{1,2^{-(k-m)/6}\}.
```

For $`k=0`$, the trivial bound one gives the same expression. Since $`k\geq n-\ell`$, averaging the declaration yields

```math
P_{\mathrm{accept}}^{\mathrm{ideal}}
\leq\min\{1,2^{-(n-\ell-m)/6}\}.
```

The declaration may depend on the prover's earlier measurement record; the conditional outcome string need not be uniform. If the rule also allows a nonnegative integer budget $`h`$ of wrong surviving bits, the conditional list argument gives

```math
P_{\mathrm{pre, Ham}\mid S}
\leq\min\left\{1,
\sqrt{V(k,\min\{h,k\})}\,2^{-(k-m)/6}\right\}.
```

The convention $`V(0,0)=1`$ includes the empty surviving string. For a variable erasure count, take the maximum over the allowed surviving lengths. Both the Hamming volume and the memory deficit depend on $`k`$.

## 4. Erasures chosen after basis disclosure

An output with erased set $`S`$ and a fixed string outside $`S`$ accepts exactly $`2^{|S|}`$ full strings. With at most $`\ell`$ erasures, its list has size at most $`2^\ell`$, even if $`S`$ depends on the disclosed bases and the decoding outcome. The general list theorem therefore gives

```math
P_{\mathrm{accept}}^{\mathrm{ideal}}
\leq\min\{1,2^{\ell/2}2^{-(n-m)/6}\}.
```

No factor $`\binom n\ell`$ is needed: the theorem bounds the list attached to each actual output, rather than a union over outputs that were not produced. For exactly $`\ell`$ erased positions and a nonnegative integer budget $`h`$ of wrong surviving bits, use

```math
L=2^\ell V(n-\ell,\min\{h,n-\ell\}).
```

For a variable erasure count, use the largest permitted actual list size. The pre-basis and post-basis guarantees apply to their respective declaration times.

## 5. Honest noise and source perturbations

If honest recovered bits have independent error probability $`e`$, exact-string completeness is $`(1-e)^n`$. Without independence, the union bound gives failure at most $`\sum_i e_i`$, where $`e_i`$ is the marginal error probability at position $`i`$. To keep this contribution to completeness loss at most $`\eta`$, it suffices that $`\sum_i e_i\leq\eta`$; uniform $`e_i\leq\eta/n`$ is one option. A fixed positive independent error rate makes exact-string completeness decay exponentially with $`n`$. These are statements about a supplied physical error model, not assumptions of independent attacks in Theorem G.

For joint preparation states $`\omega`$ and $`\omega_{\mathrm{id}}`$, including the verifier's labels, let $`\xi=\tfrac12\|\omega-\omega_{\mathrm{id}}\|_1`$. Every fixed acceptance effect $`0\leq M\leq I`$ obeys

```math
\left|\mathrm{Tr}(M\omega)
-\mathrm{Tr}(M\omega_{\mathrm{id}})\right|\leq\xi.
```

This perturbation bound applies when the joint trace-distance premise is available. The malicious-prover [RSP interface](cryptographic-certification.md#1-imported-simulation-interface) instead compares computationally accessible joint preparation-pass-and-accept events.

These statements quantify model boundaries. They do not supply an error-correction implementation, assert independent physical errors, or establish a fixed-noise-rate version of the logarithmic-overhead exact-string theorem.
