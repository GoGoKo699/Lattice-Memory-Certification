# Lower bounds and resource accounting

[Science guide](README.md) · [Error and loss variants](errors-and-losses.md)

## 1. Explicit store-and-measure witness

For integer $0\leq m\leq n$, store any $m$ of the input qubits untouched. Measure each of the remaining $t=n-m$ qubits in the eigenbasis of

```math
B=(X+Z)/\sqrt2.
```

The positive eigenvalue outcome is decoded as bit zero and the negative one as bit one, for either subsequently announced basis. The corresponding Bloch vector has equal projections $1/\sqrt2$ along $X$ and $Z$, so the bit is correct with probability

```math
\beta=\frac{1+1/\sqrt2}{2}=\cos^2(\pi/8).
```

The stored qubits are decoded perfectly after the basis announcement. Product inputs and this product strategy give

```math
P_{\mathrm{witness}}=\beta^{n-m}.
```

This is the standard Breidbart measurement, not measurement in one fixed BB84 basis; the latter would instead give per-bit success $3/4$. Only the witness's achieved probability is needed here. No global optimality claim about this strategy at intermediate memory sizes is assumed.

## 2. Optimal logarithmic order

Let $0<\delta<1$ be the target **ideal exact-string** cheating probability. To guarantee that every strategy has success at most $\delta$, the explicit witness forces

```math
t\geq\frac{\log_2(1/\delta)}{-\log_2\beta}
\simeq4.37739\log_2(1/\delta).
```

Theorem G guarantees that the integer choice $t=\lceil6\log_2(1/\delta)\rceil$ suffices whenever enough input qubits are supplied. Thus the order $\Theta(\log(1/\delta))$ is both necessary and sufficient, uniformly in the stored block size. The coefficients are not matched. This is an order statement for the ideal model, not a claim that every classical-verifier protocol needs the same overhead.

## 3. Finite comparison with an earlier uncertainty relation

The [related-work calculation](../references/RELATED_WORK.md#dfw15-finite-comparison) specializes Dupuis–Fawzi–Wehner Corollary 11 to the same memory dimension. For a fixed total $n$, ideal target $\delta=2^{-20}$ gives the following sufficient gaps:

| Total input qubits $n$ | This theorem | DFW Corollary 11, dimension-only specialization |
|---:|---:|---:|
| 1,024 | 120 | 290 |
| 10,000 | 120 | 426 |
| 1,000,000 | 120 | 698 |

The [verification script](../verification/verify.py) regenerates these numbers. This table compares two particular certified upper bounds, not optimized attacks, all possible consequences of DFW, or measured hardware performance. Earlier rate-one security is fully compatible with this finite improvement.

## 4. Charged resources

| Resource | Accounting |
|---|---|
| Honest persistent quantum storage | $n$ ideal logical qubits in the exact-string protocol |
| Adversarial persistent quantum storage | Dimension at most $2^m$ for the union of all later-accessible quantum systems |
| Classical records | No imposed bound in Theorem G; efficiently generated in the compiled protocol |
| Preparation work and ancillas | Supplied by the imported RSP construction; polynomial in its supported regime, not cost-free or quantitatively optimized here |
| Decoding work | Honest product-basis readout and classical comparison; the adversary may use any joint decoder, efficient in the compiled theorem |
| Classical interaction | Polynomially many rounds for the cited polynomial-hardness construction; no constant-round improvement is claimed |
| Randomness and hidden data | Uniform ideal $x,\theta$; the verifier's secret outputs and cryptographic randomness are not leaked before the cut |
| Waiting duration | A physical protocol parameter; no new timing-enforcement mechanism or device-independent clock is established |

No QRAM, coherent database oracle, or free state-loading procedure is assumed. In the ideal theorem the BB84 input is an explicitly supplied quantum resource; in the compiled theorem its physical preparation is replaced by the cited computationally secure classical interaction, with its costs retained.

A dimension witness is not a quantum-capacity theorem. An implementation may encode the $n$ logical qubits into more physical qubits for protection. Those physical systems remain quantum storage; the resource claim must identify whether it refers to logical or physical degrees of freedom. This analysis does not give a fault-tolerant architecture or a hardware crossover estimate.
