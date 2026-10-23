# Scientific account

A classical record can retain measurement outcomes but cannot, by itself, preserve all the information needed to answer incompatible quantum measurements selected later. This project quantifies that limitation when a prover can also retain a limited quantum system.

The central question is finite: if $n$ hidden BB84 qubits are compressed to $m$ qubits, how strongly does the deficit $n-m$ suppress the probability of recovering the **entire** hidden string? The bound proved here is $2^{-(n-m)/6}$, valid even for collective compression and arbitrarily much classical information. The derivation also treats a more general premeasurement state, which makes error and loss qualifications precise.

## Connected reading route

1. [Model and principal statements](model.md): timing, registers, the dimension restriction, and the distinction between unconditional and computational claims.
2. [Finite guessing bound](guessing-bound.md): classical refinement, discrimination, the BB84 quadratic form, hypercontractivity, and rank.
3. [Classical certification from LWE-based preparation](cryptographic-certification.md): the imported simulation interface, the reduction, and efficient parameter choices.
4. [Lower bounds and resources](lower-bounds-and-resources.md): an explicit attack, optimal-order overhead, and what is actually charged.
5. [Errors and losses](errors-and-losses.md): scored decoding, tolerated errors, erasure timing, and honest-memory noise.

The [related-work comparison](../references/RELATED_WORK.md) separates this finite statement from existing rate-one uncertainty results. The [verification suite](../verification/README.md) checks the matrix identities and finite examples used by the argument, not the cryptographic hardness assumption.

## Dependency map

Theorem G (finite guessing) uses Lemma D (discrimination), Lemma P (pure-state identity), the imported qubit hypercontractivity theorem HC, and an elementary rank inequality. Theorem C (cryptographic compilation) uses G plus the explicitly stated RSP simulation property. Theorem L (list acceptance) replaces D by its list version and reuses P and HC. The lower-bound witness is an independently specified strategy, not an assumption in these proofs.

The exact constant $1/6$ is sufficient, not asserted optimal. The optimal-order statement means that the required gap is bounded above and below by fixed multiples of $\log(1/\delta)$ in the exact-string ideal model. It does not extend unchanged to a fixed tolerated error fraction or to total hardware footprint.
