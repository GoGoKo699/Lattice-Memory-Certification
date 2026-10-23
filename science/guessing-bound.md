# Complete proof of the finite guessing bound

[Model](model.md) · [Science guide](README.md)

All traces in intermediate matrix expressions are ordinary, unnormalized traces. The explicitly defined Schatten norms in the hypercontractivity step are normalized. This distinction produces the factor $2^{-n/3}$ before the final square root.

## 1. Classical refinement without extra quantum memory

In the stronger premeasurement model, first condition on $C=c$. Decompose the resulting density operator on $AQ$ as

```math
\rho^c_{AQ}=\sum_j p(j\mid c)|\psi_{cj}\rangle\langle\psi_{cj}|.
```

Give $j$ to the decoder as additional **classical** information. This can only increase its success probability and does not enlarge $Q$. The independent, uniform basis choice remains independent of $(c,j)$. It is therefore enough to bound every normalized pure branch $|\psi\rangle_{AQ}$, whose Schmidt rank $r$ satisfies

```math
r\leq\min(D,d),\qquad d=2^n.
```

It would not be legitimate to hand the prover a quantum purification of $\rho^c_{AQ}$ without charging its dimension. Nor is $\operatorname{rank}\rho_A\leq D$ true for an arbitrary mixed $\rho_{AQ}$: already $\rho_A=I/d$ with a one-dimensional $Q$ is a counterexample. The refinement above avoids both mistakes.

## 2. Lemma D: discrimination through the square-root measurement

Consider subnormalized positive operators $\{\sigma_x\}$ with $S=\sum_x\sigma_x$ and $\operatorname{Tr}S=1$. Write inverses only on the support of $S$. Define

```math
P_{\mathrm{pgm}}=\sum_x\operatorname{Tr}
 (\sigma_xS^{-1/2}\sigma_xS^{-1/2}).
```

This is the success probability of the pretty-good, or square-root, measurement, with any unused support completed arbitrarily. For every POVM $\{M_x\}$, set

```math
A_x=S^{-1/4}\sigma_xS^{-1/4},
\qquad B_x=S^{1/4}M_xS^{1/4}.
```

Hilbert–Schmidt Cauchy–Schwarz gives

```math
\left(\sum_x\operatorname{Tr}M_x\sigma_x\right)^2
\leq\left(\sum_x\operatorname{Tr}A_x^2\right)
     \left(\sum_x\operatorname{Tr}B_x^2\right).
```

The first factor is $P_{\mathrm{pgm}}$. Since $B_x$ are positive and $\sum_xB_x=S^{1/2}$, the second factor is at most $\operatorname{Tr}S=1$: every cross term $\operatorname{Tr}B_xB_y$ is nonnegative. Taking the supremum over POVMs proves

```math
P_{\mathrm{opt}}^2\leq P_{\mathrm{pgm}}.
```

This is an established Barnum–Knill bound, not a new discrimination theorem. The argument is included to fix normalization and support conventions. See [BK02](../references/RELATED_WORK.md#bk02-discrimination).

## 3. Lemma P: the pure-state identity

For a normalized pure branch, use a Schmidt decomposition

```math
|\psi\rangle_{AQ}=\sum_{j=1}^{r}\sqrt{\lambda_j}
 |a_j\rangle_A|b_j\rangle_Q,
\qquad \rho=\operatorname{Tr}_Q|\psi\rangle\langle\psi|,
\qquad R=\sqrt\rho.
```

For a fixed basis $\theta$, measuring $A$ yields the subnormalized vector

```math
|v_x\rangle=\sum_j\sqrt{\lambda_j}
 \langle x_\theta|a_j\rangle|b_j\rangle,
\qquad \sigma_x=|v_x\rangle\langle v_x|.
```

Its sum is $S=\sum_j\lambda_j|b_j\rangle\langle b_j|$, independent of $\theta$. Therefore

```math
\langle v_x|S^{-1/2}|v_x\rangle
=\sum_j\sqrt{\lambda_j}|\langle x_\theta|a_j\rangle|^2
=\langle x_\theta|R|x_\theta\rangle.
```

Substitution in Lemma D gives the exact identity

```math
P_{\mathrm{pgm}}(\theta)
=\sum_x\langle x_\theta|R|x_\theta\rangle^2.
```

The probabilities of the outcomes are already inside $\sigma_x$; no additional uniform-outcome assumption or division by an outcome probability is made.

## 4. BB84 averaging as a Pauli quadratic form

Let $\Delta_Z$ and $\Delta_X$ denote dephasing in the two single-qubit BB84 bases, and let $\mathcal T=(\Delta_Z+\Delta_X)/2$. Independence of the basis choices implies

```math
\mathbb E_\Theta P_{\mathrm{pgm}}(\Theta)
=\operatorname{Tr}\big[R\,\mathcal T^{\otimes n}(R)\big].
```

On the Pauli basis $(I,X,Y,Z)$, the eigenvalues of $\mathcal T$ are $(1,1/2,0,1/2)$. Let $\mathcal D_\eta(A)=\eta A+(1-\eta)\operatorname{Tr}(A)I/2$ be the qubit depolarizing map. Its Pauli eigenvalues are $(1,\eta,\eta,\eta)$.

Expand the Hermitian $R$ in orthogonal Pauli words. In the quadratic form, every real coefficient is squared. Each word's $\mathcal T$ weight is at most its $\mathcal D_{1/2}$ weight, so

```math
\operatorname{Tr}\big[R\,\mathcal T^{\otimes n}(R)\big]
\leq\operatorname{Tr}\big[R\,\mathcal D_{1/2}^{\otimes n}(R)\big]
=\operatorname{Tr}\left[\mathcal D_{1/\sqrt2}^{\otimes n}(R)^2\right].
```

The last equality uses self-adjointness of depolarization and composition of its parameters. This is a quadratic-form comparison, not a claim that the difference of the channels is completely positive.

## 5. Imported theorem HC and the rank estimate

For an operator on $n$ qubits define the normalized Schatten norm

```math
\|A\|_{p,\mathrm{norm}}=
 \left(d^{-1}\operatorname{Tr}|A|^p\right)^{1/p}.
```

Qubit hypercontractivity states that for Hermitian $A$, $1\leq p\leq2\leq q$, and $0\leq\eta\leq\sqrt{(p-1)/(q-1)}$,

```math
\|\mathcal D_\eta^{\otimes n}(A)\|_{q,\mathrm{norm}}
\leq\|A\|_{p,\mathrm{norm}}.
```

We import this tensor-power theorem as stated in Montanaro, Theorem 13; see [M12](../references/RELATED_WORK.md#m12-hypercontractivity). It is a substantive prior theorem, not a consequence inferred from our finite tests.

Choose $p=3/2$, $q=2$, and $\eta=1/\sqrt2$. Then

```math
\begin{aligned}
\mathbb E_\Theta P_{\mathrm{pgm}}(\Theta)
&\leq d\,\|R\|_{3/2,\mathrm{norm}}^2\\
&=d^{-1/3}\big(\operatorname{Tr}\rho^{3/4}\big)^{4/3}\\
&\leq d^{-1/3}r^{1/3}.
\end{aligned}
```

The last line is the elementary inequality $\sum_{j=1}^r\lambda_j^{3/4}\leq r^{1/4}$ for a probability vector, obtained by concavity or Hölder. In particular, the normalized trace factor has not been dropped.

## 6. Finish Theorem G

Apply Lemma D to each basis, then Cauchy–Schwarz to the classical average:

```math
\begin{aligned}
\mathbb E_\Theta P_{\mathrm{opt}}(\Theta)
&\leq\mathbb E_\Theta\sqrt{P_{\mathrm{pgm}}(\Theta)}\\
&\leq\sqrt{\mathbb E_\Theta P_{\mathrm{pgm}}(\Theta)}\\
&\leq(r/d)^{1/6}\leq(D/d)^{1/6}.
\end{aligned}
```

This holds for every pure conditional branch, hence also after averaging the refinement labels and discarding the extra information. It proves the arbitrary-state formulation and therefore the original preparation experiment. The proof covers any finite classical alphabet without an alphabet-dependent loss; countable records follow by summing conditional bounds. General classical records are handled by the same conditional-state integral in finite-dimensional quantum systems.

## Checks and interpretation

The full-memory endpoint $D=d$ permits success one. At zero quantum storage the bound is deliberately not sharp: it gives $2^{-n/6}$ while the explicit Breidbart strategy gives $\beta^n$. No equality characterization or optimal exponent constant is asserted.

The [finite verification](../verification/README.md) directly compares the Schmidt/PGM and Pauli identities, tests the imported norm inequality on finite examples, checks normalized quantum instruments, and reproduces lower-bound strategies. These checks complement the argument; they do not replace its universal quantifiers or an external proof review.
