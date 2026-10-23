# Model and principal statements

[Science guide](README.md) · [Complete proof](guessing-bound.md)

## Registers and chronology

Let $n\geq1$, $d=2^n$, and $D\geq1$. The verifier chooses independent uniform strings $X,\Theta\in\{0,1\}^n$. The supplied state is

```math
|X\rangle_\Theta=U_\Theta|X\rangle,
\qquad U_\theta=\bigotimes_{i=1}^n H^{\theta_i},
\qquad H=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
```

Before receiving $\Theta$, the prover applies any quantum instrument to the full input. Its retained information at the storage cut is a classical register $C$ and a quantum register $Q$ with $\dim Q\leq D$. The classical alphabet has no imposed size limit. After the cut, the verifier reveals $\Theta$; the prover chooses a POVM depending on $(C,\Theta)$ and outputs a string $\widehat X$. Exact success means $\widehat X=X$.

The encoder and decoder may act jointly across all positions. In the ideal theorem they need not be efficient. All quantum systems that persist across the cut and are later accessible to the prover are part of $Q$, even when stored elsewhere or initially called a reference. An inaccessible discarded environment is not given back later. Fresh uncorrelated ancillary states during decoding are allowed and are absorbed into the POVM. There is no presumption that a physical device uses independent attacks or independent noise.

## Theorem G: finite-dimensional guessing

For every encoder and decoder in this model,

```math
P_{\mathrm{guess}}(X\mid C Q\Theta)
\leq\min\{1,(D/d)^{1/6}\}.
```

In particular, $D\leq2^m$ and $0\leq m\leq n$ imply

```math
P_{\mathrm{guess}}\leq2^{-(n-m)/6},
\qquad H_{\min}(X\mid C Q\Theta)\geq(n-m)/6.
```

Here conditional min-entropy for a classical variable is defined operationally as the negative base-two logarithm of optimal guessing probability. The statement is unsmoothed and finite; it has no asymptotic remainder. The $m\geq n$ regime has only the trivial upper bound one.

### Stronger premeasurement formulation

Let $\rho_{ACQ}$ be **any** state, classical on $C$, with $A$ consisting of $n$ qubits and $\dim Q\leq D$. Choose $\Theta$ uniformly and independently of this state, measure $A$ in the product BB84 basis, and call the outcome $X$. The same bound holds. In this formulation $X$ need not be uniform conditioned on a branch.

The preparation experiment is a special case: begin with $n$ EPR pairs, apply the encoder to one half, and delay measurement of the other half until after the cut. The real BB84 bases ensure that measuring one half prepares the desired state on the other. The proof never imposes an invalid rank bound on the mixed marginal $\rho_A$; rank is used only after a classical refinement to pure conditional states.

## Theorem C: conditional classical verification

Suppose a remote-state-preparation protocol satisfies the pass-weighted computational simulation interface stated in [the certification account](cryptographic-certification.md) with error $\varepsilon_{\mathrm{RSP}}$. For every efficient malicious prover whose total retained quantum dimension at the cut is at most $2^m$,

```math
P_{\mathrm{accept}}
\leq\min\{1,\varepsilon_{\mathrm{RSP}}+2^{-(n-m)/6}\}.
```

The theorem is conditional on that interface; the cited LWE construction supplies it in a specified inverse-polynomial-error regime. The ideal bound G itself has no LWE assumption. The roles of the ideal input, the simulator, and the real classical interaction must not be interchanged.

## Theorem L: lists

Suppose the decoder's output specifies a set of at most $L\geq1$ possible hidden strings. The set may depend on the basis and the classical record, but not on the unknown $X$ except through the decoder's actual information. Then

```math
P_{\mathrm{list}}
\leq\min\{1,\sqrt L\,(D/2^n)^{1/6}\}.
```

An acceptance rule with tolerated errors is a list rule, not exact decoding. Its proof and implications appear in [errors and losses](errors-and-losses.md).

## Operational meaning

A false-acceptance probability is not a deterministic count of qubits inferred from one observed pass. It bounds how often a prover satisfying the dimension restriction can pass the specified test. Under the cryptographic compilation, the adversary must also belong to the efficient class in the imported LWE security assumption.

The cut can be placed within a waiting interval, provided all persistent quantum information at that cut is counted and all subsequent actions are included in the decoder. The theorem does not identify the hardware location, prove a quantum-channel capacity, or establish usefulness for arbitrary fault-tolerant workloads.
