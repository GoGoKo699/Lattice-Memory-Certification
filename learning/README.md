# Learning guide

**Question:** what can a verifier conclude when a device must answer a quantum measurement chosen only after its storage has been restricted?

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. The [Watrous bridge](WATROUS_BRIDGE.md) identifies selected sections, translates notation, and supplies the steps that belong to this project rather than the textbook. It includes a complete two-input-qubit, one-stored-qubit example.

## Route through the project

For a continuous explanation, read the [explanatory report (PDF)](report/Lattice_Memory_Certification_Report.pdf). For structured study, use the bridge and milestone map below.

Read the [bridge's opening experiment](WATROUS_BRIDGE.md#the-experiment), then use the [30-milestone map](MILESTONES.md). M01–M14 build the objects and assumptions, ending with the complete storage experiment. M15–M30 assemble the finite bound, its conditional cryptographic use, and its limitations. Each milestone gives an understanding target, dependencies, a conceptual connection and authoritative source pointers. The map depends on the science, not a particular reader's background or progress.

For a direct specialist route, start with the [model](../science/model.md) and [proof](../science/guessing-bound.md). The [science guide](../science/README.md) connects those pages to the LWE reduction, lower-bound strategy, error and loss variants, and resource accounting. The learning pages explain the same contribution; they do not replace its exact statements.

## What the anchor supplies

The relevant foundations are finite-dimensional operators and norms, quantum states and channels, measurements, reduced states, Schmidt decompositions, and state discrimination. Watrous's Theorem 3.10 supplies the Barnum–Knill inequality used in the proof. [Selected sections and page references](WATROUS_BRIDGE.md#anchor-sections) are provided rather than assigning the entire book.

The tensor-power hypercontractivity theorem and the LWE-based remote-preparation guarantee are separate research dependencies. The bridge states their roles and links their primary sources. Neither is presented as a theorem in Watrous, and neither creates a second educational anchor.

## Destination

The route ends with the ability to connect a bounded retained quantum dimension to an exact-string guessing bound, explain why the ideal result has no cryptographic assumption, and identify the extra conditions needed for a classical verifier. It also distinguishes logarithmic overhead in the ideal exact-recovery model from an optimal constant, a noisy-hardware guarantee, or efficient negligible-soundness compilation.
