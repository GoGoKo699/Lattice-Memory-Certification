#!/usr/bin/env python3
"""Finite checks at the delayed-basis guessing/noisy-processing interface.

Dense two-qubit channels check the genuine quantum-plus-classical CPTP
factorization and basis-dependent endpoint probabilities. The authoritative
rank-budget checks live in Measurement-Free-Memory-Cost; this script does not
fetch that repository or infer that a physical device obeys its assumptions.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import itertools
import json
import math
from pathlib import Path

import numpy as np

import verify


def replacement_factorization(s: int, c: int) -> tuple[list[np.ndarray], list[np.ndarray]]:
    """Kraus maps F: QCG->QC and J: QC->QCG, with C dephased."""
    qdim, cdim, gdim = 2**s, 2**c, 2**(2 - s - c)
    f_ops = []
    for z, g in itertools.product(range(cdim), range(gdim)):
        kraus = np.zeros((qdim * cdim, 4), dtype=complex)
        for q in range(qdim):
            kraus[q * cdim + z, (q * cdim + z) * gdim + g] = 1
        f_ops.append(kraus)
    j_ops = []
    for g in range(gdim):
        kraus = np.zeros((4, qdim * cdim), dtype=complex)
        for qc in range(qdim * cdim):
            kraus[qc * gdim + g, qc] = 1 / math.sqrt(gdim)
        j_ops.append(kraus)
    return f_ops, j_ops


def apply(kraus: list[np.ndarray], rho: np.ndarray) -> np.ndarray:
    return sum(op @ rho @ op.conj().T for op in kraus)


def independent_pauli_twirl(s: int, c: int, rho: np.ndarray) -> np.ndarray:
    """Twirl by the commutant, independently of the F/J Kraus construction."""
    axes = ([verify.I] for _ in range(s))
    choices = list(axes) + [[verify.I, verify.Z] for _ in range(c)]
    choices += [list(verify.PAULIS) for _ in range(2 - s - c)]
    paulies = [verify.tensor(words) for words in itertools.product(*choices)]
    return sum(p @ rho @ p.conj().T for p in paulies) / len(paulies)


def random_unitary(rng: np.random.Generator, dim: int) -> np.ndarray:
    matrix = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
    q, _ = np.linalg.qr(matrix)
    return q


def replacement_branch(mask: int) -> list[np.ndarray]:
    """Two-slot identity/replacement branch, with no flag in its output."""
    reset = []
    for out, inp in itertools.product(range(2), repeat=2):
        op = np.zeros((2, 2), dtype=complex)
        op[out, inp] = 1 / math.sqrt(2)
        reset.append(op)
    choices = [reset if mask & (1 << slot) else [verify.I] for slot in range(2)]
    return [verify.tensor(words) for words in itertools.product(*choices)]


def pauli_noise(rho: np.ndarray, gamma: float) -> np.ndarray:
    """Independent implementation of product depolarization by Pauli errors."""
    single = [math.sqrt(1 - 3 * gamma / 4) * verify.I]
    single += [math.sqrt(gamma / 4) * pauli for pauli in verify.PAULIS[1:]]
    return apply([verify.tensor(words) for words in itertools.product(single, repeat=2)], rho)


def check_cut_averaging(audit: verify.Audit, prefix: list[np.ndarray],
                        basis_matrices: list[np.ndarray]) -> dict:
    """Compare actual Pauli noise with independent replacement choices at cuts.

    Earlier rounds are averaged into the same prefix for all future choices.
    The actual endpoint decoder is identical on every branch. This checks a
    finite fixture, rather than certifying independence in an external device.
    """
    gamma = 0.23
    hadamard = np.array([[1, 1], [1, -1]], dtype=complex) / math.sqrt(2)
    cnot = np.array([[1, 0, 0, 0], [0, 1, 0, 0],
                     [0, 0, 0, 1], [0, 0, 1, 0]], dtype=complex)
    t_gate = np.diag([1, np.exp(1j * math.pi / 4)])
    # None denotes a full product-noise round. Every other item is a single
    # fixed Clifford or charged T primitive; there is no adaptive controller.
    operations = [None, np.kron(hadamard, verify.I), cnot,
                  np.kron(verify.I, t_gate), None]
    branches = [replacement_branch(mask) for mask in range(4)]
    weights = [gamma**mask.bit_count() * (1 - gamma)**(2 - mask.bit_count())
               for mask in range(4)]
    audit.equal('future_branch_weights_normalized', sum(weights), 1)
    cut_scores = [0.0] * (len(operations) + 1)
    actual_score = 0.0
    for basis in basis_matrices:
        for x in range(4):
            vector = basis[:, x]
            effect = np.outer(vector, vector.conj())
            states = [apply(prefix, effect)]
            for op in operations:
                states.append(pauli_noise(states[-1], gamma) if op is None
                              else op @ states[-1] @ op.conj().T)
            actual_probability = float(np.trace(effect @ states[-1]).real)
            actual_score += actual_probability / 16
            for cut in range(len(states)):
                suffix = operations[cut:]
                noisy_rounds = sum(op is None for op in suffix)
                average_state = np.zeros((4, 4), dtype=complex)
                average_probability = 0.0
                for choices in itertools.product(range(4), repeat=noisy_rounds):
                    rho = states[cut].copy()
                    branch_weight = 1.0
                    index = 0
                    for op in suffix:
                        if op is None:
                            choice = choices[index]
                            rho = apply(branches[choice], rho)
                            branch_weight *= weights[choice]
                            index += 1
                        else:
                            rho = op @ rho @ op.conj().T
                    average_state += branch_weight * rho
                    average_probability += branch_weight * float(np.trace(effect @ rho).real)
                audit.equal('cut_averaged_channel_output', average_state, states[-1])
                audit.equal('cut_averaged_actual_decoder', average_probability,
                            actual_probability)
                cut_scores[cut] += average_probability / 16
    return {'noise_rounds': 2, 'primitive_cuts': len(cut_scores),
            'basis_input_cases': 16, 'depolarizing_strength': gamma,
            'actual_unconditional_score': actual_score,
            'averaged_actual_branch_scores': cut_scores,
            'noise_implementations': ['Pauli-error channel', 'independent replacement choices']}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', type=Path)
    args = parser.parse_args()
    audit = verify.Audit()
    rng = np.random.default_rng(20261104)
    basis_matrices = verify.bases(2)
    # One fixed CPTP prefix for all secret labels and every proof branch.
    prefix = [math.sqrt(weight) * random_unitary(rng, 4)
              for weight in (0.3, 0.7)]
    tail_unitary = random_unitary(rng, 4)
    cases = []
    for s in range(3):
        for c in range(3 - s):
            f_ops, j_ops = replacement_factorization(s, c)
            audit.equal('F_trace_preserving', sum(f.conj().T @ f for f in f_ops), np.eye(4))
            audit.equal('J_trace_preserving', sum(j.conj().T @ j for j in j_ops), np.eye(2**(s+c)))
            # The 16 matrix units span all operators, including imaginary
            # coherences outside the span of the BB84 projectors below.
            for row, column in itertools.product(range(4), repeat=2):
                unit = np.zeros((4, 4), dtype=complex)
                unit[row, column] = 1
                audit.equal('full_channel_matrix_units', apply(j_ops, apply(f_ops, unit)),
                            independent_pauli_twirl(s, c, unit))
            total_success = 0.0
            basis_input_cases = 0
            for basis in basis_matrices:
                # This endpoint may depend on the disclosed basis. The prefix
                # above was fixed before any basis was supplied.
                for x in range(4):
                    vector = basis[:, x]
                    rho = apply(prefix, np.outer(vector, vector.conj()))
                    qc = apply(f_ops, rho)
                    direct = independent_pauli_twirl(s, c, rho)
                    factored = apply(j_ops, qc)
                    audit.equal('Q_plus_C_CPTP_factorization', factored, direct)
                    audit.equal('normalized_Q_plus_C_output', np.trace(qc), 1)
                    audit.leq('positive_Q_plus_C_output', -float(np.linalg.eigvalsh(qc).min()), 0)
                    # Every off-diagonal C block must vanish, without tracing
                    # away its input-dependent classical probability.
                    cdim = 2**c
                    for z, zp in itertools.permutations(range(cdim), 2):
                        audit.equal('classical_blocks', qc[z::cdim, zp::cdim], 0)
                    effect_vector = basis[:, x]
                    effect = np.outer(effect_vector, effect_vector.conj())
                    direct_probability = float(np.trace(effect @ tail_unitary @ direct
                                                       @ tail_unitary.conj().T).real)
                    factored_probability = float(np.trace(effect @ tail_unitary @ factored
                                                         @ tail_unitary.conj().T).real)
                    audit.equal('basis_endpoint_probability', direct_probability, factored_probability)
                    total_success += direct_probability / 16
                    basis_input_cases += 1
            score_bound = min(1.0, 2.0**((s - 2) / 6), 2.0**(s + c - 2))
            audit.leq('branch_score_bound', total_success, score_bound)
            cases.append({'s_quantum_qubits': s, 'c_classical_bits': c,
                          'binary_rank': 2 * s + c,
                          'basis_input_cases': basis_input_cases,
                          'average_score': total_success,
                          'branch_upper_bound': score_bound})

    # Independent full-replacement/identity channel choices are proof flags,
    # rather than physically returned information. A common basis readout
    # already gives this exact unconditional average.
    mixtures = []
    for weight in (Fraction(0), Fraction(1, 5), Fraction(2, 5), Fraction(1)):
        p = weight + (1 - weight) / 4
        mixed_channel = [math.sqrt(float(weight)) * np.eye(4)]
        mixed_channel += [math.sqrt(float(1 - weight)) * op
                          for op in replacement_branch(3)]
        probability_sum = 0.0
        for basis in basis_matrices:
            for x in range(4):
                vector = basis[:, x]
                effect = np.outer(vector, vector.conj())
                # Compute the density matrix and fixed basis readout directly,
                # without adding a flag or optimizing a branch decoder.
                probability_sum += float(np.trace(effect @ apply(mixed_channel, effect)).real) / 16
        audit.equal('dense_unconditional_mixture_score', probability_sum, float(p))
        mixtures.append({'identity_weight': str(weight), 'unconditional_score': str(p),
                         'expected_rank': str(4 * weight)})

    cut_averaging = check_cut_averaging(audit, prefix, basis_matrices)

    a = 24 * (Fraction(2, 5) - Fraction(1, 4096)) / (1 - Fraction(1, 4096))
    audit.equal('shared_twelve_qubit_rank_floor', float(a), 9.596483516483518)
    report = {
        'status': 'passed', 'seed': 20261104,
        'canonical_algebras': len(cases), 'channel_cases': cases,
        'unconditional_channel_mixtures': mixtures,
        'primitive_cut_averaging': cut_averaging,
        'shared_example': {'challenge_qubits': 12, 'score': '2/5',
                           'random_guess_baseline': '1/4096', 'rank_floor': str(a)},
        'assertions': sum(audit.counts.values()), 'check_counts': audit.counts,
        'maximum_identity_errors': audit.max_errors,
        'maximum_positive_inequality_violations': audit.max_violation,
        'authoritative_dynamical_checks':
            'Measurement-Free-Memory-Cost/verification/verify_guessing_processing.py',
        'limits': ['Finite channel identities do not replace the all-cut proof.',
                   'No hardware noise or controller premise is verified.',
                   'The LWE preparation wrapper is not imported.',
                   'No network access or other checkout is needed at runtime.'],
    }
    text = json.dumps(report, sort_keys=True, indent=2) + '\n'
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(text, encoding='utf-8')
    print(text, end='')


if __name__ == '__main__':
    main()
