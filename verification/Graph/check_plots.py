#!/usr/bin/env python3
"""Check analytic plot values, integer thresholds and packaged asset identity."""
from __future__ import annotations

import argparse
from decimal import Decimal, ROUND_CEILING, localcontext
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import re
import struct
import sys

import matplotlib
import numpy as np


HERE = Path(__file__).resolve().parent
PACKAGED_PDF_SHA256 = "6c59611929f0cbfe40c4e301b314a8c87d4e3f05dc0adb763a71295be3445aad"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(actual: float, expected: float, message: str) -> None:
    require(math.isfinite(actual) and math.isclose(actual, expected, rel_tol=5e-13,
                                                   abs_tol=0.0), message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_examples() -> tuple[dict, dict]:
    path = HERE.parent / "verify.py"
    spec = importlib.util.spec_from_file_location("lattice_numerical_checks", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    audit = module.Audit()
    return module.elementary_checks(audit), audit.counts


def check_values(data: dict, examples: dict) -> dict:
    constants = data["constants"]
    close(constants["beta"], examples["breidbart_beta"], "canonical beta mismatch")
    close(constants["necessary_gap_coefficient"], examples["necessary_gap_coefficient"],
          "canonical necessary-gap coefficient mismatch")
    require(constants["sufficient_gap_coefficient"] == examples["sufficient_gap_coefficient"] == 6,
            "canonical sufficient-gap coefficient mismatch")

    with localcontext() as context:
        context.prec = 60
        two = Decimal(2)
        beta = (1 + 1 / two.sqrt()) / 2
        rate = -beta.ln() / two.ln()
        close(constants["minus_log2_beta"], float(rate), "strategy exponent mismatch")
        a = data["panel_a"]
        require(a["missing_qubits_t"] == list(range(121)), "unexpected deficit range")
        upper, achieved = a["universal_upper_bound"], a["explicit_store_and_measure_success"]
        require(len(upper) == len(achieved) == 121, "probability array length mismatch")
        for t, hi, lo in zip(a["missing_qubits_t"], upper, achieved, strict=True):
            close(hi, float(two ** (-Decimal(t) / 6)), f"upper bound at t={t}")
            close(lo, float(beta ** t), f"strategy at t={t}")
            require(0 < lo <= hi <= 1, f"probability ordering at t={t}")
        close(upper[120], 2**-20, "ideal 120-qubit gap endpoint")

        b = data["panel_b"]
        require(b["target_denominator"] == 100 and b["target_numerator"] == list(range(3001)),
                "unexpected target-strength grid")
        fields = [b["target_strength_log2_inverse_delta"], b["necessary_integer_gap"],
                  b["sufficient_integer_gap"]]
        require(all(len(v) == 3001 for v in fields), "threshold array length mismatch")
        for j, (u, necessary, sufficient) in enumerate(zip(*fields, strict=True)):
            target = Decimal(j) / 100
            require(u == float(target), f"target strength at index {j}")
            require(necessary == int((target / rate).to_integral_value(rounding=ROUND_CEILING)),
                    f"necessary ceiling at u={u}")
            require(sufficient == int((6 * target).to_integral_value(rounding=ROUND_CEILING)),
                    f"sufficient ceiling at u={u}")
        require((fields[1][2000], fields[2][2000]) == (88, 120), "u=20 thresholds")
        require((fields[1][3000], fields[2][3000]) == (132, 180), "u=30 thresholds")

        # Check every analytic jump used to draw the ceiling staircases.
        # At an interior jump x=k*c, ceil(x/c)=k, while immediately above it
        # the threshold is k+1. The final endpoint can truncate the last step.
        boundary_checks = 0
        for name, spacing in (("necessary", rate), ("sufficient", Decimal(1) / 6)):
            xs = b[f"plotted_{name}_breakpoints_u"]
            ys = b[f"plotted_{name}_gap"]
            last = int((Decimal(30) / spacing).to_integral_value(rounding=ROUND_CEILING))
            require(ys == list(range(last + 1)) and len(xs) == len(ys),
                    f"{name} staircase length")
            require(xs[0] == 0 and xs[-1] == 30, f"{name} staircase endpoints")
            for k in range(1, last):
                boundary = spacing * k
                close(xs[k], float(boundary), f"{name} jump location {k}")
                require(xs[k - 1] < xs[k] < xs[k + 1], f"{name} jump order {k}")
                # Evaluating infinitesimally to either side checks the ceiling
                # orientation without relying on a rounded float at the jump.
                offset = spacing / Decimal(10**8)
                lower = int(((boundary - offset) / spacing).to_integral_value(rounding=ROUND_CEILING))
                upper = int(((boundary + offset) / spacing).to_integral_value(rounding=ROUND_CEILING))
                require(lower == k and upper == k + 1, f"{name} jump orientation {k}")
                boundary_checks += 1
    return {"probability_pairs": 121, "target_strengths": 3001,
            "interior_ceiling_boundaries": boundary_checks}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=HERE,
                        help="Generated PDF, PNG and JSON directory; compare its PDF with the committed one.")
    args = parser.parse_args()
    paths = {suffix: args.output_dir / f"memory_deficit{suffix}"
             for suffix in (".pdf", ".png", "_data.json")}
    data = json.loads(paths["_data.json"].read_text())
    versions = {"numpy": np.__version__, "matplotlib": matplotlib.__version__}
    pins = dict(line.strip().split("==") for line in (HERE / "requirements.txt").read_text().splitlines()
                if line.strip() and not line.startswith("#"))
    # This overview uses NumPy and Matplotlib. The shared environment also pins
    # mpmath for the separate finite-bound comparison generator.
    pins = {name: pins[name] for name in versions}
    require(versions == data["environment"] == pins, "plotting environment/version mismatch")
    examples, elementary_counts = canonical_examples()
    counts = check_values(data, examples)

    generated_hash = sha256(paths[".pdf"])
    reference_hash = sha256(HERE / "memory_deficit.pdf")
    require(generated_hash == data["pdf_sha256"] == reference_hash == PACKAGED_PDF_SHA256,
            "PDF differs from its JSON hash or the packaged reference")

    # PDF and PNG are two formats of the same 200-dpi figure geometry.
    png = paths[".png"].read_bytes()
    require(png[:8] == b"\x89PNG\r\n\x1a\n", "invalid PNG signature")
    pixels = struct.unpack(">II", png[16:24])
    box = re.search(rb"/MediaBox\s*\[\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*\]",
                    paths[".pdf"].read_bytes())
    require(box is not None, "PDF MediaBox missing")
    x0, y0, x1, y1 = map(float, box.groups())
    require(all(abs(actual - points * 200 / 72) <= 2 for actual, points in
                zip(pixels, (x1 - x0, y1 - y0))), "PDF/PNG geometry mismatch")
    inventory = {str(p.relative_to(HERE.parent.parent)) if p.is_relative_to(HERE.parent.parent)
                 else str(p): sha256(p) for p in [HERE / "generate_plots.py", HERE / "requirements.txt",
                 HERE / "check_plots.py", HERE.parent / "verify.py", *paths.values()]}
    print(json.dumps({"status": "passed", "versions": versions, "checked": counts,
                      "canonical_elementary_check_counts": elementary_counts,
                      "packaged_pdf_sha256": reference_hash, "png_pixels": pixels,
                      "sha256_inventory": inventory,
                      "scope": "Analytic plot/source and asset consistency; not a proof, cryptographic test, or hardware benchmark."},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
