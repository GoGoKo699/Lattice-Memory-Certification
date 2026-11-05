# Lower bounds and resource accounting

[Science guide](README.md) · [Error and loss variants](errors-and-losses.md)

## 1. Explicit store-and-measure witness

For integer $`0\leq m\leq k`$, store any $`m`$ of the input qubits untouched. Measure each of the remaining $`t=k-m`$ qubits in the eigenbasis of

```math
B=(\mathsf X+\mathsf Z)/\sqrt2.
```

The positive eigenvalue outcome is decoded as bit zero and the negative one as bit one, for either subsequently announced basis. The corresponding Bloch vector has equal projections $`1/\sqrt2`$ along the Pauli $`\mathsf X`$ and $`\mathsf Z`$ axes, so the bit is correct with probability

```math
\beta=\frac{1+1/\sqrt2}{2}=\cos^2(\pi/8).
```

The stored qubits are decoded perfectly after the basis announcement. Product inputs and this product strategy give

```math
P_{\mathrm{ach}}=\beta^t.
```

This is the standard Breidbart measurement. Measuring in one fixed BB84 basis instead gives per-bit success $`3/4`$. The store-and-measure strategy supplies an explicit lower bound on optimal success.

## 2. Optimal logarithmic order

Let $`P^*_{k,m}`$ denote the optimum over all encoders and decoders in the ideal storage model. Theorem G and the explicit strategy give

```math
\beta^t\leq P^*_{k,m}\leq2^{-t/6}.
```

For target ideal exact-string success $`0<\delta<1`$, requiring $`P^*_{k,m}\leq\delta`$ forces

```math
t\geq\frac{\log_2(1/\delta)}{-\log_2\beta}
\simeq4.37739\log_2(1/\delta).
```

Round the necessary threshold upward for an integer deficit. Theorem G guarantees that $`t=\lceil6\log_2(1/\delta)\rceil`$ suffices whenever enough input qubits are supplied. Thus the necessary and sufficient deficit has order $`\Theta(\log(1/\delta))`$, uniformly in the stored block size, with unmatched constants. This order statement concerns the ideal exact-string test; the compiled protocol separately accounts for preparation error and work.

## 3. Finite comparison with an earlier uncertainty relation

The [related-work calculation](../references/RELATED_WORK.md#dfw15-finite-comparison) specializes Dupuis–Fawzi–Wehner Corollary 11 to the same memory dimension. For a fixed total $`k`$, ideal target $`\delta=2^{-20}`$ gives the following sufficient gaps:

| Total input qubits $`k`$ | This theorem | DFW Corollary 11, dimension-only specialization |
|---:|---:|---:|
| 1,024 | 120 | 290 |
| 10,000 | 120 | 426 |
| 1,000,000 | 120 | 698 |

The [verification script](../verification/verify.py) regenerates these numbers. Both columns are sufficient deficits obtained from the specified guessing bounds. Earlier rate-one security and this finite dimension-only comparison address different aspects of the storage tradeoff.

### Three inputs with one retained qubit

At $`k=3,m=1,d_Q=2`$, a separate exact finite certificate improves the available upper bound:

```math
\frac{3+2\sqrt2}{8}
\leq P^*_{3,1}
\leq\frac{2+7\sqrt2}{16}.
```

The values are approximately $`0.7285533906`$ and $`0.7437184335`$. The lower value is the explicit store-and-Breidbart strategy. The upper value follows from a global two-copy purity certificate and Renes's finite-alphabet discrimination inequality, improving the verified normalized DFW/Renes value $`(1+2\sqrt7)/8\simeq0.7864378278`$. The [full account](finite-guessing.md) covers arbitrary encoders and classical records, proves equality of the optimized arbitrary-state and preparation formulations, and checks a finite moment-profile consequence. It does not determine the optimum or tensorize against joint encoders.

The universal exponent remains $`1/6`$. Any universal guessing law $`P^*_{k,m}\leq2^{-c(k-m)}`$ must satisfy $`c\leq-\log_2\beta\simeq0.2284466968`$ by the achieved strategy. The [collision-method obstruction](finite-guessing.md#5-a-limitation-of-rank-sensitive-collision-methods) separately rules out a universal PGM rank exponent strictly above $`1/3`$, hence rules out improving $`1/6`$ through that collision-only route. It leaves stronger joint-discrimination arguments open.

## 4. Charged resources

| Resource | Accounting |
|---|---|
| Honest persistent quantum storage | $`k`$ ideal logical qubits in the exact-string protocol |
| Adversarial persistent quantum storage | Dimension at most $`2^m`$ for the union of all later-accessible quantum systems |
| Classical records | No imposed bound in Theorem G; efficiently generated in the compiled protocol |
| Preparation work and ancillas | Supplied by the imported RSP construction; polynomial in its supported regime, with total costs unoptimized |
| Decoding work | Honest product-basis readout and classical comparison; the adversary may use any joint decoder, efficient in the compiled theorem |
| Classical interaction | Polynomially many rounds for the imported polynomial-hardness construction |
| Randomness and hidden data | Uniform ideal $`x,\theta`$; the verifier's secret outputs and cryptographic randomness are not leaked before the cut |
| Waiting duration | An externally specified protocol parameter |

In the ideal theorem the BB84 input is an explicitly supplied quantum resource. The compiled protocol obtains the input through the imported computationally secure classical interaction, with its preparation work and communication costs retained.

An implementation may encode the $`k`$ logical qubits into more physical qubits for protection. Every physical system that survives the cut and remains accessible during decoding contributes to the quantum storage. The certified resource is persistent storage at that cut; total implementation cost and quantum-channel capacity are separate quantities.
