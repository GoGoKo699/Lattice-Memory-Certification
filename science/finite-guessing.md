# A rank-sensitive three-input guessing bound

[Finite theorem](guessing-bound.md) · [Model](model.md) · [Noisy application](noisy-processing.md)

For three independent BB84 inputs and one retained quantum qubit, a two-copy purity constraint gives a certified finite improvement:

```math
\beta^2=\frac{3+2\sqrt2}{8}
\leq P^*_{3,1}
\leq C_3:=\frac{2+7\sqrt2}{16}
=0.743718433538229\ldots.
\qquad\text{(F1)}
```

Here unrestricted classical records and arbitrary joint encoders and basis-dependent POVMs are allowed. The lower value is $`0.728553390593274\ldots`$. The upper value improves the normalized DFW/Renes specialization $`(1+2\sqrt7)/8=0.786437827766148\ldots`$. It does not determine the optimum or improve the all-size exponent $`1/6`$.

The notation in this chapter is $`k`$ challenge qubits, retained quantum dimension $`d_Q`$, and $`m=\log_2 d_Q`$ when that dimension is a power of two. Thus the instance is $`k=3,d_Q=2,m=1`$. The general ideal theorem elsewhere uses $`n`$ for challenge qubits and $`D`$ for retained dimension. No noisy physical width or storage duration occurs in (F1).

## 1. Arbitrary states and the preparation experiment have the same optimum

The [existing proof](guessing-bound.md#1-classical-refinement-without-extra-quantum-memory) bounds a stronger-looking premeasurement experiment: prepare any state on $`AQ`$, with $`\dim A=2^k`$ and $`\dim Q\leq d_Q`$, choose independent uniform $`\Theta`$, measure $`A`$ in the product BB84 basis, and guess its entire outcome using $`Q`$ and unrestricted classical records. Refining each classical branch into pure states gives an upper bound without increasing the quantum dimension. Hence its optimum is attained on a pure state and finite basis-dependent POVMs.

Conversely, take any such pure state $`\psi_{AQ}`$ and a decoder. For every $`k`$-qubit Pauli $`P_a`$, form the flagged Pauli twirl

```math
\Omega_{AQC}=4^{-k}\sum_a
 (P_a\otimes I)\psi_{AQ}(P_a^\dagger\otimes I)
 \otimes|a\rangle\langle a|_C.
\qquad\text{(F2)}
```

Its $`A`$ marginal is $`I/2^k`$, so it is the normalized Choi state of a CPTP channel from the supplied input to $`QC`$. Explicitly, with the computational transpose,

```math
\mathcal E(B)=2^k\operatorname{Tr}_A[(B^T\otimes I)\Omega].
```

Measuring one half of a Bell state in a real BB84 basis prepares the original uniform BB84 input on the other half. Each Pauli maps a vector of a given product BB84 basis to another vector in that same basis, up to a phase. After learning $`a,\Theta`$, the decoder relabels the outcome by the corresponding bit flips and uses its original POVM. This preserves the score. The flag is classical and has only $`4^k`$ values; the quantum output dimension is unchanged.

Every arbitrary-state pure strategy therefore has a permitted preparation-experiment implementation with the same score. The reverse inclusion follows by source replacement. Thus the two optimized guessing probabilities are equal. This argument establishes attainability of arbitrary-state strategies, including the lower bound in (F1); it does not establish attainability of the upper bound $`C_3`$.

## 2. Exact three-qubit collision certificate

Consider one normalized pure conditional state on $`AQ`$, with $`\dim Q\leq2`$. Put $`\rho=\operatorname{Tr}_Q\psi`$ and $`R=\sqrt\rho`$. Then

```math
R\geq0,\qquad \operatorname{rank}R\leq2,\qquad
\operatorname{Tr}R^2=1,\qquad t_0:=(\operatorname{Tr}R)^2\leq2.
```

The existing pure-state identity gives the basis-averaged pretty-good guessing probability

```math
Q=\operatorname{Tr}[R\mathcal T^{\otimes3}(R)],\qquad
\mathcal T=(\Delta_X+\Delta_Z)/2.
\qquad\text{(F3)}
```

For each three-qubit Pauli word $`P`$, write $`t_P=(\operatorname{Tr}RP)^2\geq0`$. Ordinary, unnormalized Pauli orthogonality gives $`\sum_Pt_P=8`$. The multiplier of $`\mathcal T`$ on $`I,X,Y,Z`$ is respectively $`1,1/2,0,1/2`$. Let $`S_1`$ sum $`t_P`$ over the nine words of weight one, including $`Y`$ words. Each nonidentity word of weight at least two has multiplier at most $`1/4`$. Consequently

```math
Q\leq\frac18\left[t_0+\frac12S_1+
\frac14(8-t_0-S_1)\right]
=\frac14+\frac{3t_0+S_1}{32}.
\qquad\text{(F4)}
```

This relaxation intentionally assigns a positive weight to single-site $`Y`$ terms even though their actual multiplier is zero.

To constrain $`S_1`$, normalize $`\sigma=R/\operatorname{Tr}R`$. Linear-entropy subadditivity on three systems gives

```math
\sum_{i=1}^3\operatorname{Tr}\sigma_i^2
\leq2+\operatorname{Tr}\sigma^2.
\qquad\text{(F5)}
```

A self-contained two-copy certificate proves this inequality. For disjoint systems $`U,V`$, their swap operators commute, and

```math
(I-F_U)(I-F_V)\geq0.
```

Its expectation in $`\sigma_{UV}^{\otimes2}`$ is $`1-\operatorname{Tr}\sigma_U^2-\operatorname{Tr}\sigma_V^2+\operatorname{Tr}\sigma_{UV}^2`$. Apply it first to $`AB|C`$ and then to $`A|B`$. Equivalently, the resulting operator is the sum

```math
2I+F_{ABC}-F_A-F_B-F_C
=(I-F_{AB})(I-F_C)+(I-F_A)(I-F_B)\geq0.
```

The one-qubit Bloch identity and $`\operatorname{Tr}\sigma^2=1/t_0`$ now imply

```math
S_1=t_0\left(2\sum_i\operatorname{Tr}\sigma_i^2-3\right)
\leq t_0+2.
```

Combining this with (F4) and $`t_0\leq2`$ proves the **global certificate**

```math
Q\leq\frac5{16}+\frac{t_0}{8}\leq\frac9{16}.
\qquad\text{(F6)}
```

This is an exact outer relaxation covering every rank-two positive $`R`$. It is not an optimization over a selected family of encoders. Its PGM bound is tight: $`R=(I/\sqrt2)\otimes|b\rangle\langle b|\otimes|b\rangle\langle b|`$, with a pure real Bloch vector in the $`XZ`$ plane, gives $`Q=1\cdot(3/4)^2=9/16`$.

## 3. Convert the collision certificate to arbitrary decoding

Renes's finite-alphabet discrimination inequality [R17, equation (12)](../references/RELATED_WORK.md) states, for an eight-label ensemble,

```math
P_{\mathrm{pgm}}(\theta)\geq
p_\theta^2+\frac{(1-p_\theta)^2}{7},
```

where $`p_\theta`$ is its optimal POVM success. This theorem allows nonuniform ensemble probabilities and noncommuting states. Convexity of the right-hand side permits averaging over bases. For $`p=\mathbb E_\Theta p_\Theta\geq1/8`$, (F6) therefore yields

```math
p^2+\frac{(1-p)^2}{7}\leq\frac9{16}.
```

Solving the quadratic on $`[1/8,1]`$ gives $`p\leq C_3`$. Every classical pure branch has the same cap; averaging proves (F1) with unrestricted classical records, arbitrary encoders, and arbitrary basis-dependent POVMs. No nonconvex numerical optimization is used as an upper-bound certificate.

For comparison, the inherited normalized DFW spectral constraints with $`\operatorname{Tr}R\leq\sqrt2`$ yield only $`Q\leq5/8`$. Combining that value with the same Renes inequality gives $`(1+2\sqrt7)/8`$. The improvement comes from the additional two-copy purity constraint, not from changing the normalization or the discrimination theorem.

## 4. Survival through the noisy moment interface

The improvement is finite, but it can be composed before branch averaging. In the companion noisy application let an envelope of binary rank $`r`$ have $`s`$ quantum qubits and $`c`$ classical bits, so $`r=2s+c`$. For $`k=3,s=1`$, replace its quantum-dimension cap by $`C_3`$, retaining the output-dimension and all other valid caps. At $`r=4,s=1,c=2`$, the prior normalized recovery family permits the cap $`(1+2\sqrt7)/8`$, while (F1) gives the smaller $`C_3`$.

For a fully reproducible example take $`z=27/25`$. A concave majorant of the new integer-rank profile has rational knots

```math
(1,1/8),\quad(z^2,1/2),\quad
(z^3,311/500),\quad(z^4,93/125),\quad(z^6,1),
\qquad\text{(F7)}
```

continued at one. Its inputs include the classical cap $`\beta^3\lt311/500`$, (F1) with $`C_3\lt93/125`$, and the inherited recovery cap at rank five, $`(1+\sqrt{35})/8\lt173/200`$. The [exact verifier](../verification/verify_finite_guessing.py) checks the decreasing slopes and every integer rank using rational witnesses. Thus $`p\leq P(\mathbb E z^r)`$ at every applicable cut. In particular, $`\mathbb E z^r\leq z^4`$ forces $`p\leq93/125=0.744`$, whereas the prior rank-four cap exceeds $`3/4`$. For score $`p=3/4`$, the new moment floor is strictly greater than four:

```math
\log_z\left[z^4+\frac3{128}(z^6-z^4)\right]\gt4.
```

This is an improvement of a finite profile and its concave composition. It supplies no tensorization theorem against joint encoders and makes no change to the existing $`k=12`$ certified example.

## 5. A limitation of rank-sensitive collision methods

The finite certificate does not extend to a better uniform exponent by simply proving a stronger rank-sensitive PGM inequality. In fact, for any $`a\gt1/3`$ and any fixed finite $`C`$, the universal bound

```math
Q\leq C\left(\frac{\operatorname{rank}R}{2^k}\right)^a
```

is false, even for positive normalized $`R`$ diagonal in a product Breidbart basis.

To prove this, let $`k`$ run through multiples of eight, choose an integer $`b_k=\lfloor k^{3/4}\rfloor`$, and let $`S_k`$ be the set of binary strings of weight at most $`k/2-b_k`$. In the product eigenbasis of $`(X+Z)/\sqrt2`$, put

```math
r_k=|S_k|,\qquad R_k=P_{S_k}/\sqrt{r_k},\qquad
u_k=r_k/2^k.
```

On this diagonal algebra, $`\mathcal T`$ is exactly the classical binary channel with crossover probability $`1/4`$. If $`U`$ is uniform and $`V`$ is obtained by those independent flips, then

```math
Q_k=\Pr[U,V\in S_k]/\Pr[U\in S_k].
\qquad\text{(F8)}
```

Elementary binary type bounds and the Taylor expansion of relative entropy give

```math
\ln u_k=-2b_k^2/k+O(b_k^4/k^3+\ln k).
```

For a lower bound on the joint event, use the single joint type with counts $`3k/8+b_k,\ k/8,\ k/8,\ 3k/8-b_k`$ for $`00,01,10,11`$. Both marginal strings lie in $`S_k`$. Relative to the actual joint probabilities $`(3/8,1/8,1/8,3/8)`$, its relative entropy is

```math
\frac83\frac{b_k^2}{k^2}+O(b_k^4/k^4).
```

The multinomial type probability is at least its relative-entropy exponential times $`(k+1)^{-4}`$. Hence

```math
\ln Q_k\geq-\frac23\frac{b_k^2}{k}
-O(b_k^4/k^3+\ln k),\qquad
Q_k\geq u_k^{1/3+o(1)}.
\qquad\text{(F9)}
```

The existing hypercontractive bound gives $`Q_k\leq u_k^{1/3}`$, so the exponent $`1/3`$ of this rank-sensitive collision statistic is sharp in this regime. Taking $`m_k=\lceil\log_2r_k\rceil`$ changes the logarithmic deficit by less than one and preserves the obstruction for integer memory-qubit budgets.

Consequently, an argument consisting only of a universal rank-dependent upper bound on $`Q`$, followed by $`p\leq\sqrt Q`$ or the finite-alphabet Renes conversion, cannot improve the uniform guessing exponent beyond $`1/6`$. Here $`Q_k\gg2^{-k}`$, so the Renes conversion has the same square-root exponent. This is a limitation of that proof route. It does **not** show that the true guessing exponent is $`1/6`$, that $`C_3`$ is attainable, or that a stronger joint-discrimination argument is impossible.

## 6. Attribution, review scope and remaining questions

The pure-state PGM identity and hypercontractive estimate are inherited from the existing proof. The finite-alphabet PGM conversion is Renes (2017); the normalized spectral comparison is based on Dupuis, Fawzi and Wehner (2015). The two-copy purity inequality and the classical method-of-types mechanism are established tools. The additions here are their explicit rank-sensitive three-input evaluation, its compatible finite moment profile, the flagged-twirl equivalence, and the embedded obstruction to improving this collision-only proof route.

The prior audit inspected those primary sources and the Tomamichel–Fehr–Kaniewski–Wehner monogamy bound. The last is a two-recipient problem; a dimension-lifting application gives no stronger cap here. The internal Quantum Interface Cost comparison concerns local binary measurement statistics, rather than recovering the whole string. BB84 Basis Information concerns joint success of two separated recipients. Neither supplies a stronger theorem for the present single-recipient task. This is a scoped comparison, not an exhaustive publication-priority claim.

The uniform exponent remains $`1/6`$ in the proved theorem, with store-and-Breidbart imposing the necessary ceiling $`-\log_2\beta=0.2284466968\ldots`$ on any proposed universal exponent. The exact value of $`P^*_{3,1}`$, a better universal joint-discrimination inequality, and tensorization of finite improvements remain open. No sharper Hamming/list theorem is claimed. The existing obstruction at error tolerance $`h\geq k-m`$ remains unchanged.
