# Scientific account

A classical record can retain measurement outcomes but cannot, by itself, preserve all the information needed to answer incompatible quantum measurements selected later. This project quantifies that limitation when a prover can also retain a limited quantum system.

The central question is finite: when $`n`$ hidden BB84 inputs leave at most $`m`$ retained qubits, how strongly does the deficit $`t=n-m`$ suppress recovery of the **entire** hidden string? For $`0\leq m\leq n`$, the upper bound is $`2^{-t/6}`$, allowing collective encoding and decoding and unrestricted classical records. The stronger premeasurement formulation applies to arbitrary states, so it also supports conditioning on a pre-basis erasure declaration.

## Connected reading route

1. [Model and principal statements](model.md): timing, registers, the dimension restriction, and the distinction between unconditional and computational claims.
2. [Finite guessing bound](guessing-bound.md): classical refinement, discrimination, the BB84 quadratic form, hypercontractivity, and rank.
3. [Classical certification from LWE-based preparation](cryptographic-certification.md): the imported simulation interface, the reduction, and efficient parameter choices.
4. [Lower bounds and resources](lower-bounds-and-resources.md): an explicit attack, optimal-order overhead, and what is actually charged.
5. [Errors and losses](errors-and-losses.md): scored decoding, tolerated errors, erasure timing, and honest-memory noise.
6. [Delayed-basis guessing and continuing noisy-memory processing](noisy-processing.md): a separate noisy-device application, its all-cut rank floor, gate and contiguous-interval budgets, and the strongest checked prior recovery comparison.

The [related-work comparison](../references/RELATED_WORK.md) identifies inherited tools and the fixed finite comparison with earlier rate-one uncertainty results. The [analytic figure](../verification/Graph/README.md) displays the achieved and universal bounds. The [verification guide](../verification/README.md) distinguishes finite checks from the analytical and computational premises.

## Notation and error targets

The input dimension is $`d=2^n`$ and the retained quantum dimension satisfies $`D\leq2^m`$. The pure-branch Schmidt rank is $`r\leq\min(D,d)`$; the Hamming error allowance is $`h`$. The operators $`\mathsf X,\mathsf Y,\mathsf Z`$ are the Paulis and $`\mathsf H`$ is the Hadamard. Normalized Schatten norms carry $`\mathrm{n}`$ in their subscript; all other matrix traces are ordinary unnormalized traces.

An ideal exact-string target is $`\delta`$. The compiled protocol has total soundness target $`\varepsilon`$ and preparation simulation error $`\varepsilon_{\mathrm{RSP}}`$. Allocating at most $`\varepsilon/2`$ to each contribution gives the additive storage choice in the certification account. Its efficient guarantee uses the imported nonuniform quantum-polynomial-time convention, sufficiently large security parameter, polynomial output length and inverse-polynomial soundness.

The noisy-device application declares its own resource notation: $`k`$ challenge qubits, $`n`$ total noisy persistent qubits, $`D`$ depolarizing rounds, and unconditional exact-string score $`p`$. Every persistent controller record is counted and noisy, and the fixed interior primitives retain their stated charges. It uses one full-output Pauli envelope before the basis-dependent free readout. These additional premises are not conclusions of the ideal guessing experiment.

## Dependency map

Theorem G (finite guessing) uses Lemma D (discrimination), Lemma P (pure-state identity), the imported qubit hypercontractivity theorem HC, and an elementary rank inequality. Theorem C (cryptographic compilation) uses G plus the explicitly stated RSP simulation property. Theorem L (list acceptance) replaces D by its list version and reuses P and HC. The lower-bound witness is an independently specified strategy, not an assumption in these proofs.

The achieved Breidbart strategy and universal bound fix the ideal exact-string gap at order $`\log_2(1/\delta)`$, uniformly in the retained block size, with unmatched constants. Tolerated errors and erasure timing change the acceptance rule; physical protection and total implementation cost require their own accounting.

The noisy application combines Theorem G with the CPTP Pauli-algebra factorization and dynamical ledger of [Measurement-Free-Memory-Cost](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/87296f795359b0b66e0c49d20555634fd0d3d3ae/science/guessing_processing.md). It supplies an operational score-based corollary and keeps the main dynamical proof in that companion project. Its recovery comparison finds no additional asymptotic processing consequence over the strongest checked prior route. The inference verifies neither device assumptions nor an LWE wrapper.

