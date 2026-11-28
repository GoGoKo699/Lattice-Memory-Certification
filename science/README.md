# Scientific account

A classical record can retain measurement outcomes but cannot, by itself, preserve all the information needed to answer incompatible quantum measurements selected later. This project quantifies that limitation when a prover can also retain a limited quantum system.

The central question is finite: when $`k`$ hidden BB84 inputs leave at most $`m`$ retained qubits, how strongly does the deficit $`t=k-m`$ suppress recovery of the **entire** hidden string? For $`0\leq m\leq k`$, the upper bound is $`2^{-t/6}`$, allowing collective encoding and decoding and unrestricted classical records. The stronger premeasurement formulation applies to arbitrary states, so it also supports conditioning on a pre-basis erasure declaration.

## Connected reading route

1. [Model and principal statements](model.md): timing, registers, the dimension restriction, and the distinction between unconditional and computational claims.
2. [Finite guessing bound](guessing-bound.md): classical refinement, discrimination, the BB84 quadratic form, hypercontractivity, and rank.
3. [Rank-sensitive small-challenge refinements](finite-guessing.md): exact collision optima for three, four and five inputs with one retained qubit, arbitrary-encoder guessing caps, and finite moment profiles. Includes the exact Breidbart-diagonal optimum, strictness of the original three-input cap, and the collision-only route obstruction.
4. [Direct discrimination and its limitations](direct-discrimination.md): exact fixed-encoder decoder certificates and a proved failure of diagonal duals on a Hamming-ball family; neither is a global encoder improvement.
5. [Classical certification from LWE-based preparation](cryptographic-certification.md): the imported simulation interface, the reduction, efficient parameter choices, and the counted-memory composition for processing.
6. [Lower bounds and resources](lower-bounds-and-resources.md): an explicit attack, optimal-order overhead, and what is actually charged.
7. [Errors and losses](errors-and-losses.md): scored decoding, tolerated errors, erasure timing, and honest-memory noise.
8. [Delayed-basis guessing and continuing noisy-memory processing](noisy-processing.md): the all-cut rank and exponential-moment floors, extinction-based reliability law, gate and contiguous-interval budgets, and extensions for correlated replacement and a classical verifier.

The [related-work comparison](../references/RELATED_WORK.md) identifies inherited tools and the fixed finite comparison with earlier rate-one uncertainty results. The [analytic figure](../verification/Graph/README.md) displays the achieved and universal bounds. The [verification guide](../verification/README.md) distinguishes finite checks from the analytical and computational premises.

## Notation and error targets

The input dimension is $`d=2^k`$ and the retained quantum dimension satisfies $`d_Q\leq2^m`$. The pure-branch Schmidt rank is $`r\leq\min(d_Q,d)`$; the Hamming error allowance is $`h`$. The operators $`\mathsf X,\mathsf Y,\mathsf Z`$ are the Paulis and $`\mathsf H`$ is the Hadamard. Normalized Schatten norms carry $`\mathrm{n}`$ in their subscript; all other matrix traces are ordinary unnormalized traces.

An ideal exact-string target is $`\delta`$. The compiled protocol has total soundness target $`\varepsilon`$ and preparation simulation error $`\eta_{\mathrm{prep}}`$. Allocating at most $`\varepsilon/2`$ to each contribution gives the additive storage choice in the certification account. Its efficient guarantee uses the imported nonuniform quantum-polynomial-time convention, sufficiently large security parameter, polynomial output length and inverse-polynomial soundness.

The noisy-device application declares its own resource notation: $`k`$ challenge qubits, $`n`$ total noisy persistent qubits, $`D`$ depolarizing rounds, and unconditional exact-string score $`p`$. Every persistent controller record is counted and noisy, and the fixed interior primitives retain their stated charges. It uses one full-output Pauli envelope before the basis-dependent free readout. These additional premises are not conclusions of the ideal guessing experiment.

## Dependency map

Theorem G (finite guessing) uses Lemma D (discrimination), Lemma P (pure-state identity), the imported qubit hypercontractivity theorem HC, and an elementary rank inequality. Theorem C (cryptographic compilation) uses G plus the explicitly stated RSP simulation property. Theorem L (list acceptance) replaces D by its list version and reuses P and HC. The lower-bound witness is an independently specified strategy, not an assumption in these proofs.

The [three-input certificate](finite-guessing.md) bounds arbitrary encoders with one retained qubit and unrestricted classical records. The tight $`9/16`$ averaged PGM bound and the inherited Renes inequality first give $`C_3=(2+7\sqrt2)/16`$. Stability near the PGM maximum then gives $`P^*_{3,1}\leq C_3-3\cdot10^{-8}`$. A flagged Pauli twirl equates the optimized arbitrary-state and preparation formulations. The Hamming-ball construction shows that the uniform exponent needs a proof beyond a rank-only PGM power bound followed by a square root.

The [direct-discrimination chapter](direct-discrimination.md) separates decoder optimization for one fixed encoder from optimization over all encoders. Exact primal/dual certificates enclose the former for two Hamming-ball projectors; those encoders underperform store-and-Breidbart. A separate all-size argument shows that restricting the decoder dual to the Breidbart-diagonal algebra cannot even reproduce the known universal exponent on the large-ball family. Competitive certificates on that route must keep off-diagonal information. This does not establish the optimal guessing exponent.

The achieved Breidbart strategy and universal bound fix the ideal exact-string gap at order $`\log_2(1/\delta)`$, uniformly in the retained block size, with unmatched constants. Tolerated errors and erasure timing change the acceptance rule; physical protection and total implementation cost require their own accounting.

The noisy application combines Theorem G with the CPTP Pauli-algebra factorization and dynamical ledger of [Measurement-Free-Memory-Cost](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/4b5ae9a75658bc44106b07fbb6deb2330e806df8/science/guessing_processing.md). It supplies an operational score-based corollary and keeps the main dynamical proof in that companion project. The prior recovery route implies both convenient mean-rank floors for every $`k\geq1`$. The companion's [moment theorem](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/4b5ae9a75658bc44106b07fbb6deb2330e806df8/science/moment_processing.md) retains the actual product-noise probabilities to strengthen the ledger. The [extensions](noisy-processing.md#extensions-of-the-score-to-gate-inference) give the conditions for using a correlated replacement process and for composing the score bound with a classical verifier.


The [extinction consequence](noisy-processing.md#survival-of-the-envelope-gives-a-reliability-dependent-budget) uses the chance score of an input-independent branch to limit total envelope extinction. A rank-dependent hazard and cumulative-rank balance then give a $`D\ln D`$ processing lower bound at fixed challenge, score and noise with logarithmic width. It changes neither the ideal guessing exponent nor the arbitrary-encoder finite bound; the companion owns the full T-charge theorem.
