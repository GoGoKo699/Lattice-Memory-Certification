# Lattice Memory Certification

**How many qubits must a prover retain to recover a hidden string after its measurement bases are revealed?**

For an arbitrary collective encoder, unlimited classical storage and a quantum memory of dimension at most $D$, this project proves a finite BB84 guessing bound:

```math
P_{\mathrm{guess}}\leq\min\left\{1,\left(\frac{D}{2^n}\right)^{1/6}\right\}.
```

For $m$ retained qubits, the exponent depends on the missing-qubit gap $n-m$, not on the total input size separately. Inserting this estimate into the existing LWE-based remote-state-preparation construction of Hhan, Morimae, Okinaka and Yamakawa gives a conditional classical-verification protocol with **logarithmic additive storage overhead**. This is a storage-certification result, not an attack on lattice cryptography.

## Principal results

| Result | Statement and scope | Authoritative account |
|---|---|---|
| Finite storage converse | $P_{\mathrm{guess}}\leq 2^{-(n-m)/6}$, including arbitrary collective processing and unlimited classical records | [Model](science/model.md), [proof](science/guessing-bound.md) |
| Conditional LWE compilation | $P_{\mathrm{accept}}\leq\varepsilon_{\mathrm{RSP}}+2^{-(n-m)/6}$, for the efficient adversaries covered by the imported simulation theorem | [Certification](science/cryptographic-certification.md) |
| Optimal order of overhead | A store-and-Breidbart-measure strategy succeeds with $\beta^{n-m}$, where $\beta=(1+1/\sqrt2)/2$ | [Lower bounds and resources](science/lower-bounds-and-resources.md) |
| List acceptance | Lists of size at most $L$ give $P_{\mathrm{list}}\leq\min\{1,\sqrt L\,2^{-(n-m)/6}\}$ | [Errors and losses](science/errors-and-losses.md) |
| Error and erasure boundaries | Exact recovery, tolerated errors, and pre- versus post-basis erasures have different storage guarantees | [Errors and losses](science/errors-and-losses.md) |

For total soundness error $\varepsilon$, preparation error at most $\varepsilon/2$ and

```math
n=m+\left\lceil6\log_2(2/\varepsilon)\right\rceil
```

suffice. The cited polynomial-hardness LWE construction supports this efficient compilation for **inverse-polynomial** $\varepsilon$; the formula alone does not establish efficient negligible-soundness compilation. Honest storage is $n$ logical qubits during the waiting period. Preparation, readout, classical communication and temporary quantum workspace are separate resources.

## Read the science

Start with the [science guide](science/README.md), then follow the [exact model](science/model.md), [complete finite-bound proof](science/guessing-bound.md), and [cryptographic reduction](science/cryptographic-certification.md). The [related-work account](references/RELATED_WORK.md) identifies inherited ingredients and compares a specific finite specialization of the earlier uncertainty bound. The [LLM reading map](llms.txt) points directly to the same authoritative files.

The elementary discrimination step is a Barnum–Knill inequality; the tensor-power hypercontractivity theorem is imported with explicit normalization. The contribution developed here is their rank-sensitive combination and its storage-certification consequence. Earlier work already permits storage rates approaching one. The present source comparison is not an exhaustive priority certificate.

## Reproduce finite checks

With Python 3.13:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 .venv/bin/python verification/verify.py
```

The [verification guide](verification/README.md) distinguishes analytical proof, finite matrix checks and untested cryptographic assumptions. The [stored report](verification/expected_results.json) records the actual cases and numerical errors.

## Consequential boundaries

The memory budget counts **every quantum system accessible after the storage cut**, including remote ancillas. Fresh, uncorrelated decoding workspace is allowed. The basis string must be hidden until after that cut. Accepting one run is not a deterministic measurement of memory size; the conclusion is a false-acceptance bound under a specified dimension hypothesis.

The ideal mathematical converse is unconditional. The classical-verifier realization is computational and inherits its LWE and simulation assumptions. A fixed positive physical error rate is not automatically compatible with exact-string completeness; allowing a fixed fraction of wrong answers also changes the storage requirement.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
