#!/usr/bin/env python3
"""Generate the analytic memory-deficit figure and all plotted values.

Run from any directory:
    python3 verification/Graph/generate_plots.py

The curves bound optimal exact-string success in the ideal BB84 storage task.
The gap between the curves records the unresolved optimal exponent.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FixedLocator, FuncFormatter, MultipleLocator


HERE = Path(__file__).resolve().parent
PINNED_VERSIONS = {"numpy": "2.3.5", "matplotlib": "3.10.8"}
FIXED_DATE = dt.datetime(2026, 11, 3, 0, 0, tzinfo=dt.timezone.utc)


def calculate() -> dict:
    """Compute values directly from the proved bound and explicit strategy."""
    beta = (1.0 + 1.0 / math.sqrt(2.0)) / 2.0
    exponent = -math.log2(beta)
    necessary_coefficient = 1.0 / exponent

    deficit = np.arange(121, dtype=int)
    upper = np.exp2(-deficit / 6.0)
    achieved = np.power(beta, deficit)

    # Target strength u=k/100 is represented rationally when computing ceil(6u).
    # This prevents a floating-point approximation to an integer from causing
    # an artificial extra qubit in the sufficient integer gap.
    target_numerator = np.arange(3001, dtype=int)
    target_denominator = 100
    target_bits = target_numerator / target_denominator
    necessary = np.ceil(necessary_coefficient * target_bits).astype(int)
    sufficient = (
        6 * target_numerator + target_denominator - 1
    ) // target_denominator

    # The plotted staircases use analytic breakpoints, rather than joining
    # a dense grid whose jumps could be displaced by the sampling interval.
    necessary_last = math.ceil(30.0 / exponent)
    necessary_breaks = np.append(np.arange(necessary_last) * exponent, 30.0)
    sufficient_breaks = np.arange(181) / 6.0

    assert math.isclose(beta, math.cos(math.pi / 8) ** 2, abs_tol=2e-16)
    assert math.isclose(necessary_coefficient, 4.3773887469084, abs_tol=1e-12)
    assert upper[0] == achieved[0] == 1.0
    assert math.isclose(upper[120], 2.0**-20, rel_tol=1e-14)
    assert math.isclose(achieved[1], beta, rel_tol=1e-14)
    assert np.all(achieved <= upper + 1e-15)
    assert np.all(np.diff(upper) < 0) and np.all(np.diff(achieved) < 0)
    assert np.all(necessary <= sufficient)
    assert necessary[0] == sufficient[0] == 0
    assert necessary[2000] == 88 and sufficient[2000] == 120
    assert necessary[-1] == 132 and sufficient[-1] == 180

    # Integer thresholds genuinely meet their defining scalar inequalities.
    assert np.all(exponent * necessary >= target_bits - 1e-12)
    assert np.all(exponent * (necessary[1:] - 1) < target_bits[1:] + 1e-12)
    assert np.all(sufficient / 6 >= target_bits - 1e-12)
    assert np.all((sufficient[1:] - 1) / 6 < target_bits[1:] + 1e-12)

    return {
        "constants": {
            "beta": beta,
            "minus_log2_beta": exponent,
            "necessary_gap_coefficient": necessary_coefficient,
            "sufficient_gap_coefficient": 6,
        },
        "panel_a": {
            "missing_qubits_t": deficit.tolist(),
            "universal_upper_bound": upper.tolist(),
            "explicit_store_and_measure_success": achieved.tolist(),
        },
        "panel_b": {
            "target_strength_log2_inverse_delta": target_bits.tolist(),
            "target_numerator": target_numerator.tolist(),
            "target_denominator": target_denominator,
            "necessary_integer_gap": necessary.tolist(),
            "sufficient_integer_gap": sufficient.tolist(),
            "plotted_necessary_breakpoints_u": necessary_breaks.tolist(),
            "plotted_necessary_gap": list(range(necessary_last + 1)),
            "plotted_sufficient_breakpoints_u": sufficient_breaks.tolist(),
            "plotted_sufficient_gap": list(range(181)),
        },
    }


def power_label(value: float, _position: int) -> str:
    return rf"$2^{{{int(round(math.log2(value)))}}}$"


def plot(data: dict, output: Path) -> None:
    plt.rcParams.update(
        {
            "font.family": "STIXGeneral",
            "mathtext.fontset": "stix",
            "font.size": 10.0,
            "axes.labelsize": 10.5,
            "axes.titlesize": 11,
            "xtick.labelsize": 9.5,
            "ytick.labelsize": 9.5,
            "legend.fontsize": 9.1,
            "axes.linewidth": 0.65,
            "lines.linewidth": 1.6,
            "xtick.major.width": 0.65,
            "ytick.major.width": 0.65,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "savefig.transparent": False,
        }
    )
    blue, orange, light = "#176C91", "#B45D26", "#DDECF2"
    fig, axes = plt.subplots(1, 2, figsize=(7.3, 2.8), layout="constrained")
    fig.set_constrained_layout_pads(w_pad=0.035, h_pad=0.035, wspace=0.075)

    a = data["panel_a"]
    x = np.asarray(a["missing_qubits_t"])
    hi = np.asarray(a["universal_upper_bound"])
    lo = np.asarray(a["explicit_store_and_measure_success"])
    ax = axes[0]
    ax.fill_between(x, lo, hi, color=light, zorder=1)
    ax.plot(x, hi, color=blue, label=r"Universal upper bound $2^{-t/6}$", zorder=3)
    ax.plot(x, lo, color=orange, linestyle=(0, (4, 2)),
            label=r"Explicit strategy $\beta^t$", zorder=3)
    ax.set_yscale("log", base=2)
    ax.set_xlim(0, 120)
    ax.set_ylim(2.0**-28, 1.25)
    ax.xaxis.set_major_locator(MultipleLocator(30))
    ax.yaxis.set_major_locator(FixedLocator(np.exp2(np.arange(-25, 1, 5))))
    ax.yaxis.set_major_formatter(FuncFormatter(power_label))
    ax.set_xlabel(r"Missing-qubit gap $t=k-m$")
    ax.set_ylabel("Exact-string success probability")
    ax.set_title("(a) Bounds on guessing", loc="left", pad=5)
    ax.legend(loc="lower left", frameon=False, handlelength=1.9,
              labelspacing=0.35, borderaxespad=0.25)

    b = data["panel_b"]
    ax = axes[1]
    ax.step(b["plotted_sufficient_breakpoints_u"], b["plotted_sufficient_gap"],
            where="pre", color=blue,
            label=r"Sufficient: $\lceil6u\rceil$")
    ax.step(b["plotted_necessary_breakpoints_u"], b["plotted_necessary_gap"],
            where="pre", color=orange,
            linestyle=(0, (4, 2)), label=r"Necessary: $\lceil u/(-\log_2\beta)\rceil$")
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 185)
    ax.xaxis.set_major_locator(MultipleLocator(10))
    ax.yaxis.set_major_locator(MultipleLocator(30))
    ax.set_xlabel(r"Target strength $u=\log_2(1/\delta)$")
    ax.set_ylabel("Integer missing-qubit gap")
    ax.set_title("(b) Gap for target success", loc="left", pad=5)
    ax.legend(loc="upper left", frameon=False, handlelength=1.9,
              labelspacing=0.35, borderaxespad=0.25)

    for ax in axes:
        ax.grid(axis="both", color="0.87", linewidth=0.5, zorder=0)
        ax.set_axisbelow(True)
        ax.tick_params(direction="out", length=3, pad=3)
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(
        output,
        format="pdf",
        metadata={
            "Title": "Finite BB84 storage-gap bounds",
            "Author": "",
            "Subject": "Analytic upper bound and explicit strategy; unmatched constants",
            "Creator": "generate_plots.py",
            "CreationDate": FIXED_DATE,
            "ModDate": FIXED_DATE,
        },
        bbox_inches="tight",
        pad_inches=0.025,
    )
    fig.savefig(output.with_suffix(".png"), dpi=200,
                bbox_inches="tight", pad_inches=0.025)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=HERE)
    args = parser.parse_args()
    observed = {"numpy": np.__version__, "matplotlib": matplotlib.__version__}
    if observed != PINNED_VERSIONS:
        raise RuntimeError(f"Use the pinned plotting environment: {observed!r}")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    data = calculate()
    data["environment"] = observed
    data["interpretation"] = {
        "panel_a": "For integer t, beta^t <= optimal ideal guessing success <= 2^(-t/6). Shading is the interval allowed by these bounds; it is not an exact frontier or a claim that every intermediate value is achievable.",
        "panel_b": "For target delta=2^(-u), ceil(u/(-log2(beta))) is necessary and ceil(6u) sufficient. u=0 is the trivial endpoint. Sufficient here refers only to the ideal test; remote-preparation error must be budgeted separately.",
        "scope": "Analytic ideal-model bounds; no cryptographic implementation, physical-noise model, hardware data, or optimal exponent claim.",
    }
    pdf = args.output_dir / "memory_deficit.pdf"
    plot(data, pdf)
    data["pdf_sha256"] = hashlib.sha256(pdf.read_bytes()).hexdigest()
    json_path = args.output_dir / "memory_deficit_data.json"
    json_path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"pdf": str(pdf), "data": str(json_path),
                      "pdf_sha256": data["pdf_sha256"],
                      "assertions": "passed", "constants": data["constants"]}, indent=2))


if __name__ == "__main__":
    main()
