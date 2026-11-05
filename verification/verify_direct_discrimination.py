#!/usr/bin/env python3
"""Exact fixed-encoder decoder certificates; no external numerical solver.

The universal diagonal-dual limitation is proved in science/direct-discrimination.md.
This checks the finite SDP witnesses, rational radical ordering, and finite
parameter instances of that limitation. It does not optimize all encoders.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
import math
from pathlib import Path


class Q2:
    """The exactly ordered field Q(sqrt(2))."""
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    def __add__(self, other):
        other = other if isinstance(other, Q2) else Q2(other)
        return Q2(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __sub__(self, other):
        return self + -(other if isinstance(other, Q2) else Q2(other))

    def __mul__(self, other):
        other = other if isinstance(other, Q2) else Q2(other)
        return Q2(self.a * other.a + 2 * self.b * other.b,
                  self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = other if isinstance(other, Q2) else Q2(other)
        den = other.a * other.a - 2 * other.b * other.b
        assert den != 0
        return self * Q2(other.a / den, -other.b / den)

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out = Q2(1)
        for _ in range(n):
            out = out * self
        return out

    def sign(self):
        a, b = self.a, self.b
        if not b:
            return (a > 0) - (a < 0)
        if not a:
            return (b > 0) - (b < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        d = a * a - 2 * b * b
        return ((d > 0) - (d < 0)) * (1 if a > 0 else -1)

    def is_zero(self):
        return self.a == 0 and self.b == 0

    def json(self):
        return [str(self.a), str(self.b)]


def sigma(k, support, x):
    """Entries of P B^tensor(k)|x><x|B^tensor(k) P / |S|."""
    r = len(support)
    c2, s2, cs = Q2(F(1, 2), F(1, 4)), Q2(F(1, 2), -F(1, 4)), Q2(0, F(1, 4))
    matrix = []
    for y in support:
        row = []
        for z in support:
            t = (y ^ x).bit_count() + (z ^ x).bit_count()
            val = c2 ** (k - (t + 1) // 2) * s2 ** (t // 2)
            if t % 2:
                val = val * cs
            val = val * (-1) ** ((y & x).bit_count() + (z & x).bit_count()) / r
            row.append(val)
        matrix.append(row)
    return matrix


def require_positive_definite(matrix):
    """Exact LDL; every pivot must be strictly positive in Q(sqrt(2))."""
    n = len(matrix)
    assert all((matrix[i][j] - matrix[j][i]).is_zero()
               for i in range(n) for j in range(n))
    lower = [[Q2(int(i == j)) for j in range(n)] for i in range(n)]
    diagonal = []
    for i in range(n):
        d = matrix[i][i] - sum((lower[i][j] ** 2 * diagonal[j]
                               for j in range(i)), Q2())
        assert d.sign() > 0, ('nonpositive LDL pivot', i, d.json())
        diagonal.append(d)
        for j in range(i + 1, n):
            lower[j][i] = (matrix[j][i] - sum(
                (lower[j][h] * lower[i][h] * diagonal[h] for h in range(i)), Q2())) / d


def check_certificate(row):
    k, r = row['k'], row['r']
    support = [x for x in range(2 ** k) if x.bit_count() <= row['radius']]
    assert len(support) == r == k + 1 and r & (r - 1) == 0
    v = F(row['v'])
    a, b = (1 - k * v * v) / (1 + k * v * v), 2 * v / (1 + k * v * v)
    W = [[a] + [b] * k] + [
        [b] + [-int(i == j) + (1 - a) / k for j in range(k)] for i in range(k)]
    assert all(sum(W[h][i] * W[h][j] for h in range(r)) == int(i == j)
               for i in range(r) for j in range(r))
    dual = [[F(x) for x in line] for line in row['H']]
    assert len(dual) == r and all(len(line) == r for line in dual)
    total = [[Q2() for _ in range(r)] for _ in range(r)]
    lower, pgm = Q2(), Q2()
    for x in range(2 ** k):
        sx = sigma(k, support, x)
        for i in range(r):
            for j in range(r):
                total[i][j] = total[i][j] + sx[i][j]
        prior = sum((sx[i][i] for i in range(r)), Q2())
        pgm = pgm + r * prior ** 2
        if x in support:
            column = support.index(x)
            lower = lower + sum((W[i][column] * W[j][column] * sx[i][j]
                                 for i in range(r) for j in range(r)), Q2())
        require_positive_definite([[Q2(dual[i][j]) - sx[i][j]
                                    for j in range(r)] for i in range(r)])
    assert all((total[i][j] - F(int(i == j), r)).is_zero()
               for i in range(r) for j in range(r))
    upper = sum(dual[i][i] for i in range(r))
    assert lower.json() == row['lower_exact']
    assert upper == F(row['upper_exact'])
    displayed_lower = F('0.8010769969' if k == 3 else '0.4609687373')
    assert (lower - displayed_lower).sign() > 0
    assert (Q2(upper) - lower).sign() > 0
    beta = Q2(F(1, 2), F(1, 4))
    store = beta ** (k - (r.bit_length() - 1))
    assert (store - upper).sign() > 0
    assert (pgm - upper * upper).sign() > 0
    return {'k': k, 'r': r, 'm': r.bit_length() - 1,
            'lower_display_rational': str(displayed_lower), 'lower_exact': lower.json(),
            'upper_exact': str(upper), 'pgm_exact': pgm.json(),
            'exact_dual_constraints': 2 ** k,
            'strictly_below_store_and_breidbart': True,
            'strictly_below_sqrt_pgm': True}


def floor_q2(x):
    # Floating point suggests a candidate only; exact inequalities certify it.
    candidate = math.floor(float(x.a) + math.sqrt(2) * float(x.b))
    while (x - candidate).sign() < 0:
        candidate -= 1
    while (x - (candidate + 1)).sign() >= 0:
        candidate += 1
    assert (x - candidate).sign() >= 0 and (x - (candidate + 1)).sign() < 0
    return candidate


def log_bounds(x):
    """Rational log enclosure by range reduction and the atanh series."""
    assert x > 0
    if x < 1:
        lo, hi = log_bounds(1 / x)
        return -hi, -lo
    power = 0
    while x > 2:
        x /= 2
        power += 1

    def unit(z):
        u = (z - 1) / (z + 1)
        terms = 60
        value = sum((2 * u ** (2 * j + 1) / (2 * j + 1)
                     for j in range(terms)), F(0))
        tail = 2 * u ** (2 * terms + 1) / ((2 * terms + 1) * (1 - u * u))
        return value, value + tail

    lo, hi = unit(x)
    l2, h2 = unit(F(2))
    return lo + power * l2, hi + power * h2


def check_diagonal_parameters():
    rows = []
    for s in (4, 5, 6):
        k, b, L = 2 ** (4 * s), 2 ** (3 * s), 2 ** (2 * s)
        h = k // 2 - b
        # The displayed t is k/2 - sqrt(2)(b+2L), rounded down.
        t = floor_q2(Q2(F(k, 2), -b - 2 * L))
        eta = Q2(0, F(1, 2))
        mean = Q2(F(k, 2), F(2 * t - k, 4))
        assert 0 <= t <= k and h >= 3 * L + 2 and L * L == k
        assert (mean - (Q2(h - 2 * L) - eta)).sign() > 0
        assert (Q2(h - 2 * L) - mean).sign() >= 0
        assert F(k, 8 * L * L) == F(1, 8)
        ratio = F(h - 3 * L, k - h + 3 * L + 1)
        prefactor = F(7, 8 * (3 * L + 2) * (k + 1))
        assert 0 < ratio < 1 and 0 < prefactor < 1
        log_pref_lo, _ = log_bounds(prefactor)
        log_ratio_lo, _ = log_bounds(ratio)
        log_lower = log_pref_lo + (3 * L + 1) * log_ratio_lo
        if s == 6:
            assert log_lower > -831 > -F(b * b, 3 * k)
        rows.append({'k': k, 'b': b, 'h': h, 'L': L, 'input_weight': t,
                     'dual_lower_prefactor': str(prefactor),
                     'dual_lower_base': str(ratio), 'dual_lower_power': 3 * L + 1,
                     'mean_and_variance_hypotheses_exact': True,
                     'diagonal_dual_at_least_exp_minus_831': s == 6,
                     'universal_success_log_upper_hoeffding': str(-F(b * b, 3 * k))})
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    certificate = Path(__file__).with_name('direct_discrimination_results.json')
    rows = json.loads(certificate.read_text())
    results = {'status': 'passed', 'arithmetic': 'exact rationals and Q(sqrt(2))',
               'scope': 'fixed encoders only; no universal exponent or k=3,m=1 improvement',
               'fixed_encoder_certificates': [check_certificate(row) for row in rows],
               'diagonal_dual_parameter_checks': check_diagonal_parameters()}
    output = json.dumps(results, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.write_text(output)
    print(output, end='')


if __name__ == '__main__':
    main()
