# From Watrous to finite quantum-memory certification

[Learning guide](README.md) · [30 milestones](MILESTONES.md) · [Scientific account](../science/README.md)

## The experiment

A device receives qubits whose classical bit values were encoded in one of two incompatible bases. It does not yet know which basis was used at each position. It may process all the inputs together, keep an arbitrary classical record, and retain a smaller quantum system. Only afterward are the bases revealed. It must then return the **entire** hidden bit string correctly.

The distinction is between keeping a measurement record and keeping a quantum state on which the later-selected measurement can still be performed. The project quantifies that distinction without assuming that the device processes inputs independently. The [exact model](../science/model.md) specifies every register and the storage cut.

## Source and edition

The single anchor is John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018, DOI [10.1017/9781316848142](https://doi.org/10.1017/9781316848142). The author's [book page](https://jhwatrous.github.io/books-and-courses.html) links a [standard-layout prepublication copy](https://jhwatrous.github.io/TQI.pdf) and [errata](https://jhwatrous.github.io/TQI.errata.pdf).

The section and printed-page references below use that January 2018 author copy. Printed page numbers are not PDF viewer indices; for example, printed page 138 is PDF page 146. The public copy is for personal use and is not redistributed in this repository. Consult the errata when using the book; this route does not rely on the channel-distance theorem corrected there as Theorem 3.56.

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
| §§3.2–3.3, pp. 139–198 | Fidelity and channel distances | Compare guessing-based conclusions with recoverable Bell fidelity |
| §§4.1.1 and 4.2.2 | Mixed-unitary channels, fixed points and spectra | Pauli conditional expectations and the companion's channel-rank bottleneck |

These are selected locations, not a requirement to read every page in each interval. Chapter 6 can provide further entanglement context, but the Schmidt-rank step already has its needed foundation in §1.1.3. Watrous is also the single educational anchor of [Measurement-Free Memory Cost](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost); its [bridge](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/main/learning/WATROUS_BRIDGE.md) develops the channel and Pauli-envelope side. The project-specific cryptographic and noisy-processing models are supplied by their scientific accounts rather than attributed to the textbook.

## Notation and normalization

Watrous generally writes vectors as $`u`$ and adjoints as $`u^*`$. Here the same vector is written $`|u\rangle`$, its adjoint is $`\langle u|`$, and $`uu^*`$ becomes $`|u\rangle\langle u|`$. The book's measurement function $`\mu(x)`$ is our POVM effect $`M_x`$. An ensemble element $`\eta(x)`$ corresponds to our subnormalized positive operator $`\sigma_x`$; its trace includes the probability of label $`x`$.

Our symbols $`n`$ and $`m`$ count input and retained qubits, with $`0\leq m\leq n`$. The dimensions are $`d=2^n`$ and $`D\leq2^m`$. The symbol $`r`$ in the proof counts nonzero Schmidt coefficients of a **pure conditional state**, while $`h`$ counts tolerated Hamming errors. The rank satisfies $`r\leq\min(D,d)`$. The verifier's hidden bit string is $`X`$, the later-revealed basis string is $`\Theta`$, the unrestricted classical record is $`C`$, and the quantum memory is $`Q`$.

The Pauli operators are $`\mathsf X,\mathsf Y,\mathsf Z`$, and the Hadamard operator is $`\mathsf H`$, so $`|x\rangle_\theta=\mathsf H^\theta|x\rangle`$ for one input qubit. These operator symbols are distinct from the hidden string $`X`$. We use $`\delta`$ for an ideal guessing-probability target, $`\varepsilon`$ for total false acceptance in the compiled protocol, and $`\varepsilon_{\mathrm{RSP}}`$ for the preparation simulation error.

Watrous's Schatten norms are unnormalized. The imported hypercontractivity theorem instead uses

```math
\|A\|_{p,\mathrm{n}}
=d^{-1/p}\|A\|_p
=\left(d^{-1}\mathrm{Tr}|A|^p\right)^{1/p}.
```

Here $`d`$ is the dimension of the space on which $`A`$ acts. The ordinary trace of a density operator is one, while the normalized trace of the identity is one. Confusing these conventions loses the input-dimension factor that makes the memory-deficit estimate meaningful.

When a positive operator has a zero eigenvalue, its negative powers in the proof act only on its support. This is the same support convention underlying the textbook's Moore–Penrose-inverse definition of the pretty-good measurement. Missing POVM support may be completed arbitrarily because it has zero ensemble probability.

For classical $`X`$, the project uses $`H_{\min}(X\mid C Q\Theta)=-\log_2P_{\mathrm{guess}}`$. This is an operational guessing definition, not the von Neumann entropy of a register. No general smooth-entropy formalism is needed for the finite proof.

The [noisy-processing application](../science/noisy-processing.md) uses $`k`$ for challenge length, $`n`$ for total noisy physical width, $`D`$ for noise rounds and $`r`$ for binary Pauli-envelope dimension. Those meanings differ from the ideal theorem's input count $`n`$, retained dimension $`D`$ and pure-branch Schmidt rank $`r`$. The application restates its convention before using the theorem; neither $`2n`$ physical label directions nor $`2^r`$ algebra dimension is automatically a count of surviving quantum qubits.

## A complete two-qubit example

Take $`n=2`$ and permit one retained qubit, so $`m=1`$, $`d=4`$, and $`D=2`$. The source supplies $`|x_1\rangle_{\theta_1}|x_2\rangle_{\theta_2}`$ with all four label bits independent and uniform. The device stores the first qubit unchanged. Before learning either basis, it measures the second in the Breidbart basis, the eigenbasis of $`(\mathsf X+\mathsf Z)/\sqrt2`$, and records the outcome $`c\in\{0,1\}`$ classically.

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

The pure branch has Schmidt rank $`r=2`$, equal to the rank of this marginal. In either basis, the second bit has conditional probabilities $`\beta`$ and $`1-\beta`$; the stored first bit is perfectly distinguishable. The square-root measurement therefore has success

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

**Averaging the hidden bases.** Averaging this expression produces $`\mathrm{Tr}[R\mathcal T^{\otimes n}(R)]`$, with $`\mathcal T=(\Delta_Z+\Delta_X)/2`$. Here $`\Delta_Z`$ and $`\Delta_X`$ dephase in the computational and Hadamard bases. On $`(I,\mathsf X,\mathsf Y,\mathsf Z)`$, the map has weights $`(1,1/2,0,1/2)`$, bounded by those of depolarization with parameter $`1/2`$. The comparison is between quadratic forms.

**Imported hypercontractivity.** The required tensor-power inequality is [Montanaro's Theorem 13](../references/RELATED_WORK.md#m12-hypercontractivity), with the Montanaro–Osborne attribution recorded there. For normalized Schatten norms, its $`p=3/2`$, $`q=2`$, $`\eta=1/\sqrt2`$ case and a rank estimate give

```math
\mathbb E_\Theta P_{\mathrm{pgm}}(\Theta)
\leq d^{-1/3}\big(\mathrm{Tr}\rho^{3/4}\big)^{4/3}
\leq(r/d)^{1/3}.
```

The rank estimate follows from $`\sum_{j=1}^r\lambda_j^{3/4}\leq r^{1/4}`$ for eigenvalues that sum to one. This is where limited quantum storage constrains the averaged experiment.

**Finish and interpret.** Averaging the discrimination inequality and using $`\mathbb E\sqrt Z\leq\sqrt{\mathbb E Z}`$ gives $`P_{\mathrm{guess}}\leq\min\{1,(D/2^n)^{1/6}\}`$. With $`D\leq2^m`$, this gives $`2^{-(n-m)/6}`$. Averaging over the extra classical labels then returns the original experiment, including joint encoders and decoders. For target ideal guessing probability $`0\lt \delta\lt 1`$, a deficit $`n-m\geq\lceil6\log_2(1/\delta)\rceil`$ suffices whenever the input length permits that gap.

## From ideal inputs to a classical verifier

The ideal experiment assumes that the verifier can supply hidden BB84 states. A classical verifier cannot simply perform that preparation itself. The project instead imports an LWE-based remote-state-preparation protocol with a specific simulation guarantee; the complete assumptions and proof are in [classical certification](../science/cryptographic-certification.md).

For orientation, learning with errors concerns noisy modular linear equations: samples have the form $`(a,b)`$ with $`b=\langle a,s\rangle+e\pmod q`$, a hidden vector $`s`$, and a specified error distribution. Hardness depends on the parameter family and adversary model. This project does not establish hardness of those equations or choose deployment parameters. It uses the particular quantum-hardness assumption of the cited preparation theorem.

The imported interface covers nonuniform quantum-polynomial-time provers and continuations, with polynomially bounded preparation length; its cryptographic guarantees hold for sufficiently large security parameter. It compares the probability of **preparation passing and the continuation accepting** against a simulator supplied with ideal quantum BB84 inputs alone. The verifier retains the classical hidden labels. Composing that simulator with the prover's actual compression at the storage cut gives an encoder covered by the finite theorem. Consequently,

```math
P_{\mathrm{accept}}
\leq\min\{1,\varepsilon_{\mathrm{RSP}}+2^{-(n-m)/6}\}.
```

There is no conditioning on a rare pass and no division by its probability. Preparation may require more workspace before the cut; all quantum information accessible across the cut is charged. This distinction is essential to preserving the physical meaning of the claim.

For target total false-acceptance probability $`0\lt \varepsilon\lt 1`$, choose $`\varepsilon_{\mathrm{RSP}}\leq\varepsilon/2`$ and ideal guessing target $`\delta=\varepsilon/2`$. This allocation gives $`n=m+\lceil6\log_2(2/\varepsilon)\rceil`$. The imported construction supplies polynomially many rounds and inverse-polynomial soundness. Efficient negligible-soundness compilation requires a corresponding preparation guarantee. The ideal converse remains unconditional even though its classical-verifier implementation is computational.

## Scope and resources

An explicit Breidbart strategy gives the [matching logarithmic order](../science/lower-bounds-and-resources.md) of the ideal overhead, but not a matching constant. A successful run gives a false-acceptance guarantee under a memory hypothesis, not a deterministic measurement of stored qubits. The [list, error and erasure results](../science/errors-and-losses.md) change the acceptance rule explicitly; fixed noise cannot be inserted into exact recovery without changing completeness. Logical retained qubits, physical error-correction overhead, preparation work, and channel capacity are different quantities.

The [milestone map](MILESTONES.md) integrates these distinctions into the scientific story. Primary research citations support the imported ingredients and comparisons; Watrous remains the one educational anchor.

## From a storage cut to a processing witness

The finite theorem also applies to the quantum-plus-classical output of a Pauli algebra. The [application](../science/noisy-processing.md) is self-contained about the new physical premises; the companion owns the [complete transfer and recovery comparison](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/main/science/guessing_processing.md).

Use $`k`$ independent uniform BB84 challenge qubits. The device receives the quantum states alone. The hidden string $`X`$ is never revealed, and only the basis string $`\Theta`$ is disclosed after all charged storage has ended. Let $`n`$ count every noisy persistent data, syndrome, controller and resource qubit, and let $`D`$ count independent depolarizing rounds. The score $`p`$ is unconditional whole-string success.

At each temporal cut, average the earlier noise into a CPTP prefix. Fixing future mathematical replacement choices gives a CPTP tail to the full physical output before the basis-dependent final readout. Its Pauli envelope starts with the conservative terminal reserve $`M=2n`$. If its rank is $`r=2s+c`$, a trace-preserving conditional expectation factors the tail through $`s`$ quantum qubits and $`c`$ classical bits. This is an actual CPTP quantum-plus-classical encoder, so Theorem G gives a branch score at most $`\min\{1,2^{(s-k)/6}\}`$.

Finite classical-alphabet dimension counting separately gives $`\min\{1,2^{s+c-k}\}`$. This second bound is applied to the genuine encoder before the optional pure-state refinement inside the guessing proof: the extra mathematical refinement labels do not belong to the physical $`c`$-bit register. Combining the two bounds and averaging over future noise forces an expected-rank floor at every cut. For $`k\ge8`$, one convenient floor is

```math
\mathbb E r_t\ge
2k\left[\frac{p-2^{-k}}{1-2^{-k}}\right]_+.
```

The same floor can then be inserted into the companion's gate and contiguous-interval ledger. The proof uses independent channel choices without postselection; it never supplies a noise flag to the device. Arbitrary endpoint readout is allowed after the charged interval.

For example, $`k=12`$ and $`p=0.4`$ yield an expected-rank floor about $`9.5965`$, even though the score is below one half. Applied branchwise before averaging, existing recovery inequalities imply both the straight-chord floor and the small-block polygon floor stated in the application. Those convenient floors therefore give no additional gate or interval consequence; the factorization explains the operational connection.

The [moment extension](../science/noisy-processing.md#exponential-moments-strengthen-the-dynamical-inference) retains actual product-noise probabilities in $`X_z=\log_z\mathbb E[z^r]`$. A coordinate-pivot injection and Jensen's inequality contract it by $`\alpha_z=\ln(1-q+qz^2)/(2\ln z)`$, while each T-type gate adds at most one. The direct quantum-plus-classical branch curve supplies a floor in this moment variable; fixing a recovery of the averaged channel supplies a complementary floor $`a_z`$ at every cut. The scalar optimization applies again, with its floor and noise factor replaced. In a growing challenge at fixed positive score, this improves the long-storage coefficient; the weak-noise order remains $`k\gamma D`$.

The interval reserve now bounds $`X_z`$, not only the mean rank. The full-output bound $`2n`$ is always safe. Neither this refinement nor the previous rank floor supplies physical flags or changes the storage model.

This application assumes a fixed circuit of the permitted primitives, input-independent replacement resets, and noisy counted persistent controller records. Their processing must still be charged correctly; counting record bits does not make arbitrary feedback free. A guessing score does not verify the model's noise or controller assumptions. At random-guessing success $`p=2^{-k}`$, discarding the challenge is a zero-processing strategy. The LWE compilation above is a separate result: no processing guarantee is automatically attached to it.

