# Classical verification through LWE-based preparation

[Model](model.md) · [Finite proof](guessing-bound.md) · [Resource boundary](lower-bounds-and-resources.md)

This page separates an unconditional information-theoretic statement from its conditional classical-verifier realization. It uses the remote-state-preparation (RSP) interface of Hhan, Morimae, Okinaka and Yamakawa, Definition 2.8 and Lemma 2.9, which in turn uses Zhang's verifiable-preparation work. The construction and LWE assumption are imported, not re-proved here. See [HMOY25 and Z25](../references/RELATED_WORK.md#hmoy25-and-z25-classical-preparation).

## 1. Imported simulation interface

Let the ideal joint state consist of uniform classical $(x,\theta)$ held by the verifier and $|x\rangle_\theta$ supplied to a preparation simulator. For every efficient malicious preparation prover, the imported property supplies an efficient simulator acting on the **quantum BB84 input alone**, producing a flag and the malicious prover's output system. For every efficient continuation, real and simulated probabilities of the joint event “preparation passes and continuation accepts” differ by at most $\varepsilon_{\mathrm{RSP}}$.

This is an unconditional, pass-weighted probability comparison. It is not a trace-distance statement about every malicious state, nor a statement conditioned on the flag being pass. The verifier's hidden $x$ and $\theta$ are not supplied classically to the simulator.

The honest-preparation property gives a joint state negligibly close in trace distance to the ideal BB84 source with a passing flag. Under the cited polynomial quantum hardness of LWE, the imported result supports polynomial-length outputs and inverse-polynomial simulation error with polynomially many rounds.

## 2. Protocol at general length

Run that preparation with output length $n$. The verifier retains its flag, $x$, and $\theta$. The honest prover retains the $n$ prepared qubits through the waiting period. Only after the storage cut does the verifier send $\theta$. The prover measures in the indicated bases and returns $\widehat x$. Accept exactly when preparation passed and $\widehat x=x$.

The verifier can send a uniform dummy basis on failed preparation while always rejecting. Nothing in the soundness proof requires leaking the flag before the cut. A malicious prover may perform arbitrary efficient preprocessing and compression before the cut; its classical record is unrestricted in the ideal analysis and polynomially generated in the cryptographic implementation.

## 3. Proof of Theorem C

Fix an efficient malicious prover and its actual encoder $E$ at the storage cut. Its retained output is $(C,Q)$ with $\dim Q\leq2^m$. Choose the simulator supplied by the RSP property.

Consider the efficient distinguishing continuation that runs $E$, reveals the verifier's basis as in the real protocol, runs the malicious decoder, and checks the returned string against $x$. The imported simulation guarantee gives

```math
P_{\mathrm{real\ accept}}
\leq\varepsilon_{\mathrm{RSP}}
 +P_{\mathrm{sim\ pass\ and\ correct}}.
```

Compose the simulator with $E$. This is an allowed encoder on the ideal BB84 source. Any simulator workspace that is retained and accessible after the cut is part of $Q$; discarded workspace cannot reappear during decoding. Its flag and transcripts may be added to $C$. This composition preserves the quantum memory restriction because the actual encoder defines the cut.

Give arbitrary output guesses to failed simulated branches, if needed, to obtain an ordinary complete decoding strategy. Then

```math
P_{\mathrm{sim\ pass\ and\ correct}}
\leq P_{\mathrm{sim\ correct}}
\leq2^{-(n-m)/6}
```

by Theorem G. Combining the inequalities proves C. No division by the preparation-pass probability occurs. In particular, rare passes cannot amplify a conditioning error in this argument. The simulator need not satisfy the memory restriction before $E$; all surviving quantum information must satisfy it after $E$.

## 4. Efficient inverse-polynomial corollary

Let $m(\lambda)\geq0$ be efficiently computable and polynomially bounded. Let $p(\lambda)\geq1$ be a polynomial target. Use an RSP with simulation error at most $1/(2p(\lambda))$ and choose

```math
n(\lambda)=m(\lambda)
 +\left\lceil6\log_2(2p(\lambda))\right\rceil.
```

Under the imported LWE hypothesis, this yields a polynomial-round classical-verifier protocol with false-acceptance probability at most $1/p(\lambda)$ against the specified efficient $m(\lambda)$-qubit provers. Honest completeness is $1-\operatorname{negl}(\lambda)$ in the ideal honest-storage model. Unlike the asymptotic estimate in HMOY25 Theorem 4.3, this finite calculation does not require $m(\lambda)=\omega(\log\lambda)$.

More generally, given an RSP with error at most $\varepsilon/2$, the algebraic choice $n=m+\lceil6\log_2(2/\varepsilon)\rceil$ makes total soundness at most $\varepsilon$. **Efficiently obtaining that RSP is a separate requirement.** The cited lemma directly supplies the inverse-polynomial regime, not arbitrary negligible error with polynomial overhead.

For example, the ideal storage term alone is at most $2^{-20}$ with a gap of $120$ qubits. Total soundness $2^{-20}$ with equal error allocation requires gap $126$ and RSP error at most $2^{-21}$. These are algebraic examples, not concrete LWE parameter recommendations or hardware cost estimates.

## 5. What this does and does not replace

The protocol wrapper and computational simulation framework are inherited. The replacement is the ideal finite-storage estimate. HMOY25's polynomial-hardness construction used honest storage $\lceil9.1m\rceil$ in its stated regime; the present corollary replaces that multiplicative gap by an additive one. Their separate four-round, negligible-soundness construction uses stronger hardness assumptions and is not superseded in those resource dimensions.

The result certifies a storage bottleneck under a specified computational model. It does not prove LWE hardness, provide a new LWE encryption scheme, establish negligible soundness under the same efficient compilation, or optimize the classical verifier's total cost. Error-tolerant acceptance can be composed with the same simulation property using Theorem L, but its list-size cost must then be included explicitly.
