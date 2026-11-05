# Classical verification through LWE-based preparation

[Model](model.md) · [Finite proof](guessing-bound.md) · [Resource boundary](lower-bounds-and-resources.md)

The unconditional finite guessing bound becomes a conditional classical-verifier protocol through remote state preparation (RSP). This page uses the interface of Hhan, Morimae, Okinaka and Yamakawa, Definition 2.8 and Lemma 2.9, based on Zhang's verifiable-preparation work. See [HMOY25 and Z25](../references/RELATED_WORK.md#hmoy25-and-z25-classical-preparation) for the imported construction and LWE assumption.

## 1. Imported simulation interface

The ideal source consists of independent uniform labels $`(X,\Theta)`$ held by the verifier and the quantum state $`|X\rangle_\Theta`$ supplied to a simulator. For every efficient malicious preparation prover, the imported interface supplies an efficient simulator acting on the **quantum BB84 input alone**. It produces a preparation flag and the system passed to subsequent processing. For every efficient continuation, real and simulated probabilities of the joint event “preparation passes and the continuation accepts” differ by at most $`\eta_{\mathrm{prep}}`$. The continuation includes the verifier's use of its hidden labels; neither label is supplied classically to the simulator before the cut.

Efficient adversaries, simulators and continuations follow the imported nonuniform quantum-polynomial-time convention. The cryptographic guarantees hold for sufficiently large security parameter $`\lambda`$ and polynomially bounded output length.

The malicious-prover guarantee compares joint preparation-pass-and-accept probabilities **without conditioning on preparation passing**. Its assumptions are computational; it is not a trace-distance approximation for every malicious state.

The honest-preparation property gives a joint state negligibly close in trace distance to the ideal BB84 source with a passing flag. Under the cited polynomial quantum hardness of LWE, the imported result supports polynomial-length outputs and inverse-polynomial simulation error with polynomially many rounds.

## 2. Protocol at general length

Run that preparation with output length $`k`$. The verifier retains its flag, $`x`$, and $`\theta`$. The honest prover retains the $`k`$ prepared qubits through the waiting period. Only after the storage cut does the verifier send $`\theta`$. The prover measures in the indicated bases and returns $`\widehat x`$. Accept exactly when preparation passed and $`\widehat x=x`$.

The verifier can send a uniform dummy basis on failed preparation while always rejecting. Nothing in the soundness proof requires leaking the flag before the cut. A malicious prover may perform arbitrary efficient preprocessing and compression before the cut; its classical record is unrestricted in the ideal analysis and polynomially generated in the cryptographic implementation.

## 3. Proof of Theorem C

Fix an efficient malicious prover, for $`0\leq m\leq k`$, including its encoder $`E`$ whose output registers define $`(C,Q)`$ at the storage cut. The quantum output register has dimension $`\dim Q\leq2^m`$. Choose the simulator supplied by the RSP interface.

Consider the efficient distinguishing continuation that runs $`E`$, reveals the verifier's basis as in the real protocol, runs the malicious decoder, and checks the returned string against $`x`$. The imported simulation guarantee gives

```math
P_{\mathrm{real\ accept}}
\leq\eta_{\mathrm{prep}}
 +P_{\mathrm{sim\ pass\ and\ correct}}.
```

The simulator followed by $`E`$ is an allowed encoder on the ideal BB84 source. Its flag and transcripts may be retained classically. Every surviving accessible quantum system belongs to $`Q`$; discarded workspace cannot be restored during decoding. The simulator may use larger temporary workspace before $`E`$, since $`E`$ defines the bounded output register at the cut.

Give arbitrary output guesses to failed simulated branches, if needed, to obtain an ordinary complete decoding strategy. Then

```math
P_{\mathrm{sim\ pass\ and\ correct}}
\leq P_{\mathrm{sim\ correct}}
\leq2^{-(k-m)/6}
```

by Theorem G. Combining the inequalities gives Theorem C:

```math
P_{\mathrm{accept}}
\leq\min\{1,\eta_{\mathrm{prep}}+2^{-(k-m)/6}\}.
```

No division by the preparation-pass probability occurs. The dimension restriction is an output-register bound on $`E`$, so it applies to both real and simulated inputs. A rank bound on a state observed only in the real experiment would be a weaker premise.

## 4. Efficient inverse-polynomial corollary

Let $`m(\lambda)\geq0`$ be integer valued, efficiently computable and polynomially bounded in the security parameter $`\lambda`$. Let $`p(\lambda)\geq1`$ be a polynomial target. Use an RSP with simulation error at most $`1/(2p(\lambda))`$ and choose

```math
k(\lambda)=m(\lambda)
 +\left\lceil6\log_2(2p(\lambda))\right\rceil.
```

Under the imported LWE hypothesis, this yields a polynomial-round classical-verifier protocol with false-acceptance probability at most $`1/p(\lambda)`$ against the specified efficient $`m(\lambda)`$-qubit provers. Honest completeness is $`1-\mathrm{negl}(\lambda)`$ in the ideal honest-storage model. Unlike the asymptotic estimate in HMOY25 Theorem 4.3, this finite calculation does not require $`m(\lambda)=\omega(\log\lambda)`$.

More generally, for target total soundness $`\varepsilon\in(0,1)`$ and preparation error at most $`\varepsilon/2`$, the algebraic choice $`k=m+\lceil6\log_2(2/\varepsilon)\rceil`$ suffices. The cited lemma supplies the required preparation efficiently in the inverse-polynomial regime. Efficient negligible-soundness compilation would require a corresponding preparation guarantee.

For example, ideal target $`\delta=2^{-20}`$ requires a sufficient storage gap of $`120`$ qubits. Total soundness $`\varepsilon=2^{-20}`$ with equal error allocation requires gap $`126`$ and RSP error at most $`2^{-21}`$. These are algebraic error-budget examples.

## 5. Contribution and resource scope

The protocol wrapper and computational simulation framework are inherited. The replacement is the ideal finite-storage estimate. HMOY25's polynomial-hardness construction used honest storage $`\lceil9.1m\rceil`$ in its stated regime; the present corollary replaces that multiplicative gap by an additive one. Their separate four-round, negligible-soundness construction uses stronger hardness assumptions and is not superseded in those resource dimensions.

The certified resource is persistent quantum storage at the cut. Preparation work, ancillas, classical communication and physical protection remain separate resources, as specified in the [resource account](lower-bounds-and-resources.md#4-charged-resources). Error-tolerant acceptance can be composed with the same simulation interface using Theorem L, with its list-size cost included explicitly.
