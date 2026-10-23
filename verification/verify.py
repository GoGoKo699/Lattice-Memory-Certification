#!/usr/bin/env python3
"""Deterministic finite checks for Lattice Memory Certification.

This checks identities and sampled inequalities, not cryptographic hardness,
all encoders, or the tensor-power hypercontractivity theorem. Run without
arguments for a JSON report; --write PATH saves that same report.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import re
from pathlib import Path

import numpy as np
from numpy.typing import NDArray

Matrix = NDArray[np.complex128]
SEED = 20261023
TOL = 2e-10
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
H = (X + Z) / math.sqrt(2)
PAULIS = (I, X, Y, Z)


class Audit:
    def __init__(self) -> None:
        self.counts: dict[str, int] = {}
        self.max_errors: dict[str, float] = {}
        self.max_violation: dict[str, float] = {}

    def equal(self, name: str, a, b, tol: float = TOL) -> None:
        err = float(np.max(np.abs(np.asarray(a) - np.asarray(b))))
        if not np.isfinite(err) or err > tol:
            raise AssertionError(f'{name}: error {err:.4g} exceeds {tol:.4g}')
        self.counts[name] = self.counts.get(name, 0) + 1
        self.max_errors[name] = max(self.max_errors.get(name, 0.0), err)

    def leq(self, name: str, a: float, b: float) -> None:
        violation = max(0.0, float(a - b))
        if not np.isfinite(a + b) or violation > TOL:
            raise AssertionError(f'{name}: {a:.16g} > {b:.16g}')
        self.counts[name] = self.counts.get(name, 0) + 1
        self.max_violation[name] = max(self.max_violation.get(name, 0.0), violation)


def psd_power(a: Matrix, power: float) -> Matrix:
    vals, vecs = np.linalg.eigh((a + a.conj().T) / 2)
    if float(vals.min()) < -TOL:
        raise AssertionError('Matrix is not positive semidefinite')
    out = np.zeros_like(vals)
    mask = vals > 1e-13
    out[mask] = vals[mask] ** power
    return (vecs * out) @ vecs.conj().T


def tensor(items) -> Matrix:
    result = np.ones((1, 1), dtype=complex)
    for item in items:
        result = np.kron(result, item)
    return result


def bases(n: int) -> list[Matrix]:
    return [tensor(H if b else I for b in bits)
            for bits in itertools.product((0, 1), repeat=n)]


def random_matrix(rng, rows: int, cols: int) -> Matrix:
    return rng.normal(size=(rows, cols)) + 1j * rng.normal(size=(rows, cols))


def random_state(rng, d: int, dim: int, rank: int, skew: bool) -> Matrix:
    u, _ = np.linalg.qr(random_matrix(rng, d, rank))
    v, _ = np.linalg.qr(random_matrix(rng, dim, rank))
    lam = np.exp(np.linspace(0, -6 if skew else 0, rank))
    lam /= lam.sum()
    return (u * np.sqrt(lam)) @ v.T


def random_povm(rng, dim: int, outcomes: int) -> list[Matrix]:
    gs = [random_matrix(rng, dim, dim) for _ in range(outcomes)]
    raw = [g.conj().T @ g for g in gs]
    inv = psd_power(sum(raw), -0.5)
    return [inv @ a @ inv for a in raw]


def pure_checks(audit: Audit, rng) -> int:
    cases = 0
    for n in range(1, 5):
        d = 2**n
        us = bases(n)
        words = list(itertools.product(range(4), repeat=n))
        ps = [tensor(PAULIS[j] for j in w) for w in words]
        weights_t = np.array([math.prod((1, 0.5, 0, 0.5)[j] for j in w)
                              for w in words])
        weights_d = np.array([0.5**sum(j != 0 for j in w) for w in words])
        for dim in sorted(set((1, 2, min(3, d), min(4, d), d))):
            for rank in sorted(set((1, dim))):
                for skew in (False, True):
                    for _ in range(2):
                        psi = random_state(rng, d, dim, rank, skew)
                        rho = psi @ psi.conj().T
                        root = psd_power(rho, 0.5)
                        s = psi.T @ psi.conj()
                        invs = psd_power(s, -0.5)
                        pgms, successes, list_successes = [], [], []
                        ls = min(3, d)
                        for u in us:
                            rows = u.conj().T @ psi
                            sigmas = [np.outer(row, row.conj()) for row in rows]
                            audit.equal('ensemble_sum', sum(sigmas), s)
                            pgm = float(sum(np.trace(t @ invs @ t @ invs).real
                                            for t in sigmas))
                            diag = np.diag(u.conj().T @ root @ u).real
                            audit.equal('pgm_schmidt_identity', pgm, np.dot(diag, diag))
                            ms = random_povm(rng, dim, d)
                            audit.equal('povm_normalization', sum(ms), np.eye(dim))
                            p = float(sum(np.trace(t @ m).real for t, m in zip(sigmas, ms)))
                            audit.leq('barnum_knill_sampled', p*p, pgm)
                            if dim == 1:
                                p_opt = max(float(t.trace().real) for t in sigmas)
                                audit.leq('barnum_knill_scalar_optimum', p_opt*p_opt, pgm)
                            if d == 2:
                                delta = sigmas[0] - sigmas[1]
                                p_opt = (1 + np.abs(np.linalg.eigvalsh(delta)).sum())/2
                                audit.leq('barnum_knill_helstrom_optimum', p_opt*p_opt, pgm)
                            # Output y accepts the cyclic list {y,...,y+L-1}.
                            fs = [sum(ms[(x-j) % d] for j in range(ls)) for x in range(d)]
                            audit.equal('list_effect_sum', sum(fs), ls*np.eye(dim))
                            pl = float(sum(np.trace(t @ f).real for t, f in zip(sigmas, fs)))
                            audit.leq('list_discrimination', pl*pl, ls*pgm)
                            pgms.append(pgm)
                            successes.append(p)
                            list_successes.append(pl)
                        avg = float(np.mean(pgms))
                        coeffs = np.array([np.trace(p @ root).real/d for p in ps])
                        pauli_t = float(d * np.dot(coeffs**2, weights_t))
                        pauli_d = float(d * np.dot(coeffs**2, weights_d))
                        audit.equal('average_pauli_identity', avg, pauli_t)
                        audit.leq('depolarizing_domination', avg, pauli_d)
                        trace34 = float(np.trace(psd_power(rho, 0.75)).real)
                        hc = d**(-1/3) * trace34**(4/3)
                        audit.leq('hypercontractive_sample', pauli_d, hc)
                        audit.leq('rank_holder', hc, (rank/d)**(1/3))
                        audit.leq('averaged_sqrt_bound', float(np.mean(np.sqrt(pgms))),
                                  (rank/d)**(1/6))
                        audit.leq('sampled_exact_success', float(np.mean(successes)),
                                  (dim/d)**(1/6))
                        audit.leq('sampled_list_success', float(np.mean(list_successes)),
                                  min(1.0, math.sqrt(ls)*(dim/d)**(1/6)))
                        cases += 1
    return cases


def instrument_checks(audit: Audit, rng) -> int:
    cases = 0
    for n in range(1, 4):
        d = 2**n
        for dim in (1, 2, d):
            kcount = max(2, math.ceil(d/dim)+1)
            for _ in range(3):
                iso, _ = np.linalg.qr(random_matrix(rng, kcount*dim, d))
                ks = [iso[c*dim:(c+1)*dim] for c in range(kcount)]
                audit.equal('instrument_trace_preserving',
                            sum(k.conj().T @ k for k in ks), np.eye(d))
                direct, delayed, weights = 0.0, 0.0, []
                for k in ks:
                    weight = float(np.trace(k.conj().T @ k).real/d)
                    weights.append(weight)
                    psi = k.T/math.sqrt(d*weight)
                    for u in bases(n):
                        ms = random_povm(rng, dim, d)
                        for x in range(d):
                            vec = k @ u[:, x]
                            direct += np.vdot(vec, ms[x] @ vec).real / d**2
                            row = (u.conj().T @ psi)[x]
                            delayed += weight*np.vdot(row, ms[x] @ row).real/d
                audit.equal('branch_probabilities', sum(weights), 1.0)
                audit.equal('prepare_vs_delayed_measurement', direct, delayed)
                audit.leq('instrument_success_bound', direct, min(1.0,(dim/d)**(1/6)))
                cases += 1
    return cases


def elementary_checks(audit: Audit) -> dict:
    beta = (1 + 1/math.sqrt(2))/2
    _, eigvec = np.linalg.eigh((X+Z)/math.sqrt(2))
    # Highest-eigenvalue outcome is decoded as bit zero in both bases.
    v0, v1 = eigvec[:, 1], eigvec[:, 0]
    for u in (I, H):
        for x, v in ((0, v0), (1, v1)):
            audit.equal('breidbart_bit_success', abs(np.vdot(v,u[:,x]))**2, beta)
    for n in range(1, 6):
        d = 2**n
        for u in bases(n):
            psi = np.eye(d)/math.sqrt(d)
            sigma = [np.outer(v,v.conj()) for v in u.T @ psi]
            pgm = sum(float(np.trace(t @ t).real*d) for t in sigma)
            audit.equal('full_memory_endpoint', pgm, 1.0)
        for m in range(n+1):
            gap = n-m
            attack = beta**gap
            upper = 2**(-gap/6)
            audit.leq('witness_vs_upper_bound', attack, upper)
            for r in range(gap+1):
                p = sum(math.comb(gap,j)*(1-beta)**j*beta**(gap-j)
                        for j in range(r+1))
                volume = sum(math.comb(n,j) for j in range(r+1))
                audit.leq('hamming_witness_vs_list_bound',p,
                          min(1.0,math.sqrt(volume)*upper))
                if r == gap:
                    audit.equal('tolerated_missing_qubits',p,1.0)
    def h2(x: float) -> float:
        if not 0 <= x <= 1:
            raise ValueError('Binary entropy argument must be in [0,1]')
        return sum(-z*math.log2(z) for z in (x,1-x) if z > 0)
    comparison=[]
    ideal_error=2**-20
    for n in (1024, 10000, 1000000):
        a=(1+2*math.log2(1/ideal_error))/n
        previous_gap=math.ceil(n*(h2(a)+a))
        new_gap=math.ceil(6*math.log2(1/ideal_error))
        comparison.append({'n':n,'ideal_error':ideal_error,
                           'this_sufficient_gap':new_gap,
                           'dfw_cor11_dimension_specialization_sufficient_gap':previous_gap})
        audit.leq('comparison_in_admissible_range',previous_gap,n)
    return {'breidbart_beta':beta,
            'necessary_gap_coefficient':1/(-math.log2(beta)),
            'sufficient_gap_coefficient':6,
            'finite_comparison':comparison}


def navigation_checks(audit: Audit) -> int:
    root=Path(__file__).resolve().parents[1]
    count=0
    for file in sorted(root.rglob('*.md')):
        text=file.read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)\s]+)\)',text):
            if '://' in target or target.startswith(('mailto:','#')):
                continue
            path=target.split('#',1)[0]
            if path and not (file.parent/path).exists():
                raise AssertionError(f'Broken local path: {file.relative_to(root)} -> {target}')
            count+=1
    audit.equal('local_navigation_paths',count,count)
    return count


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', type=Path, help='Save the JSON report to this path')
    args=parser.parse_args()
    rng=np.random.default_rng(SEED)
    audit=Audit()
    state_cases=pure_checks(audit,rng)
    instrument_cases=instrument_checks(audit,rng)
    examples=elementary_checks(audit)
    links=navigation_checks(audit)
    result={'status':'passed','seed':SEED,'numpy_version':np.__version__,
            'absolute_tolerance':TOL,'pure_state_cases':state_cases,
            'instrument_cases':instrument_cases,'local_link_paths_checked':links,
            'check_counts':audit.counts,'maximum_identity_errors':audit.max_errors,
            'maximum_positive_inequality_violations':audit.max_violation,
            'examples':examples,
            'limits':['Finite deterministic checks are not a proof of general inequalities.',
                      'No cryptographic implementation, hardness test, or hardware benchmark is run.',
                      'Random POVMs are not a global search for the optimal joint decoder.',
                      'Local link checks do not inspect hosted mathematical rendering.']}
    encoded=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.write:
        args.write.parent.mkdir(parents=True,exist_ok=True)
        args.write.write_text(encoded,encoding='utf-8')
    print(encoded,end='')


if __name__=='__main__':
    main()
