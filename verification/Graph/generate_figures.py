#!/usr/bin/env python3
"""Reproduce the storage-gap and finite-guessing comparison figure.

Run from any directory. This generator and its dependency pins reproduce the
quantitative figure directly; no LaTeX installation is required.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np

BASE = Path(__file__).resolve().parent
BLUE, ORANGE, GREEN, GRAY = "#0072B2", "#D55E00", "#009E73", "#666666"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 9,
    "axes.labelsize": 10, "axes.titlesize": 10,
    "xtick.labelsize": 9, "ytick.labelsize": 9,
    "legend.fontsize": 8.2, "axes.spines.top": False,
    "axes.spines.right": False, "axes.linewidth": 0.7,
    "pdf.fonttype": 42, "ps.fonttype": 42,
    "savefig.facecolor": "white", "figure.facecolor": "white",
})



def save(fig, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    # Suppress time-bearing PDF metadata so regeneration is byte-stable.
    fig.savefig(target, bbox_inches="tight", pad_inches=0.035,
                metadata={"CreationDate": None, "ModDate": None,
                          "Creator": "generate_figures.py"})
    fig.savefig(target.with_suffix(".png"), dpi=220, bbox_inches="tight", pad_inches=0.035)
    plt.close(fig)

def lattice_figure(output_dir):
    fig, axs = plt.subplots(1, 2, figsize=(7.0, 3.35),
                            gridspec_kw={"width_ratios": [1.25, 1]}, constrained_layout=True)
    t = np.arange(0, 61)
    beta = (1+1/np.sqrt(2))/2
    ax = axs[0]
    ax.plot(t, 2.0**(-t/6), color=BLUE, lw=1.9, label=r"Universal upper $2^{-t/6}$")
    ax.plot(t, beta**t, color=GREEN, lw=1.9, ls="--", label=r"Achievable lower $\beta^t$")
    ax.set(xlabel=r"Storage deficit $t=k-m$", ylabel="Whole-string guessing probability",
           yscale="log", xlim=(0, 60), ylim=(5e-5, 1.25))
    ax.grid(which="major", color="#DDDDDD", lw=0.6)
    ax.legend(frameon=False, loc="lower left")
    ax.text(0, 1.02, "(a)", transform=ax.transAxes, weight="bold")
    ax.text(0.98, 0.97, r"$\beta=(1+1/\sqrt{2})/2$", ha="right", va="top",
            transform=ax.transAxes, fontsize=8.5)
    k = np.array([3, 4, 5])
    caps = np.array([(2+7*np.sqrt(2))/16, (2+np.sqrt(345))/32,
                     (4+np.sqrt(4526))/128])
    lower = beta**(k-1)
    upper = 2.0**(-(k-1)/6)
    bx = axs[1]
    bx.vlines(k, lower, caps, color="#A9B5BD", lw=5, zorder=1)
    bx.plot(k, upper, color=BLUE, marker="^", ms=5, ls=":", lw=1.3,
            label="Universal upper")
    bx.plot(k, caps, color=ORANGE, marker="o", ms=5, ls="None",
            label="Finite upper")
    bx.plot(k, lower, color=GREEN, marker="s", ms=5, ls="None",
            label="Achievable lower")
    for x, y in zip(k, caps):
        bx.annotate(f"{y:.6f}", (x, y), xytext=(0, 10),
                    textcoords="offset points", ha="center", fontsize=8.2, color=ORANGE)
    bx.set(xlabel=r"BB84 inputs $k$ ($m=1$)", ylim=(0.46, 0.86),
           xlim=(2.6, 5.4), xticks=k)
    bx.grid(axis="y", color="#DDDDDD", lw=0.6)
    bx.legend(frameon=False, fontsize=7.7, loc="lower left")
    bx.text(0, 1.02, "(b)", transform=bx.transAxes, weight="bold")
    save(fig, output_dir/"lattice_bounds.pdf")


def validate():
    """Use independent high-precision scalar formulas for all plotted values."""
    mp.mp.dps = 80
    beta = (1 + mp.sqrt(mp.mpf(1) / 2)) / 2
    finite = []
    for k, Q, cap in [(3, mp.mpf(9)/16, (2+7*mp.sqrt(2))/16),
                       (4, mp.mpf(27)/64, (2+mp.sqrt(345))/32),
                       (5, mp.mpf(81)/256, (4+mp.sqrt(4526))/128)]:
        d = mp.mpf(2)**k
        # Solve p^2 + (1-p)^2/(d-1) = Q without the closed cap formula.
        inverse = (1 + mp.sqrt((d-1)*(d*Q-1))) / d
        assert abs(inverse-cap) < mp.mpf('1e-75')
        assert abs(cap**2+(1-cap)**2/(d-1)-Q) < mp.mpf('1e-75')
        assert Q == (mp.mpf(3)/4)**(k-1)
        lower = beta**(k-1)
        upper = mp.power(2, -mp.mpf(k-1)/6)
        assert lower < cap < upper
        finite.append({'k': k, 'm': 1, 'exact_PGM': str(Q),
                       'achievable_lower': mp.nstr(lower, 65),
                       'finite_upper': mp.nstr(cap, 65),
                       'universal_upper': mp.nstr(upper, 65)})
    values = []
    for t in range(61):
        lower = beta**t
        upper = mp.power(2, -mp.mpf(t)/6)
        assert lower <= upper
        assert np.isclose(float(lower), ((1+1/np.sqrt(2))/2)**t, rtol=1e-13)
        assert np.isclose(float(upper), 2.0**(-t/6), rtol=1e-13)
        values.append({'deficit': t, 'achievable_lower': mp.nstr(lower, 65),
                       'universal_upper': mp.nstr(upper, 65)})
    return {'scope': 'Finite figure formulas and asset identity; not a proof of a universal theorem or a physical-device test.',
            'independent_check': '80-digit scalar finite-alphabet inversion and product PGM score',
            'finite_instances': finite, 'deficit_values': values,
            'packages': {'matplotlib': matplotlib.__version__, 'numpy': np.__version__, 'mpmath': mp.__version__}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=BASE)
    args = parser.parse_args()
    observed = {'matplotlib': matplotlib.__version__, 'numpy': np.__version__, 'mpmath': mp.__version__}
    expected_versions = {'matplotlib': '3.10.8', 'numpy': '2.3.5', 'mpmath': '1.3.0'}
    assert observed == expected_versions, 'Use the pinned plotting environment'
    data = validate()
    lattice_figure(args.output_dir)
    pdf = args.output_dir / 'lattice_bounds.pdf'
    data['pdf_sha256'] = hashlib.sha256(pdf.read_bytes()).hexdigest()
    expected = 'a31a685e5832078b7b10ccdc5dd605e1cfb323292ae2a4592273246841138078'
    assert data['pdf_sha256'] == expected, 'Figure differs from the accepted reference asset'
    data['outputs'] = [{'path': p.name, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'bytes': p.stat().st_size}
                       for p in [pdf, pdf.with_suffix('.png')]]
    (args.output_dir / 'lattice_bounds_data.json').write_text(json.dumps(data, indent=2) + '\n')
    print(json.dumps({'status': 'passed', 'pdf': str(pdf), 'pdf_sha256': data['pdf_sha256'],
                      'finite_instances': data['finite_instances']}, indent=2))


if __name__ == '__main__':
    main()
