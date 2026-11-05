#!/usr/bin/env python3
"""Exact finite BB84/purity certificates, with separately labelled diagnostics.

The universal statements are proved in science/finite-guessing.md. This checker
verifies rational Gram and swap-sector identities, attained collision maxima
at three, four and five inputs, radical enclosures, every finite algebra pair
in the moment example, and one exact Hamming-ball method counterexample.
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


def binomial(n: int, j: int) -> int:
    return math.comb(n, j) if 0 <= j <= n else 0


def swap_sector_coefficients(k: int, h: int) -> list[F]:
    """Coefficients of A_j in 2^k Tr[(R tensor R) E_h], equation (F6b)."""
    krawtchouk = [sum((-1)**a * binomial(ell, a) * binomial(k-ell, h-a)
                     for a in range(h+1)) for ell in range(k+1)]
    return [sum((F(krawtchouk[ell] * binomial(k-j, ell-j), 2**ell)
                 for ell in range(j, k+1)), F(0)) for j in range(k+1)]


def check_swap_sectors(k: int) -> list[list[F]]:
    """Exact projector eigenvalues and an independent subset expansion."""
    masks = range(2**k)
    sectors = [[mask for mask in masks if mask.bit_count() == h]
               for h in range(k+1)]
    for negative in masks:
        eigenvalues = []
        for sector in sectors:
            # Evaluate the explicit products (I +/- F_i)/2 on a joint
            # swap eigenspace. Nonnegative 0/1 values certify the projectors.
            value = F(0)
            for mask in sector:
                product = 1
                for i in range(k):
                    swap_sign = -1 if negative & (1 << i) else 1
                    product *= 1-swap_sign if mask & (1 << i) else 1+swap_sign
                value += F(product, 2**k)
            require(value in (0, 1), 'local swap-sector projector eigenvalue')
            eigenvalues.append(value)
        require(sum(eigenvalues) == 1, 'local swap sectors partition identity')
        require(eigenvalues[negative.bit_count()] == 1, 'sector label')

    coefficients = [swap_sector_coefficients(k, h) for h in range(k+1)]
    for h, sector in enumerate(sectors):
        for j in range(k+1):
            support = (1 << j)-1
            # For a fixed support, expand each projector over all swap
            # subsets, then use the reduced-purity Pauli trace identity.
            expanded = sum((F(sum((-1)**((mask & subset).bit_count())
                                  for mask in sector), 2**subset.bit_count())
                            for subset in masks if subset & support == support), F(0))
            require(expanded == coefficients[h][j], 'swap-to-Pauli subset expansion')
    return coefficients


def normalized_spectral_cap(k: int, retained_dimension: int) -> F:
    """Exact normalized DFW relaxation, including all 2^j binomial(k,j) labels."""
    remaining = F(1)
    cap = F(retained_dimension, 2**k)
    score = F(0)
    for j in range(k+1):
        mass = min(remaining, 2**j * binomial(k, j) * cap)
        score += mass / 2**j
        remaining -= mass
    require(remaining == 0, 'normalized spectral weights filled')
    return score


def breidbart_power(power: int) -> tuple[F, F]:
    """Return a,b with beta^power=a+b sqrt(2), exactly."""
    a, b = F(1), F(0)
    for _ in range(power):
        a, b = a/2+b/2, a/4+b/2
    return a, b


def finite_swap_sector_certificates() -> dict:
    cases = {
        4: {'alpha': F(7,512), 'beta': F(13,128),
            'sectors': [(2,F(1,64))], 'last': F(1,256),
            'collision': F(27,64), 'radicand': 345,
            'score_a': F(1,16), 'score_b': F(1,32),
            'score_exact': '(2+sqrt(345))/32',
            'expected_H': {2: [27,-9,-1,3,3]},
            'H_q_scale': {2: 8}, 'spectral': F(9,16)},
        5: {'alpha': F(21,4096), 'beta': F(39,512),
            'sectors': [(2,F(3,512)), (5,F(5,256))], 'last': F(3,1024),
            'collision': F(81,256), 'radicand': 4526,
            'score_a': F(1,32), 'score_b': F(1,128),
            'score_exact': '(4+sqrt(4526))/128',
            'expected_H': {2: [135,-27,-9,5,7,5], 5: [1,-1,1,-1,1,-1]},
            'H_q_scale': {2: 16, 5: 32}, 'spectral': F(29,64)},
    }
    results = {}
    s2 = sqrt_bounds(2)
    for k, case in cases.items():
        d = 2**k
        coefficients = check_swap_sectors(k)
        for h, expected in case['expected_H'].items():
            require([case['H_q_scale'][h]*x for x in coefficients[h]] == expected,
                    f'k{k} explicit positive sector polynomial')
        for j in range(k+1):
            rhs = case['alpha'] + (case['beta'] if j == 0 else 0)
            rhs -= sum(weight*coefficients[h][j] for h,weight in case['sectors'])
            rhs -= case['last'] if j == k else 0
            require(rhs == F(1,2**(k+j)), f'k{k} exact dual coefficient {j}')
        collision = case['alpha']*d + 2*case['beta']
        require(collision == case['collision'], f'k{k} rank2 specialization')

        # I/sqrt(2) tensor a real pure state on every remaining site:
        # A_j=2 binomial(k-1,j), and every Y coefficient is zero.
        product_weights = [2*binomial(k-1,j) for j in range(k+1)]
        require(sum(product_weights) == d, 'matching product Parseval')
        for h in range(k+1):
            sector = sum(x*y for x,y in zip(coefficients[h],product_weights))
            require(sector >= 0, 'matching product sector positivity')
            if h >= 2:
                require(sector == 0, 'matching product has at most one antisymmetric pair')
        achieved = sum((F(value,2**(k+j)) for j,value in enumerate(product_weights)), F(0))
        require(achieved == collision == F(3,4)**(k-1), 'exact collision attainment')

        a,b,n = case['score_a'], case['score_b'], case['radicand']
        # d p^2-2p+1-(d-1)Q=0 in Q(sqrt(n)); positive branch is >1/d.
        require(d*(a*a+n*b*b)-2*a+1-(d-1)*collision == 0,
                'Renes quadratic constant coefficient')
        require(2*d*a*b-2*b == 0, 'Renes quadratic radical coefficient')
        upper = tuple(a+b*x for x in sqrt_bounds(n))
        require(upper[0] > F(1,d), 'Renes upper root selected')
        la,lb = breidbart_power(k-1)
        lower = tuple(la+lb*x for x in s2)
        require(lower[1] < upper[0] < 1, 'strict guessing gap remains open')
        inherited_spectral = normalized_spectral_cap(k,2)
        require(inherited_spectral == case['spectral'], 'normalized DFW comparison')
        require(collision**3 < F(2,d) < inherited_spectral**3,
                'new collision < hypercontractive collision < spectral collision')
        results[str(k)] = {
            'retained_quantum_dimension':2,
            'projector_joint_eigenspaces_checked':d,
            'swap_sector_expansion_exact':True,
            'positive_sector_polynomials':{
                str(h):{'A_coefficients':values,
                        'multiple_of_sector_expectation':d*case['H_q_scale'][h]}
                for h,values in case['expected_H'].items()},
            'coefficient_identity_exact':True,
            'collision_maximum_exact':str(collision),
            'collision_maximum_attained':True,
            'attaining_product_weight_sums':product_weights,
            'score_upper_exact':case['score_exact'],
            'score_upper_interval':decimal_interval(upper),
            'store_and_breidbart_interval':decimal_interval(lower),
            'score_upper_is_not_claimed_attainable':True,
            'inherited_normalized_DFW_collision_exact':str(inherited_spectral),
            'strict_improvement_over_hypercontractive_and_spectral_caps':True,
        }
    return results


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


def swap_sector_matrix_diagnostics() -> dict:
    """Check the exact algebra against partial traces of actual matrices."""
    one = [np.eye(2), np.array([[0,1],[1,0]]),
           np.array([[0,-1j],[1j,0]]), np.diag([1,-1])]
    def tensor(ops):
        out = np.ones((1,1))
        for op in ops:
            out = np.kron(out,op)
        return out
    def reduced(matrix, k, keep):
        out = matrix.reshape([2]*(2*k))
        current = k
        for i in range(k-1,-1,-1):
            if i not in keep:
                out = np.trace(out, axis1=i, axis2=i+current)
                current -= 1
        return out.reshape(2**len(keep),2**len(keep))

    rng = np.random.default_rng(20261106)
    results = {}
    for k in (4,5):
        d = 2**k
        words = list(itertools.product(range(4),repeat=k))
        paulis = np.array([tensor([one[j] for j in w]) for w in words])
        pauli_weights = np.array([sum(j!=0 for j in w) for w in words])
        multipliers = np.array([0 if 2 in w else 2.**(-weight)
                                for w,weight in zip(words,pauli_weights)])
        coefficients = np.array([swap_sector_coefficients(k,h) for h in range(k+1)],float)
        vectors = [rng.normal(size=(d,2))+1j*rng.normal(size=(d,2)) for _ in range(6)]
        matrices = []
        for vector in vectors:
            matrix = vector@vector.conj().T
            matrices.append(matrix/np.linalg.norm(matrix))
        b = np.array([math.cos(math.pi/8),math.sin(math.pi/8)])
        matrices.append(tensor([np.eye(2)/math.sqrt(2)]+[np.outer(b,b)]*(k-1)))
        max_trace_error = 0.
        max_q = 0.
        product_q = None
        for index,matrix in enumerate(matrices):
            traces = np.einsum('ij,pji->p',matrix,paulis)
            require(np.max(np.abs(traces.imag)) < 1e-10, 'Hermitian Pauli coefficients real')
            ts = traces.real**2
            weights = np.bincount(pauli_weights,weights=ts,minlength=k+1)
            require(abs(sum(weights)-d) < 1e-9, 'four/five input dense Parseval')
            q = float(multipliers@ts/d)
            relaxed = float(sum(weights[j]/2**j for j in range(k+1))/d)
            require(q <= relaxed+1e-10, 'Y-discarding collision relaxation')
            require(q <= (3/4)**(k-1)+1e-10, 'four/five input dense collision cap')
            max_q = max(max_q,q)
            swap_traces = []
            for subset in range(d):
                keep = {i for i in range(k) if subset & (1<<i)}
                marginal = reduced(matrix,k,keep)
                swap_traces.append(float(np.trace(marginal@marginal).real))
            for h in range(k+1):
                direct = sum(sum((-1)**a*binomial(subset.bit_count(),a)
                                 *binomial(k-subset.bit_count(),h-a)
                                 for a in range(h+1))*value
                             for subset,value in enumerate(swap_traces))/d
                from_paulis = float(coefficients[h]@weights/d)
                error = abs(direct-from_paulis)
                max_trace_error = max(max_trace_error,error)
                require(error < 1e-10, 'independent partial-trace swap-sector identity')
                require(direct >= -1e-10, 'dense swap-sector positivity')
            if index == len(matrices)-1:
                product_q = q
                require(abs(q-(3/4)**(k-1)) < 1e-10, 'matrix product attains collision cap')
                expected = np.array([2*binomial(k-1,j) for j in range(k+1)])
                require(np.max(np.abs(weights-expected)) < 1e-9, 'matrix product weight sums')
        results[str(k)] = {'random_rank2_inputs':6,'matching_product_input':True,
                           'largest_sampled_Q':max_q,'matching_product_Q':product_q,
                           'maximum_swap_trace_identity_error':max_trace_error}
    return {'status':'passed','seed':20261106,'cases':results,
            'scope':'matrix diagnostics only; exact upper bounds come from the rational certificates'}


def main() -> None:
    parser=argparse.ArgumentParser();parser.add_argument('--write',type=Path)
    args=parser.parse_args()
    report={'status':'passed','exact_swap_certificate':swap_certificate(),
            'finite_scalar_certificate':finite_scalar_certificate(),
            'four_five_input_swap_sector_certificates':finite_swap_sector_certificates(),
            'moment_composition_certificate':moment_certificate(),
            'hamming_ball_method_counterexample':hamming_counterexample(),
            'dense_diagnostics':dense_diagnostics(),
            'swap_sector_matrix_diagnostics':swap_sector_matrix_diagnostics(),
            'limits':['The three finite guessing upper bounds are not proved optimal or attained.',
                      'The collision maxima at three, four and five inputs with one retained qubit are attained.',
                      'The all-size guessing exponent remains1/6.',
                      'The Hamming-ball counterexample limits only scalar-PGM proof routes.',
                      'No tensorization against joint encoders or hardware-model verification is claimed.']}
    text=json.dumps(report,sort_keys=True,indent=2)+'\n'
    if args.write:
        args.write.parent.mkdir(parents=True,exist_ok=True);args.write.write_text(text,encoding='utf-8')
    print(text,end='')


if __name__=='__main__':
    main()
