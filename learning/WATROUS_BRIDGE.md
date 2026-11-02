# From Watrous to finite quantum-memory certification

[Learning guide](README.md) · [30 milestones](MILESTONES.md) · [Scientific account](../science/README.md)

## The experiment

A device receives qubits whose classical bit values were encoded in one of two incompatible bases. It does not yet know which basis was used at each position. It may process all the inputs together, keep an arbitrary classical record, and retain a smaller quantum system. Only afterward are the bases revealed. It must then return the **entire** hidden bit string correctly.

The distinction is between keeping a measurement record and keeping a quantum state on which the later-selected measurement can still be performed. The project quantifies that distinction without assuming that the device processes inputs independently. The [exact model](../science/model.md) specifies every register and the storage cut.

## Source and edition

The single anchor is John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018, DOI [10.1017/9781316848142](https://doi.org/10.1017/9781316848142). The author's [book page](https://jhwatrous.github.io/books-and-courses.html) links a [standard-layout prepublication copy](https://jhwatrous.github.io/TQI.pdf) and [errata](https://jhwatrous.github.io/TQI.errata.pdf).

The section and printed-page references below were checked against that January 2018 author copy on 2026-10-23. Printed page numbers are not PDF viewer indices; for example, printed page 138 is PDF page 146. The public copy is for personal use and is not redistributed in this repository. These learning pages contain project-specific explanations, not copied textbook passages. Consult the errata when using the book; this route does not rely on the channel-distance theorem corrected there as Theorem 3.56.

## Anchor sections

| Watrous location | Foundation used here | Project connection |
|---|---|---|
| §§1.1.1–1.1.2, pp. 1–23 | Vectors, tensor products, operators and trace | Registers, BB84 vectors and measurement probabilities |
| §1.1.3, pp. 24–34; Schmidt decomposition on p. 31 | Spectral calculus, operator norms and Schmidt decomposition | Square roots, support inverses and the pure-branch rank bound |
| §§1.2.1–1.2.2, pp. 35–52 | Convexity and probability | Classical refinement and averaging inequalities |
| §§2.1.1–2.1.3, pp. 58–71 | Classical/quantum registers, reductions and purifications | Separate the classical record from retained quantum systems |
| §§2.2.1–2.2.3, pp. 72–95 | Channels, representations and examples | Arbitrary encoders, dephasing and depolarization |
| §§2.3.1–2.3.2, pp. 100–112 | Measurements and their probabilities | Decoder POVMs and subnormalized conditional ensembles |
| §3.1.1, pp. 125–131 | Binary state discrimination | Operational probability tests and small examples |
| §3.1.2, pp. 132–139; Theorem 3.10 on pp. 138–139 | Ensemble discrimination and the pretty-good measurement | Lemma D and the reduction from optimal guessing to a quadratic expression |

These are selected locations, not a requirement to read every page in each interval. Chapter 6 can provide further entanglement context, but the Schmidt-rank step already has its needed foundation in §1.1.3. The project-specific cryptographic model is supplied below and in the canonical scientific account, not attributed to the textbook.

## Notation and normalization

Watrous generally writes vectors as $`u`$ and adjoints as $`u^*`$. Here the same vector is written $`|u\rangle`$, its adjoint is $`\langle u|`$, and $`uu^*`$ becomes $`|u\rangle\langle u|`$. The book's measurement function $`\mu(x)`$ is our POVM effect $`M_x`$. An ensemble element $`\eta(x)`$ corresponds to our subnormalized positive operator $`\sigma_x`$; its trace includes the probability of label $`x`$.

Our symbols $`n`$ and $`m`$ count input and retained qubits. The dimensions are $`d=2^n`$ and $`D\leq2^m`$. The symbol $`r`$ in the proof counts nonzero Schmidt coefficients of a **pure conditional state**. It need not equal $`D`$. The verifier's hidden bit string is $`X`$, the later-revealed basis string is $`\Theta`$, the unrestricted classical record is $`C`$, and the quantum memory is $`Q`$.

Watrous's Schatten norms are unnormalized. The imported hypercontractivity theorem instead uses

```math
\|A\|_{p,\mathrm{norm}}
=d^{-1/p}\|A\|_p
=\left(d^{-1}\operatorname{Tr}|A|^p\right)^{1/p}.
```

Here $`d`$ is the dimension of the space on which $`A`$ acts. The ordinary trace of a density operator is one, while the normalized trace of the identity is one. Confusing these conventions loses the input-dimension factor that makes the memory-deficit estimate meaningful.

When a positive operator has a zero eigenvalue, its negative powers in the proof act only on its support. This is the same support convention underlying the textbook's Moore–Penrose-inverse definition of the pretty-good measurement. Missing POVM support may be completed arbitrarily because it has zero ensemble probability.

For classical $`X`$, the project uses $`H_{\min}(X\mid C Q\Theta)=-\log_2P_{\mathrm{guess}}`$. This is an operational guessing definition, not the von Neumann entropy of a register. No general smooth-entropy formalism is needed for the finite proof.

## A complete two-qubit example

Take $`n=2`$ and permit one retained qubit, so $`m=1`$, $`d=4`$, and $`D=2`$. The source supplies $`|x_1\rangle_{\theta_1}|x_2\rangle_{\theta_2}`$ with all four label bits independent and uniform. The device stores the first qubit unchanged. Before learning either basis, it measures the second in the Breidbart basis, the eigenbasis of $`(X+Z)/\sqrt2`$, and records the outcome $`c\in\{0,1\}`$ classically.

The positive-eigenvalue vector is

```math
|b_0\rangle=\cos(\pi/8)|0\rangle+\sin(\pi/8)|1\rangle.
```

Choose the orthogonal real vector $`|b_1\rangle=-\sin(\pi/8)|0\rangle+\cos(\pi/8)|1\rangle`$ for the negative eigenvalue. Both have equal-magnitude projections along the computational and Hadamard measurement axes. Once the verifier reveals $`(\theta_1,\theta_2)`$, the device measures its stored qubit in basis $`\theta_1`$ to recover $`x_1`$ perfectly and uses $`c`$ as its guess for $`x_2`$ in either basis. Direct inner products give

```math
P(\widehat X=X)=\beta=\cos^2(\pi/8)
=\frac{1+1/\sqrt2}{2}\simeq0.853553.
```

One qubit and one classical bit persist across the storage cut in this strategy. The revealed bases and fresh readout workspace arrive later. This is an achieved strategy, not a proof of optimality among all collective one-qubit encoders.

To see the proof's objects, replace preparation by two EPR pairs and delay measurement of the verifier's halves $`A_1,A_2`$. Conditioned on the Breidbart outcome $`c`$, the normalized state is a Bell pair on $`A_1Q`$ tensored with $`|b_c\rangle`$ on $`A_2`$. Thus

```math
\rho_A=\frac{I_2}{2}\otimes|b_c\rangle\langle b_c|,
\qquad
R=\sqrt{\rho_A}
=\frac{I_2}{\sqrt2}\otimes|b_c\rangle\langle b_c|.
```

The marginal has rank two. In either basis, the second bit has conditional probabilities $`\beta`$ and $`1-\beta`$; the stored first bit is perfectly distinguishable. The square-root measurement therefore has success

```math
P_{\mathrm{pgm}}=\beta^2+(1-\beta)^2=\frac34.
```

The relevant comparison is

```math
\beta
\leq\sqrt{3/4}
\leq(2/4)^{1/6}
=2^{-1/6}\simeq0.890899.
```

The first inequality is the Barnum–Knill step and the second follows from the proof's hypercontractive estimate. The gap between achieved success and the final converse illustrates why the coefficient $`1/6`$ is not asserted optimal. The [learning checks](../verification/check_learning.py) calculate both conditional branches and all four basis strings directly.

## From the textbook to the finite bound

The [full proof](../science/guessing-bound.md) remains authoritative. Its logical bridge has five parts.

**Classical refinement.** Condition on the available classical record and decompose the remaining mixed state into pure states. Giving the decomposition label to the decoder is extra classical information, not an extra quantum purification. Every resulting pure state on $`AQ`$ has Schmidt rank at most $`D`$. This does not assert that an arbitrary mixed marginal $`\rho_A`$ has rank at most $`D`$.

**Discrimination.** For each basis, Watrous's Theorem 3.10 gives $`P_{\mathrm{opt}}^2\leq P_{\mathrm{pgm}}`$. The project includes the needed Cauchy–Schwarz argument as Lemma D. Substituting a Schmidt decomposition yields $`P_{\mathrm{pgm}}(\theta)=\sum_x\langle x_\theta|\sqrt\rho|x_\theta\rangle^2`$.

**Averaging the hidden bases.** Averaging this expression produces $`\operatorname{Tr}[R\mathcal T^{\otimes n}(R)]`$, with $`\mathcal T=(\Delta_Z+\Delta_X)/2`$. Its Pauli weights are bounded by those of depolarization with parameter $`1/2`$. This is a comparison of quadratic forms; it does not assert that one channel minus the other is completely positive.

**Imported hypercontractivity.** The required tensor-power inequality is [Montanaro's Theorem 13](../references/RELATED_WORK.md#m12-hypercontractivity), not a theorem supplied by the selected textbook. Its $`p=3/2`$, $`q=2`$ case and a rank estimate give

```math
\mathbb E_\Theta P_{\mathrm{pgm}}(\Theta)
\leq d^{-1/3}\big(\operatorname{Tr}\rho^{3/4}\big)^{4/3}
\leq(r/d)^{1/3}.
```

The rank estimate follows from $`\sum_{j=1}^r\lambda_j^{3/4}\leq r^{1/4}`$ for eigenvalues that sum to one. This is where limited quantum storage constrains the averaged experiment.

**Finish and interpret.** Averaging the discrimination inequality and using $`\mathbb E\sqrt Z\leq\sqrt{\mathbb E Z}`$ gives $`(D/2^n)^{1/6}`$. With $`D\leq2^m`$, this becomes $`2^{-(n-m)/6}`$. Averaging over the extra classical labels then returns the original experiment. The result applies to joint encoders and decoders, not just the product strategy in the example.

## From ideal inputs to a classical verifier

The ideal experiment assumes that the verifier can supply hidden BB84 states. A classical verifier cannot simply perform that preparation itself. The project instead imports an LWE-based remote-state-preparation protocol with a specific simulation guarantee; the complete assumptions and proof are in [classical certification](../science/cryptographic-certification.md).

For orientation, learning with errors concerns noisy modular linear equations: samples have the form $`(a,b)`$ with $`b=\langle a,s\rangle+e\pmod q`$, a hidden vector $`s`$, and a specified error distribution. Hardness depends on the parameter family and adversary model. This project does not establish hardness of those equations or choose deployment parameters. It uses the particular quantum-hardness assumption of the cited preparation theorem.

The preparation guarantee compares the probability of **preparation passing and the continuation accepting** against a simulator supplied with ideal quantum BB84 inputs, not with their classical hidden labels. Composing that simulator with the prover's actual compression at the storage cut gives an encoder covered by the finite theorem. Consequently,

```math
P_{\mathrm{accept}}
\leq\varepsilon_{\mathrm{RSP}}+2^{-(n-m)/6}.
```

There is no conditioning on a rare pass and no division by its probability. Preparation may require more workspace before the cut; all quantum information accessible across the cut is charged. This distinction is essential to preserving the physical meaning of the claim.

For target total error $`\varepsilon`$, allocating $`\varepsilon/2`$ to each contribution gives $`n=m+\lceil6\log_2(2/\varepsilon)\rceil`$. The cited efficient compilation supplies inverse-polynomial error, not an automatic efficient negligible-error result. The ideal converse remains unconditional even though its classical-verifier implementation is computational.

## What the complete result does not say

An explicit Breidbart strategy gives the [matching logarithmic order](../science/lower-bounds-and-resources.md) of the ideal overhead, but not a matching constant. A successful run gives a false-acceptance guarantee under a memory hypothesis, not a deterministic measurement of stored qubits. The [list, error and erasure results](../science/errors-and-losses.md) change the acceptance rule explicitly; fixed noise cannot be inserted into exact recovery without changing completeness. Logical retained qubits, physical error-correction overhead, preparation work, and channel capacity are different quantities.

The [milestone map](MILESTONES.md) integrates these distinctions into the scientific story. Primary research citations support the imported ingredients and comparisons; Watrous remains the one educational anchor.
