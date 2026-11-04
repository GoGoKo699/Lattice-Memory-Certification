# Thirty milestones

[Learning guide](README.md) · [Watrous bridge](WATROUS_BRIDGE.md) · [Science guide](../science/README.md)

This is the project's common understanding map, independent of any reader's background or assessment history. The single educational anchor is **Watrous, The Theory of Quantum Information (2018)**; the [bridge](WATROUS_BRIDGE.md#anchor-sections) identifies the exact sections and the research ingredients supplied outside the book.

The allocation is **14 background/preliminary milestones and 16 narrative/innovation milestones**. The background needs both quantum-information objects and the computational-preparation interface before the complete experiment can be understood. The narrative then builds the proof locally, connects it to a physical strategy and existing work, and assembles the conditional certification result and its noisy-processing application with their resource boundaries. Each phase ends in a synthesis. “Narrative/innovation” describes the project story; it does not label inherited lemmas or derived corollaries as new discoveries.

Dependencies name earlier understanding targets, not extra assignments. Primary scientific pages remain authoritative for exact assumptions and proofs. This map provides global understanding of the bounded contribution, not every technical detail of quantum information or lattice cryptography.

## Background and preliminaries

### M01: Qubit states and bases

**Phase:** Background/preliminaries.

**Central question:** What changes when the same bit is encoded in a different basis?

**Understanding target:** Explain the four BB84 states $`\mathsf H^\theta|x\rangle`$, with $`x,\theta\in\{0,1\}`$ and Hadamard operator $`\mathsf H`$, and distinguish a bit value from the basis used to encode it.

**Dependencies:** None.

**Story role:** Introduce one input before considering a stored collection.

**Conceptual connection:** Incompatible bases make the later basis announcement operationally important.

**Source pointers:** Watrous §§1.1.1–1.1.2 and 2.1.2; [experiment](WATROUS_BRIDGE.md#the-experiment); [source model](../science/model.md#registers-and-chronology).

### M02: Mixtures and hidden labels

**Phase:** Background/preliminaries.

**Central question:** Why is a hidden state label different from an unknown pure state vector?

**Understanding target:** Distinguish an ensemble, its averaged density operator, and the verifier’s classical record; explain why averaging a uniformly encoded bit hides its basis.

**Dependencies:** M01.

**Story role:** Connect preparation randomness to what the device actually receives.

**Conceptual connection:** The averaged input and the joint state with verifier labels answer different questions.

**Source pointers:** Watrous §§1.2.2 and 2.1.1–2.1.2; [source model](../science/model.md#registers-and-chronology).

### M03: Registers and quantum dimension

**Phase:** Background/preliminaries.

**Central question:** What does retaining $`m`$ qubits constrain?

**Understanding target:** Translate qubit counts to dimensions and count the joint dimension of every later-accessible quantum system, rather than a named local register alone.

**Dependencies:** M01, M02.

**Story role:** Extend individual states to compound systems.

**Conceptual connection:** A physical storage restriction becomes the dimension parameter $`D`$, while classical record size is separate.

**Source pointers:** Watrous §§1.1.1 and 2.1.1–2.1.2; [normalization and notation](WATROUS_BRIDGE.md#notation-and-normalization); [resource accounting](../science/lower-bounds-and-resources.md#4-charged-resources).

### M04: Measurements and subnormalized ensembles

**Phase:** Background/preliminaries.

**Central question:** Where are outcome probabilities stored in the proof’s matrices?

**Understanding target:** Read a POVM effect as a possible outcome and explain why the trace of a subnormalized conditional operator is already its label probability.

**Dependencies:** M02, M03.

**Story role:** Turn states into experimentally scored outcomes.

**Conceptual connection:** Correct probability weighting is necessary before any discrimination inequality can be applied.

**Source pointers:** Watrous §§2.3.1–2.3.2 and 3.1.2; [notation bridge](WATROUS_BRIDGE.md#notation-and-normalization); [Lemma D](../science/guessing-bound.md#2-lemma-d-discrimination-through-the-square-root-measurement).

### M05: Channels and quantum instruments

**Phase:** Background/preliminaries.

**Central question:** How can an encoder produce both a classical record and a smaller quantum memory?

**Understanding target:** Describe an instrument as outcome-labelled completely positive maps whose sum preserves trace; distinguish its classical outcome from its quantum output.

**Dependencies:** M03, M04.

**Story role:** Supply a model broad enough for arbitrary joint preprocessing.

**Conceptual connection:** Measurement, coherent processing and discarding fit within one encoder contract.

**Source pointers:** Watrous §§2.2.1–2.2.2 and 2.3.1–2.3.2; [encoder contract](../science/model.md#registers-and-chronology).

### M06: Classical and quantum side information

**Phase:** Background/preliminaries.

**Central question:** Why does unlimited classical information not mean unlimited quantum storage?

**Understanding target:** Condition on a classical branch without introducing an uncharged quantum reference; identify which ancillas persist across the storage cut.

**Dependencies:** M03, M05.

**Story role:** Make the permitted adversary’s information explicit.

**Conceptual connection:** A classical branch label can be freely supplied in an upper bound while a purification cannot.

**Source pointers:** Watrous §§2.1.1–2.1.3; [model](../science/model.md#registers-and-chronology); [classical refinement](../science/guessing-bound.md#1-classical-refinement-without-extra-quantum-memory).

### M07: Reduced states and Schmidt rank

**Phase:** Background/preliminaries.

**Central question:** When does a small memory force a low-rank marginal?

**Understanding target:** Use the Schmidt decomposition for a pure bipartite state and explain why its marginal rank is the Schmidt rank $`r\leq D`$; give the mixed-state limitation.

**Dependencies:** M03, M06.

**Story role:** Identify the dimension-sensitive object that the proof can legitimately bound.

**Conceptual connection:** Pure-state rank connects a storage budget to eigenvalue inequalities.

**Source pointers:** Watrous §1.1.3, p. 31, and §2.1.3; [refinement and rank](../science/guessing-bound.md#1-classical-refinement-without-extra-quantum-memory).

### M08: Delayed EPR measurement

**Phase:** Background/preliminaries.

**Central question:** Why can the preparation experiment be analysed by measuring half of an entangled state later?

**Understanding target:** Explain how an EPR pair and a delayed measurement in a real BB84 basis reproduce the supplied state and its labels without granting the prover the labels.

**Dependencies:** M01, M05, M07.

**Story role:** Relate a physical preparation task to a bipartite mathematical model.

**Conceptual connection:** Commuting operations on separate registers allow the storage cut to precede the verifier’s measurement in the analysis.

**Source pointers:** Watrous §§1.1.1–1.1.2 and 2.1.3; [stronger formulation](../science/model.md#stronger-premeasurement-formulation); [worked example](WATROUS_BRIDGE.md#a-complete-two-qubit-example).

### M09: Optimal guessing as a task

**Phase:** Background/preliminaries.

**Central question:** What exactly is being optimized by the decoder?

**Understanding target:** Distinguish guessing one bit, the whole string, and an allowed list; express exact-string success as an ensemble-discrimination probability.

**Dependencies:** M04, M06, M08.

**Story role:** Define the operational quantity before bounding it.

**Conceptual connection:** The acceptance rule, not the entropy notation alone, determines the memory claim.

**Source pointers:** Watrous §§3.1.1–3.1.2; [Theorem G](../science/model.md#theorem-g-finite-dimensional-guessing); [Theorem L](../science/model.md#theorem-l-lists).

### M10: The square-root measurement

**Phase:** Background/preliminaries.

**Central question:** How can a specified measurement constrain the best possible measurement?

**Understanding target:** Identify the ensemble average and its support inverse in the pretty-good measurement, and state the direction of the Barnum–Knill comparison.

**Dependencies:** M04, M09.

**Story role:** Introduce a tractable measurement quantity without assuming it is optimal.

**Conceptual connection:** The square of optimal guessing is at most square-root-measurement success, enabling a quadratic proof.

**Source pointers:** Watrous §3.1.2, pp. 137–139, Theorem 3.10; [Lemma D](../science/guessing-bound.md#2-lemma-d-discrimination-through-the-square-root-measurement).

### M11: Spectral powers and trace conventions

**Phase:** Background/preliminaries.

**Central question:** Why can a missing dimension factor change the conclusion?

**Understanding target:** Translate ordinary Schatten norms to $`\|A\|_{p,\mathrm{n}}=d^{-1/p}\|A\|_p`$ and interpret fractional powers and support inverses through eigenvalues.

**Dependencies:** M07, M10.

**Story role:** Prepare the normalization and rank calculations.

**Conceptual connection:** The factor $`d^{-1/3}`$ comes from normalized trace, not a physical noise parameter.

**Source pointers:** Watrous §1.1.3; [notation and normalization](WATROUS_BRIDGE.md#notation-and-normalization); [HC convention](../science/guessing-bound.md#5-imported-theorem-hc-and-the-rank-estimate).

### M12: Pauli coordinates for averaged measurements

**Phase:** Background/preliminaries.

**Central question:** How does randomly selecting a basis become a channel acting on operators?

**Understanding target:** Explain dephasing, its average over the two bases, and the $`\mathsf X,\mathsf Y,\mathsf Z`$ Pauli weights that let a tensor-product quadratic form be compared term by term.

**Dependencies:** M01, M05, M11.

**Story role:** Link the measurement experiment to the operator structure used by the proof.

**Conceptual connection:** Basis randomness produces an averaging map; it is not assumed to be uncontrolled physical noise.

**Source pointers:** Watrous §§1.1.2 and 2.2.3; [Pauli quadratic form](../science/guessing-bound.md#4-bb84-averaging-as-a-pauli-quadratic-form).

### M13: Computational preparation and soundness

**Phase:** Background/preliminaries.

**Central question:** Which additional assumption allows a verifier with only classical communication to supply the test?

**Understanding target:** Distinguish the ideal quantum-input task from the LWE-based preparation interface, and distinguish completeness from a false-acceptance bound against efficient provers.

**Dependencies:** M05, M06, M09.

**Story role:** Introduce the cryptographic layer without mixing it into the ideal inequality.

**Conceptual connection:** Computational simulation supplies an input resource; it does not establish the information-theoretic bound.

**Source pointers:** Watrous §§2.2 and 3.1 for channel and operational language; [project-supplied cryptographic bridge](WATROUS_BRIDGE.md#from-ideal-inputs-to-a-classical-verifier); [RSP interface](../science/cryptographic-certification.md#1-imported-simulation-interface).

### M14: Assemble the complete experiment

**Phase:** Background/preliminaries.

**Central question:** What must remain hidden, and what may be retained, at each stage?

**Understanding target:** Trace preparation, joint encoding, the storage cut, basis disclosure and decoding, with all registers and assumptions accounted for.

**Dependencies:** M01, M02, M03, M04, M05, M06, M07, M08, M09, M10, M11, M12, M13.

**Story role:** Synthesize the background into one operational model.

**Conceptual connection:** The same chronology links state discrimination, a finite dimension restriction and a conditional classical-verifier implementation.

**Source pointers:** Watrous §§2.1–2.3 and 3.1; [model and principal statements](../science/model.md); [bridge](WATROUS_BRIDGE.md).

## Narrative and innovation

### M15: Refine into pure classical branches

**Phase:** Narrative/innovation.

**Central question:** How can the proof use Schmidt rank without granting extra quantum memory?

**Understanding target:** Explain the pure-state decomposition after conditioning on C, why its label can be given classically, and why the independent basis distribution is unchanged.

**Dependencies:** M06, M07, M08, M14.

**Story role:** Start the new argument at its first dimension-sensitive reduction.

**Conceptual connection:** Classical refinement turns an arbitrary mixed strategy into a family of pure-state bounds that can be averaged.

**Source pointers:** Watrous §§1.2.1 and 2.1.3; [proof step 1](../science/guessing-bound.md#1-classical-refinement-without-extra-quantum-memory).

### M16: Bound discrimination without optimizing the decoder

**Phase:** Narrative/innovation.

**Central question:** Where does the first square-root loss enter?

**Understanding target:** Follow the Hilbert–Schmidt Cauchy–Schwarz bound and explain why positivity and POVM normalization make its second factor at most one.

**Dependencies:** M10, M11, M15.

**Story role:** Apply an inherited discrimination theorem to every conditional branch.

**Conceptual connection:** A bound on a fixed square-root measurement controls arbitrary collective decoding.

**Source pointers:** Watrous §3.1.2, Theorem 3.10; [Lemma D](../science/guessing-bound.md#2-lemma-d-discrimination-through-the-square-root-measurement).

### M17: Identify the pure-state quadratic expression

**Phase:** Narrative/innovation.

**Central question:** Why does the square root of the verifier’s marginal appear?

**Understanding target:** Derive the conditional vectors from a Schmidt decomposition and connect their support-inverse overlaps to diagonal entries of the square-root marginal.

**Dependencies:** M07, M11, M16.

**Story role:** Convert an operational probability into the operator expression the proof can analyse.

**Conceptual connection:** The ensemble includes its own outcome weights, so no uniform-conditional-outcome assumption is needed.

**Source pointers:** Watrous §§1.1.3 and 2.1.3; [Lemma P](../science/guessing-bound.md#3-lemma-p-the-pure-state-identity); [two-qubit example](WATROUS_BRIDGE.md#a-complete-two-qubit-example).

### M18: Average over every basis string

**Phase:** Narrative/innovation.

**Central question:** Why does the measurement average factor into tensor powers?

**Understanding target:** Use independent uniform basis choices to identify the exact averaged quadratic form and distinguish this independence from an independence assumption on the encoder.

**Dependencies:** M12, M17.

**Story role:** Move from a single conditional basis experiment to the full block.

**Conceptual connection:** Product measurement choices coexist with arbitrary entanglement and joint processing.

**Source pointers:** Watrous §§1.1.1–1.1.2 and 2.2.3; [BB84 averaging](../science/guessing-bound.md#4-bb84-averaging-as-a-pauli-quadratic-form).

### M19: Compare with depolarization

**Phase:** Narrative/innovation.

**Central question:** What kind of ordering is sufficient for the proof?

**Understanding target:** Compare Pauli-word weights, explain the depolarizing square-root parameter, and avoid interpreting quadratic-form domination as complete-positive map ordering.

**Dependencies:** M11, M12, M18.

**Story role:** Reach an operator family with a usable tensor-power norm theorem.

**Conceptual connection:** The comparison preserves the input dimension instead of bounding each qubit separately.

**Source pointers:** Watrous §2.2.3 for channel examples; [depolarizing comparison](../science/guessing-bound.md#4-bb84-averaging-as-a-pauli-quadratic-form).

### M20: Use hypercontractivity and rank

**Phase:** Narrative/innovation.

**Central question:** How does the finite memory dimension enter the exponent?

**Understanding target:** State the imported inequality for $`\|\cdot\|_{p,\mathrm{n}}`$ at $`p=3/2`$, $`q=2`$, and $`\eta=1/\sqrt2`$, carry through its dimension factor, and bound the eigenvalue sum using Schmidt rank $`r`$.

**Dependencies:** M07, M11, M15, M19.

**Story role:** Obtain the central deficit-sensitive estimate on averaged square-root-measurement success.

**Conceptual connection:** Hypercontractivity and the pure-branch rank bound yield $`(r/d)^{1/3}`$ before the final square root.

**Source pointers:** Watrous §1.1.3 for norms; [imported HC and rank estimate](../science/guessing-bound.md#5-imported-theorem-hc-and-the-rank-estimate); [primary attribution](../references/RELATED_WORK.md#m12-hypercontractivity).

### M21: Complete the finite guessing theorem

**Phase:** Narrative/innovation.

**Central question:** Why does the final result depend on $`n-m`$?

**Understanding target:** Combine discrimination, averaging and rank, recover the bound for mixed classical branches, and identify the trivial full-memory endpoint.

**Dependencies:** M15, M16, M17, M18, M19, M20.

**Story role:** Synthesize the complete ideal converse.

**Conceptual connection:** The ratio $`D/d`$ becomes the memory deficit in the exponent without an asymptotic remainder.

**Source pointers:** Watrous §§1.2.1–1.2.2 and 3.1.2; [finish Theorem G](../science/guessing-bound.md#6-finish-theorem-g); [statement](../science/model.md#theorem-g-finite-dimensional-guessing).

### M22: Construct a lower-bound strategy

**Phase:** Narrative/innovation.

**Central question:** What prevents the additive overhead from having a better asymptotic order?

**Understanding target:** Explain storing $`m`$ qubits and Breidbart-measuring the rest, derive the achieved complete-string probability $`\beta^{n-m}`$, and distinguish optimal order from an optimal constant.

**Dependencies:** M01, M09, M14, M21.

**Story role:** Test the consequence of the converse against an explicit physical strategy.

**Conceptual connection:** For ideal guessing target $`\delta`$, the witness and converse bracket the required missing-qubit gap by fixed multiples of $`\log_2(1/\delta)`$.

**Source pointers:** Watrous §§2.3 and 3.1; [lower witness and overhead](../science/lower-bounds-and-resources.md); [worked example](WATROUS_BRIDGE.md#a-complete-two-qubit-example).

### M23: Locate the finite improvement

**Phase:** Narrative/innovation.

**Central question:** What is added beyond previously known storage rates approaching one?

**Understanding target:** Explain the particular DFW dimension specialization, compare finite sufficient gaps, and keep the limited comparison separate from a general priority claim.

**Dependencies:** M21, M22.

**Story role:** Place the established theorem in its scientific context.

**Conceptual connection:** A deficit-only finite statement and a near-unit asymptotic storage rate are related but different claims.

**Source pointers:** Watrous §3.1 for the guessing task; [DFW comparison](../references/RELATED_WORK.md#dfw15-finite-comparison); [finite table](../science/lower-bounds-and-resources.md#3-finite-comparison-with-an-earlier-uncertainty-relation).

### M24: Specify the preparation simulator

**Phase:** Narrative/innovation.

**Central question:** What does the cryptographic simulation guarantee actually compare?

**Understanding target:** Identify the simulator’s quantum input and output flag, exclude classical access to hidden labels, and explain the joint pass-and-accept probability guarantee.

**Dependencies:** M13, M14, M21.

**Story role:** Start the operational compilation from its exact imported interface.

**Conceptual connection:** Computational simulation is not unconditional trace-distance approximation to every malicious state.

**Source pointers:** Watrous §2.2 for composing operations; [RSP interface](../science/cryptographic-certification.md#1-imported-simulation-interface); [primary source](../references/RELATED_WORK.md#hmoy25-and-z25-classical-preparation).

### M25: Preserve the storage cut in the hybrid

**Phase:** Narrative/innovation.

**Central question:** Why can the ideal bound still apply after inserting a simulator?

**Understanding target:** Compose simulation with the actual encoder, charge every retained quantum output, and bound pass-and-correct without dividing by pass probability.

**Dependencies:** M05, M06, M21, M24.

**Story role:** Connect cryptographic indistinguishability to the information-theoretic converse.

**Conceptual connection:** The simulator may use temporary workspace before the cut without creating free quantum memory after it.

**Source pointers:** Watrous §2.2 for channel composition; [proof of Theorem C](../science/cryptographic-certification.md#3-proof-of-theorem-c).

### M26: Allocate the soundness budget

**Phase:** Narrative/innovation.

**Central question:** Which parameter choices give an efficient classical-verifier protocol?

**Understanding target:** Allocate total false-acceptance budget $`\varepsilon`$ between preparation error $`\varepsilon_{\mathrm{RSP}}\leq\varepsilon/2`$ and ideal guessing target $`\delta=\varepsilon/2`$, derive $`n=m+\lceil6\log_2(2/\varepsilon)\rceil`$, and retain the inverse-polynomial versus negligible distinction.

**Dependencies:** M22, M25.

**Story role:** Translate the reduction into a finite resource consequence.

**Conceptual connection:** An algebraically sufficient error budget is not itself an efficient construction of the preparation protocol.

**Source pointers:** Watrous §1.2.2 for probability bounds; [efficient corollary](../science/cryptographic-certification.md#4-efficient-inverse-polynomial-corollary); [resource table](../science/lower-bounds-and-resources.md#4-charged-resources).

### M27: Generalize the acceptance score to lists

**Phase:** Narrative/innovation.

**Central question:** How does accepting several candidate strings change the proof?

**Understanding target:** Construct the list effects, explain their summed normalization bound, and obtain the square-root-of-list-size penalty without assuming a particular decoder.

**Dependencies:** M04, M16, M21.

**Story role:** Expose a controlled extension of the exact-string task.

**Conceptual connection:** Changing the score changes the discrimination factor while preserving the same hypercontractive estimate.

**Source pointers:** Watrous §§2.3 and 3.1.2; [list discrimination](../science/errors-and-losses.md#1-lemma-dl-list-discrimination); [Theorem L](../science/model.md#theorem-l-lists).

### M28: Interpret errors and erasure timing

**Phase:** Narrative/innovation.

**Central question:** Which departures from exact recovery preserve the claimed memory guarantee?

**Understanding target:** Relate Hamming tolerance $`h`$ to the list size $`V(n,h)=\sum_{j=0}^h\binom nj`$, explain the certain-success counterexample, distinguish pre-basis from post-basis erasures, and track honest noise separately.

**Dependencies:** M08, M22, M26, M27.

**Story role:** Use the extension to delimit physically different tests.

**Conceptual connection:** Accepted errors and adaptive erasures alter soundness, while honest physical errors also affect completeness.

**Source pointers:** Watrous §§1.2.2 and 2.3 for probabilities and measurements; [errors and losses](../science/errors-and-losses.md).

### M29: A guessing score as a processing premise

**Phase:** Narrative/innovation.

**Central question:** What additional device assumptions let a guessing score constrain continuing processing?

**Understanding target:** Translate the ideal theorem into the quantum-plus-classical factor of a sampled Pauli algebra, preserve the full-output terminal reserve, and average branchwise bounds to obtain an expected-rank floor at every cut. Then explain how the actual noise probabilities contract an exponential rank moment and how a fixed recovery supplies its all-cut floor. Separate challenge length, total noisy persistent width, noise rounds, endpoint decoding and charged controller processing.

**Dependencies:** M05, M06, M14, M21, M23, M26, M28.

**Story role:** Connect the finite guessing theorem to a dynamical application before final synthesis.

**Conceptual connection:** Existing recovery reductions imply both convenient mean-rank floors. Retaining the actual noise probabilities in a logarithmic moment then strengthens the dynamical ledger; its interval reserve must control that moment rather than only the mean. The transfer assumes independent noise and an honestly charged fixed controller model; a score does not test those premises or automatically compose with the LWE wrapper.

**Source pointers:** Watrous §§2.2–2.3, 3.1.2 and 3.2; [noisy-processing application](../science/noisy-processing.md); [complete companion proof](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/main/science/guessing_processing.md); [moment theorem](https://github.com/GoGoKo699/Measurement-Free-Memory-Cost/blob/8915a7afc3b891bda5e60438ec5182acf4181310/science/moment_processing.md); [resources](../science/lower-bounds-and-resources.md#4-charged-resources).

### M30: Synthesize the complete contribution

**Phase:** Narrative/innovation.

**Central question:** What is the full claim, and under exactly which assumptions does each part hold?

**Understanding target:** Explain the ideal theorem, conditional LWE compilation, logarithmic-order lower witness, acceptance-rule limitations and noisy-processing application as one connected account with their distinct assumptions. Distinguish analytical proof, finite tests, cryptographic hardness and unverified device premises.

**Dependencies:** M21, M22, M23, M24, M25, M26, M27, M28, M29.

**Story role:** End the narrative with a global understanding of the established contribution.

**Conceptual connection:** A rank-sensitive uncertainty bound gives different operational consequences through different interfaces: retained-dimension certification, conditional classical preparation and a model-dependent continuing-processing witness. Neither an accepted run nor a finite test is a deterministic count or complete capability certificate.

**Source pointers:** Watrous foundations via the [bridge](WATROUS_BRIDGE.md); [science synthesis](../science/README.md); [principal statements](../science/model.md); [noisy processing](../science/noisy-processing.md); [verification scope](../verification/README.md).

