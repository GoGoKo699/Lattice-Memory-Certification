#!/usr/bin/env python3
"""Exact finite BB84/purity certificates, with separately labelled diagnostics.

The universal statements are proved in science/finite-guessing.md. This checker
verifies rational Gram identities, radical enclosures, every finite algebra
pair in the moment example, and one exact Hamming-ball method counterexample.
No see-saw or sampled strategy is an upper-bound certificate.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def sqrt_bounds(n: int, digits: int = 30) -> tuple[F, F]:
    scale = 10**digits
    a = math.isqrt(n * scale * scale)
    lo, hi = F(a, scale), F(a + 1, scale)
    require(lo * lo <= n < hi * hi, 'sqrt enclosure')
    return lo, hi


def log_unit_interval(x: F, terms: int = 100) -> tuple[F, F]:
    """Exact atanh series and positive geometric remainder, 1<=x<=2."""
    require(1 <= x <= 2, 'log unit interval')
    y = (x - 1) / (x + 1)
    total = sum((2 * y**(2*j + 1) / (2*j + 1) for j in range(terms)), F(0))
    tail = 2 * y**(2*terms + 1) / ((2*terms + 1) * (1 - y*y))
    return total, total + tail


def log_bounds(x: F) -> tuple[F, F]:
    require(x > 0, 'positive logarithm')
    if x < 1:
        lo, hi = log_bounds(1 / x)
        return -hi, -lo
    power = 0
    while x > 2:
        x /= 2
        power += 1
    lo, hi = log_unit_interval(x)
    l2, h2 = log_unit_interval(F(2))
    return lo + power*l2, hi + power*h2


def weighted_logs(terms: list[tuple[F, F]]) -> tuple[F, F]:
    lo = hi = F(0)
    for weight, x in terms:
        a, b = log_bounds(x)
        if weight >= 0:
            lo += weight*a; hi += weight*b
        else:
            lo += weight*b; hi += weight*a
    return lo, hi


def decimal_interval(interval: tuple[F, F], digits: int = 14) -> list[str]:
    """Outward decimal rounding, with no floating-point premise."""
    scale = 10**digits
    lo = interval[0] * scale
    hi = interval[1] * scale
    a = lo.numerator // lo.denominator
    b = -((-hi.numerator) // hi.denominator)
    def render(v: int) -> str:
        sign = '-' if v < 0 else ''
        v = abs(v)
        return f'{sign}{v // scale}.{v % scale:0{digits}d}'
    return [render(a), render(b)]


def swap(subset: tuple[int, ...]) -> np.ndarray:
    out = np.zeros((64, 64), dtype=np.int64)
    for col in range(64):
        bits = [(col >> (5-j)) & 1 for j in range(6)]
        for j in subset:
            bits[j], bits[j+3] = bits[j+3], bits[j]
        row = sum(bit << (5-j) for j, bit in enumerate(bits))
        out[row, col] = 1
    return out


def swap_certificate() -> dict:
    ident = np.eye(64, dtype=np.int64)
    fa, fb, fc = (swap((j,)) for j in range(3))
    fab, fabc = swap((0, 1)), swap((0, 1, 2))
    first = (ident-fab) @ (ident-fc)
    second = (ident-fa) @ (ident-fb)
    target = 2*ident + fabc - fa - fb - fc
    require(np.array_equal(target, first+second), 'swap sum identity')
    for gram in (first, second):
        require(np.array_equal(gram.T @ gram, 4*gram), 'rational Gram PSD identity')
    return {
        'dimension': 64,
        'identity': 'W=A+B=(A^T A+B^T B)/4',
        'integer_gram_identity': True,
        'W_sha256_int64_little_endian': hashlib.sha256(target.astype('<i8').tobytes()).hexdigest(),
        'scope': 'all states by the exact swap trace identity; no sampled eigenvalue claim',
    }


def finite_scalar_certificate() -> dict:
    s2 = sqrt_bounds(2); s7 = sqrt_bounds(7); s35 = sqrt_bounds(35)
    beta2 = tuple(F(3,8)+x/4 for x in s2)
    new = tuple(F(1,8)+7*x/16 for x in s2)
    old = tuple(F(1,8)+x/4 for x in s7)
    classical = tuple(F(5,16)+7*x/32 for x in s2)
    rank5 = tuple(F(1,8)+x/8 for x in s35)
    require(beta2[1] < new[0] < old[0], 'strict finite comparison')
    require(new[1] < F(93,125) < F(3,4) < old[0], 'strict moment comparison')
    # In Q(sqrt2), the upper root obeys 128p²-32p-47=0 exactly.
    a, b = F(1,8), F(7,16)
    require(128*(a*a+2*b*b)-32*a-47 == 0, 'quadratic constant coefficient')
    require(256*a*b-32*b == 0, 'quadratic sqrt coefficient')
    # Q <= 1/4+(3t0+S1)/32 <=5/16+t0/8 <=9/16.
    require(F(1,4)+F(2,32) == F(5,16), 'purity substitution constant')
    require(F(5,16)+F(2,8) == F(9,16), 'rank2 collision cap')
    require(classical[1] < F(311,500), 'classical rational cap')
    require(rank5[1] < F(173,200), 'rank5 rational cap')
    return {
        'pgm_upper_exact': '9/16',
        'score_upper_exact': '(2+7*sqrt(2))/16',
        'score_upper_interval': decimal_interval(new),
        'store_and_breidbart_interval': decimal_interval(beta2),
        'inherited_DFW_Renes_interval': decimal_interval(old),
        'score_upper_is_not_claimed_attainable': True,
        'finite_scalar_certificate_exact': True,
    }


def moment_certificate() -> dict:
    z = F(27,25)
    knots = [(F(1), F(1,8)), (z**2, F(1,2)), (z**3, F(311,500)),
             (z**4, F(93,125)), (z**6, F(1))]
    slopes = [(b[1]-a[1])/(b[0]-a[0]) for a,b in zip(knots,knots[1:])]
    require(all(a > b > 0 for a,b in zip(slopes,slopes[1:])), 'concave rational polygon')
    def polygon(x: F) -> F:
        for left, right in zip(knots,knots[1:]):
            if x <= right[0]:
                return left[1]+(x-left[0])*(right[1]-left[1])/(right[0]-left[0])
        return F(1)
    witnesses = []
    for r in range(7):
        for s in range(r//2+1):
            c = r-2*s
            dimension = min(F(1), F(2)**(s+c-3))
            candidates = [('output_dimension', dimension)]
            if s == 0:
                candidates.append(('classical_beta3_lt_311/500', F(311,500)))
            if s == 1:
                candidates.append(('finite_C3_lt_93/125', F(93,125)))
            if r == 5:
                candidates.append(('rank5_normalized_recovery_lt_173/200', F(173,200)))
            name, cap = min(candidates, key=lambda pair: pair[1])
            majorant = polygon(z**r)
            require(cap <= majorant, f'moment pair {(s,c)}')
            witnesses.append({'r':r,'s':s,'c':c,'witness':name,'cap':str(cap),
                              'polygon_value':str(majorant)})
    floor_moment = z**4+F(3,128)*(z**6-z**4)
    require(polygon(floor_moment) == F(3,4), 'score3/4 exact polygon inverse')
    require(floor_moment > z**4, 'moment floor strictly beyond4')
    return {'z':str(z),'knots':[[str(x),str(y)] for x,y in knots],
            'slopes':[str(x) for x in slopes], 'integer_pairs':witnesses,
            'score3/4_moment_floor_exact':str(floor_moment),
            'strict_profile_improvement':True}


def hamming_counterexample() -> dict:
    # k and b are integers, b=k^(3/4); every specified type count is integral.
    k, b = 2**20, 2**15
    delta = F(b,k)
    binary = weighted_logs([(F(1,2)-delta,1-2*delta),
                            (F(1,2)+delta,1+2*delta)])
    joint = weighted_logs([(F(3,8)+delta,1+F(8,3)*delta),
                           (F(3,8)-delta,1-F(8,3)*delta)])
    lk = log_bounds(F(k+1))
    exponent = F(2,5)
    # ln Q >= -k Dj -4ln(k+1)+k Db; ln u <= -k Db.
    # The strict inequality below proves Q > u^(2/5), without exponentiating.
    margin_lower = (1+exponent)*k*binary[0]-k*joint[1]-4*lk[1]
    require(margin_lower > 0, 'rank-sensitive exponent2/5 counterexample')
    require(margin_lower > exponent*log_bounds(F(2))[1],
            'counterexample survives next-power-of-two dimension rounding')
    ln_u = (-k*binary[1]-lk[1], -k*binary[0])
    ln_Q_lower = -k*joint[1]-4*lk[1]+k*binary[0]
    return {'k':k,'b':b,'hamming_radius':k//2-b,
            'joint_type_counts':[3*k//8+b,k//8,k//8,3*k//8-b],
            'log_rank_fraction_interval':decimal_interval(ln_u),
            'log_Q_lower':decimal_interval((ln_Q_lower,ln_Q_lower)),
            'strict_log_margin_for_Q_gt_u_power_2/5':decimal_interval((margin_lower,margin_lower)),
            'certificate':'exact rational atanh logarithm enclosures + type probability bounds',
            'integer_qubit_memory_rounding_also_certified':True,
            'scope':'counterexample to scalar rank-PGM exponent2/5, not to guessing exponent1/5'}


def dense_diagnostics() -> dict:
    ident=np.eye(2); x=np.array([[0,1],[1,0]]); y=np.array([[0,-1j],[1j,0]]); z=np.diag([1,-1])
    one=[ident,x,y,z]
    def tensor(ops):
        out=np.ones((1,1))
        for op in ops: out=np.kron(out,op)
        return out
    words=list(itertools.product(range(4),repeat=3))
    paulis=[tensor([one[j] for j in w]) for w in words]
    weights=np.array([0 if 2 in w else 2.**(-sum(j!=0 for j in w)) for w in words])
    rng=np.random.default_rng(20261105)
    max_identity_error=0.; max_q=0.
    for _ in range(40):
        b=rng.normal(size=(8,2))+1j*rng.normal(size=(8,2))
        r=b@b.conj().T;r/=np.linalg.norm(r)
        ts=np.array([np.trace(r@p).real**2 for p in paulis])
        q=float(weights@ts/8);t0=ts[0]
        s1=sum(v for w,v in zip(words,ts) if sum(j!=0 for j in w)==1)
        require(abs(ts.sum()-8)<1e-10,'dense Parseval')
        require(s1<=t0+2+1e-10,'dense purity')
        require(q<=9/16+1e-10,'dense Q bound')
        max_q=max(max_q,q)
        # All 64 Kraus operators of the flagged Pauli-twirl realization.
        psi=(rng.normal(size=(8,2))+1j*rng.normal(size=(8,2)))
        psi/=np.linalg.norm(psi)
        k=math.sqrt(8)*psi.T
        kraus=[k@p.T/8 for p in paulis]
        complete=sum(op.conj().T@op for op in kraus)
        max_identity_error=max(max_identity_error,float(np.max(np.abs(complete-np.eye(8)))))
        require(np.max(np.abs(complete-np.eye(8)))<1e-10,'dense Choi instrument trace preservation')
    return {'status':'passed','random_rank2_inputs':40,'seed':20261105,
            'largest_sampled_Q':max_q,'maximum_instrument_completeness_error':max_identity_error,
            'scope':'diagnostics only; no sampled optimization certifies the upper bound'}


def main() -> None:
    parser=argparse.ArgumentParser();parser.add_argument('--write',type=Path)
    args=parser.parse_args()
    report={'status':'passed','exact_swap_certificate':swap_certificate(),
            'finite_scalar_certificate':finite_scalar_certificate(),
            'moment_composition_certificate':moment_certificate(),
            'hamming_ball_method_counterexample':hamming_counterexample(),
            'dense_diagnostics':dense_diagnostics(),
            'limits':['The finite score upper bound is not proved optimal or attained.',
                      'The all-size guessing exponent remains1/6.',
                      'The Hamming-ball counterexample limits only scalar-PGM proof routes.',
                      'No tensorization against joint encoders or hardware-model verification is claimed.']}
    text=json.dumps(report,sort_keys=True,indent=2)+'\n'
    if args.write:
        args.write.parent.mkdir(parents=True,exist_ok=True);args.write.write_text(text,encoding='utf-8')
    print(text,end='')


if __name__=='__main__':
    main()
