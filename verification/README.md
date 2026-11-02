# Verification and reproduction

The analytical proofs are in the [science guide](../science/README.md). This suite provides deterministic finite checks for consequential normalization, support, and implementation errors. It does not establish general mathematical or computational-hardness claims by sampling.

## Environment and command

The recorded run used Python 3.13.5 and NumPy 2.3.5. From the repository root:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 .venv/bin/python verification/verify.py
OPENBLAS_NUM_THREADS=1 .venv/bin/python verification/check_learning.py
```

To save a new report without replacing the committed reference:

```bash
OPENBLAS_NUM_THREADS=1 .venv/bin/python verification/verify.py --write /tmp/lattice-memory-results.json
```

The only numerical dependency is pinned in [requirements.txt](requirements.txt). [verify.py](verify.py) uses a fixed seed, raises an exception on any failed assertion, and prints JSON on success. [expected_results.json](expected_results.json) is the stored output, not a claim of an independently reproduced run. Floating-point residuals can differ slightly across numerical libraries; each assertion uses absolute tolerance $`2\times10^{-10}`$.

## What is checked

The suite generates 112 pure conditional states for one through four Alice qubits, with several memory dimensions including a non-power-of-two dimension, rank-deficient states, flat spectra and nonuniform spectra. It compares the explicit conditional-state PGM probability against the square-root marginal identity for all BB84 bases. The resulting 1,000 basis cases also test sampled decoder POVMs, list-score effects, and matrix normalization. Where available, scalar and two-outcome Helstrom optima are checked exactly rather than replaced by a random decoder.

Pauli-basis sums are computed independently from those conditional ensembles. They verify the averaged quadratic identity, depolarizing domination, the finite hypercontractive inequality, and the rank estimate. These are sample checks of the imported theorem, not a new proof of it.

Twenty-seven trace-preserving instruments are built from independent random isometries. Direct preparation-and-measurement probabilities are compared with the delayed-EPR-measurement calculation, including nonuniform classical branch weights. This checks that conditional normalization and averaging have not silently changed the experiment.

The elementary tests cover perfect full-memory readout, the one-qubit Breidbart probabilities, product witness versus converse, Hamming-list acceptance, the certain-success counterexample when all missing bits may be wrong, and the stated finite comparison with DFW Corollary 11. Local Markdown path checks detect missing files; they do not validate web links or hosted equation rendering.

## Proof and review boundary

The finite theorem is supported by the complete analytical chain: classical pure-state refinement, a proved finite discrimination inequality, a proved Schmidt identity, a Pauli comparison, the explicitly imported tensor-power hypercontractivity theorem, and a rank inequality. The cryptographic corollary imports the precise RSP simulation interface and proves the memory-preserving reduction separately.

No code here runs LWE cryptography, estimates cryptanalytic security, optimizes all encoders or all joint decoders, simulates fault-tolerant hardware, or certifies the scientific claims through independent peer review. The source comparison is not exhaustive. Hosted mathematical rendering is a separate presentation check, not established by these numerical or local-link tests.

## Learning and repository structure checks

[check_learning.py](check_learning.py) verifies the exact M01–M30 sequence, the 14/16 phase allocation, the required understanding-target fields and backward-only dependencies. It checks relative Markdown destinations including heading fragments and the presence of the selected Watrous (2018) anchor. Anchor uniqueness, the local-to-global story, and independence from personal coaching require manual review. The script also evaluates the bridge's two-input-qubit, one-stored-qubit strategy directly, including both classical branches and all four basis strings. These checks do not assess a reader or replace scientific proof review.

Run `python verification/check_learning.py --write /tmp/lattice-learning-results.json` to save a fresh report. [learning_results.json](learning_results.json) is the recorded output. Like the original suite, this check uses the pinned NumPy dependency and a numerical tolerance of 2e-10.

## Explanatory report reproduction

The [report build guide](REPORT_BUILD.md) gives the source path, a clean build command, and the engine and inspection boundaries. The stored PDF is distinct from the fresh output and matching log produced by that command.

## Mathematical display review boundary

Balanced math delimiters, local heading checks and finite calculations do not establish correct display on GitHub. Actual-host review compares commit-pinned equations with their source and inspects wide and narrow layouts, including tables. It is a separate presentation check from the analytical proof, local link tests, and PDF build. The `hosted_rendering` field in the learning script reports only what that script itself checks.
