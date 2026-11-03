# Analytic memory-deficit figure

The [PDF](memory_deficit.pdf) and [PNG](memory_deficit.png) contain the same two-panel analytic figure. Panel (a) brackets optimal ideal exact-string success between the explicit store-and-Breidbart strategy and the universal upper bound. Panel (b) shows the necessary and sufficient integer deficits for an ideal target probability. The interval between the curves records the unresolved constants.

## Reproduce

From the repository root, use a separate plotting environment with the pins in [requirements.txt](requirements.txt):

```bash
python3 -m venv .venv-plots
.venv-plots/bin/python -m pip install -r verification/Graph/requirements.txt
OPENBLAS_NUM_THREADS=1 .venv-plots/bin/python verification/Graph/generate_plots.py
OPENBLAS_NUM_THREADS=1 .venv-plots/bin/python verification/Graph/check_plots.py
```

The generator writes `memory_deficit.pdf`, `memory_deficit.png` and `memory_deficit_data.json` in this directory. The JSON records every plotted value, the staircase breakpoints, dependency versions and PDF hash; it is generated output. The PDF has fixed metadata for deterministic reproduction. The PDF and PNG use the same labels and figure geometry.

To rebuild without replacing the committed preview:

```bash
OPENBLAS_NUM_THREADS=1 .venv-plots/bin/python verification/Graph/generate_plots.py --output-dir /tmp/lattice-memory-plot-check
OPENBLAS_NUM_THREADS=1 .venv-plots/bin/python verification/Graph/check_plots.py --output-dir /tmp/lattice-memory-plot-check
```

The checker compares the regenerated PDF with the committed PDF and the recorded reference hash. It uses `verification/verify.py`'s elementary examples to cross-check the constants, independently evaluates all probability and ceiling values with high-precision scalar arithmetic, checks every interior staircase boundary, and records source/asset hashes. It also checks the PDF/PNG geometry. These checks concern the figure and its data; they do not establish the universal theorem, computational hardness or hardware performance.

## Interpretation

For the missing-qubit gap $`t=n-m`$, panel (a) shows $`\beta^t\leq P^*_{n,m}\leq2^{-t/6}`$, with $`\beta=(1+1/\sqrt2)/2`$. The shading brackets the unknown optimum. It does not assert that all intermediate values are achievable.

For ideal target $`\delta=2^{-u}`$, panel (b) shows the necessary integer gap $`\lceil u/(-\log_2\beta)\rceil`$ and the sufficient gap $`\lceil6u\rceil`$. The endpoint $`u=0`$ is the trivial target one. At $`u=20`$, the thresholds are $`88`$ and $`120`$ qubits; at $`u=30`$, they are $`132`$ and $`180`$.

The total soundness target $`\varepsilon`$ of the classical-verifier protocol also includes preparation error. With equal error allocation, use preparation error at most $`\varepsilon/2`$ and sufficient gap $`\lceil6\log_2(2/\varepsilon)\rceil`$. Thus $`\varepsilon=2^{-20}`$ gives gap $`126`$, rather than the panel's ideal-target gap $`120`$. See the [conditional certification account](../../science/cryptographic-certification.md) and [storage-strategy account](../../science/lower-bounds-and-resources.md).
