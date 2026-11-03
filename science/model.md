# Model and principal statements

[Science guide](README.md) · [Complete proof](guessing-bound.md)

## Registers and chronology

Let $`n\geq1`$, $`d=2^n`$, and $`D\geq1`$. The verifier chooses independent uniform strings $`X,\Theta\in\{0,1\}^n`$. The supplied state is

```math
|X\rangle_\Theta=U_\Theta|X\rangle,
\qquad U_\theta=\bigotimes_{i=1}^n \mathsf H^{\theta_i},
\qquad \mathsf H=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
```

Before receiving $`\Theta`$, the prover applies any quantum instrument to the full input. Its retained information at the storage cut is a classical register $`C`$ and a quantum register $`Q`$ with $`\dim Q\leq D`$. The classical alphabet has no imposed size limit. After the cut, the verifier reveals $`\Theta`$; the prover chooses a POVM depending on $`(C,\Theta)`$ and outputs a string $`\widehat X`$. Exact success means $`\widehat X=X`$.

The encoder and decoder may act jointly across all positions, with unrestricted computational power in the ideal theorem. All quantum systems that persist across the cut and are later accessible to the prover are part of $`Q`$, including remote systems and initially shared references. Fresh uncorrelated decoding ancillas are allowed and are absorbed into the POVM. An environment returned during decoding must be counted in $`Q`$.

For a fixed encoder, $`P_{\mathrm{guess}}(X\mid CQ\Theta)`$ denotes the supremum of averaged success over its allowed decoders. The average includes the random bits, bases, and processing outcomes. The bound holds separately for every encoder, and therefore also after optimizing over encoders. All logarithms are base two.

## Theorem G: finite-dimensional guessing

For every encoder in this model,

```math
P_{\mathrm{guess}}(X\mid C Q\Theta)
\leq\min\{1,(D/d)^{1/6}\}.
```

In particular, $`D\leq2^m`$ and $`0\leq m\leq n`$ give the missing-qubit gap $`t=n-m`$ and imply

```math
P_{\mathrm{guess}}\leq2^{-(n-m)/6},
\qquad H_{\min}(X\mid C Q\Theta)\geq(n-m)/6.
```

Here $`H_{\min}(X\mid CQ\Theta)=-\log_2P_{\mathrm{guess}}(X\mid CQ\Theta)`$ is the operational conditional min-entropy of the classical string. The statement is finite and unsmoothed. For $`m\geq n`$, the dimension bound gives the trivial upper bound one.

### Stronger premeasurement formulation

Let $`\rho_{ACQ}`$ be any state, classical on $`C`$, with $`A`$ consisting of $`n`$ qubits and $`\dim Q\leq D`$. Choose $`\Theta`$ uniformly and independently of this state, measure $`A`$ in the product BB84 basis, and call the outcome $`X`$. The same bound holds. In this formulation $`X`$ need not be uniform conditioned on a branch.

The preparation experiment is a special case: begin with $`n`$ EPR pairs, apply the encoder to one half, and delay measurement of the other half until after the cut. The real BB84 bases ensure that measuring one half prepares the desired state on the other. Classical refinement to pure conditional states supplies the Schmidt-rank restriction used in the proof.

## Theorem C: conditional classical verification

Suppose a remote-state-preparation protocol satisfies the joint-pass-and-accept computational simulation interface stated in [the certification account](cryptographic-certification.md) with error $`\varepsilon_{\mathrm{RSP}}`$. For every efficient malicious prover whose total retained quantum dimension at the cut is at most $`2^m`$, with $`0\leq m\leq n`$,

```math
P_{\mathrm{accept}}
\leq\min\{1,\varepsilon_{\mathrm{RSP}}+2^{-(n-m)/6}\}.
```

The theorem is conditional on that interface; the cited LWE construction supplies it in the specified inverse-polynomial-error regime. The ideal bound G is unconditional.

## Theorem L: lists

Suppose each decoding outcome $`y`$ specifies a set $`\mathcal L_y`$ of at most $`L\geq1`$ candidate strings. The list may depend on the disclosed bases and the decoder's available information. With $`P_{\mathrm{list}}=\Pr[X\in\mathcal L_y]`$,

```math
P_{\mathrm{list}}
\leq\min\{1,\sqrt L\,(D/2^n)^{1/6}\}.
```

An acceptance rule with tolerated errors is a list rule, not exact decoding. Its proof and implications appear in [errors and losses](errors-and-losses.md).

## Operational meaning

A single observed pass does not determine a qubit count. The soundness bound limits the acceptance probability of every prover satisfying the dimension restriction. In the compiled protocol, the prover must also belong to the efficient class covered by the imported LWE assumption.

The cut can be placed within a waiting interval, provided all persistent quantum information at that cut is counted and all subsequent actions are included in the decoder. The certified resource is persistent storage at that cut; hardware location, quantum-channel capacity, and fault-tolerant workloads require separate models.
