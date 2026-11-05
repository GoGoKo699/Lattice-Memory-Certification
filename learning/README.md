# Learning guide

**Question:** what can a verifier conclude when a device must answer a quantum measurement chosen only after its storage has been restricted?

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. The [Watrous bridge](WATROUS_BRIDGE.md) identifies selected sections, translates notation, and supplies the steps that belong to this project rather than the textbook. It includes a complete two-input-qubit, one-stored-qubit example.

## Route through the project

For a continuous explanation, read the [explanatory report (PDF)](report/Lattice_Memory_Certification_Report.pdf). For structured study, use the bridge and milestone map below.

Read the [bridge's opening experiment](WATROUS_BRIDGE.md#the-experiment), then use the [30-milestone map](MILESTONES.md). M01–M14 build the objects and assumptions, ending with the complete storage experiment. M15–M30 assemble the finite bound, its conditional cryptographic use, acceptance-rule limits and noisy-processing application. Each milestone gives an understanding target, dependencies, a conceptual connection and authoritative source pointers. The map depends on the science, not a particular reader's background or progress.

For a direct specialist route, start with the [model](../science/model.md) and [proof](../science/guessing-bound.md), then the [rank-sensitive three-input refinement](../science/finite-guessing.md). The latter proves a stronger certified finite bound and identifies why the collision-only route cannot improve the universal exponent. The [science guide](../science/README.md) connects those pages to the LWE reduction, lower-bound strategy, error and loss variants, and resource accounting. The learning pages explain the same contribution; they do not replace its exact statements.

## What the anchor supplies

The relevant foundations are finite-dimensional operators and norms, quantum states and channels, measurements, reduced states, Schmidt decompositions, and state discrimination. Watrous's Theorem 3.10 supplies the Barnum–Knill inequality used in the proof. [Selected sections and page references](WATROUS_BRIDGE.md#anchor-sections) are provided rather than assigning the entire book.

The rank-sensitive finite chapter adds a two-copy purity constraint and uses Renes's sharper finite-alphabet discrimination inequality. Its exact $`9/16`$ PGM bound gives $`P^*_{3,1}\leq(2+7\sqrt2)/16`$, while the all-size exponent remains $`1/6`$. The finite certificate, its moment-profile composition, and the Hamming-ball limitation of the collision-only method have separate proof scopes; no joint-encoder tensorization is assumed.

The [direct-discrimination study](../science/direct-discrimination.md) adds exact fixed-encoder decoder certificates and an analytic diagonal-dual limitation. Its finite values improve neither the global three-input bound nor the uniform exponent.

The tensor-power hypercontractivity theorem and the LWE-based remote-preparation guarantee are separate research dependencies. The bridge states their roles and links their primary sources. Neither is presented as a theorem in Watrous, and neither creates a second educational anchor.

For the [connection to Measurement-Free Memory Cost](../science/noisy-processing.md), use the [bridge's temporal-cut explanation](WATROUS_BRIDGE.md#from-a-storage-cut-to-a-processing-witness). Both projects use Watrous (2018) as their single educational anchor, with different source-to-project routes. The companion owns the full Pauli-factorization and processing-ledger derivation, including the exponential-moment estimate that retains actual noise probabilities; this repository supplies the finite guessing theorem and the operational interpretation.

## Destination

The route ends with the ability to connect a bounded retained quantum dimension to an exact-string guessing bound, explain why the ideal result has no cryptographic assumption, and identify the extra conditions needed for a classical verifier. It also identifies when a score can supply all-cut rank and moment premises for a noisy-processing budget, and why that consequence neither verifies the device assumptions nor creates a new LWE processing test. The ideal guessing target $`\delta`$, total compiled false-acceptance target $`\varepsilon`$, physical-noise model and charged resources retain their separate meanings.

