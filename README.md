# Lattice Memory Certification

## Question

Can lattice-based remote-state preparation let a classical verifier certify nearly all of a prover's retained quantum memory?

## Candidate finite-storage theorem

For independent uniform strings X and Θ in {0,1}^n, let the prover receive the BB84 product state |X⟩_Θ. Before Θ is disclosed, it may apply an arbitrary joint quantum instrument and retain unlimited classical information but at most m qubits of quantum memory, counting every surviving quantum system. After Θ is disclosed, it guesses the complete X.

The exploration's candidate bound is

`Pr[guess X correctly] ≤ 2^{-(n-m)/6}.`

**Verification status:** this is a research-stage claim, not an independently certified theorem. A self-contained proof with all instrument, conditional-normalization, and hypercontractivity steps is required.

## Conditional cryptographic application

Under the simulation hypotheses of the LWE-based *Proofs of Quantum Memory* protocol, the proposed ideal-storage estimate implies

`Pr[accept] ≤ ε_RSP + 2^{-(n-m)/6}.`

If ε_RSP ≤ ε/2, the ideal bound is at most ε for `n ≥ m + ceil(6 log_2(2/ε))`. Cryptographic efficiency and attainable simulation error are separate obligations. This is not an attack on deployed lattice cryptography.

## Lower-bound witness

Storing m qubits and measuring each remaining BB84 qubit in the Breidbart basis succeeds with probability `((1+1/sqrt(2))/2)^(n-m)`. Thus logarithmic additive overhead is necessary in order for this exact-string guessing model; the constants do not match.

## Scientific boundaries

The certified quantity is quantum storage retained through the waiting period, not quantum channel capacity. Exact recovery, error-tolerant recovery, losses, and noisy honest memories are distinct settings. Classical transcript storage is unrestricted; all retained quantum registers must be charged.

## Closest sources and verification plan

- LWE-based *Proofs of Quantum Memory*: https://arxiv.org/abs/2510.04159
- Earlier entropic-uncertainty / storage bounds: https://arxiv.org/abs/1305.1316
- Qubit hypercontractivity ingredient: https://arxiv.org/abs/1208.0161

Next: reconstruct the full proof, audit conditional quantum instruments, check the LWE hybrid and its efficiency, compare finite bounds and priority, and establish reproducible examples. Earlier work already approaches storage rate one; novelty concerns the finite additive overhead, subject to literature verification.

**Status:** active scientific research; not yet furnished or release-ready.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
