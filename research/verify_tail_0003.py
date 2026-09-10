"""Bounded exact-arithmetic checks for COLLATZ-TAIL-0003; no dependencies."""
import itertools
import json
import platform
from fractions import Fraction as F
from pathlib import Path
from collatz.landmark_coordinate import direct_successor, coordinate_successor


def valuation(x):
    x = F(x)
    def v(a):
        a = abs(a)
        return (a & -a).bit_length() - 1
    assert x
    return v(x.numerator) - v(x.denominator)


def periodic(word):
    s = 0
    a = F(0)
    for j, k in enumerate(word):
        a += F(2**s, 3**(j+1))
        s += k
    return -a / (1 - F(2**s, 3**len(word)))


def main():
    out = {'python': platform.python_version(), 'arithmetic': 'exact integers and fractions'}
    count = 0
    dictionary_checks = 0
    for start in range(1, 200, 2):
        n, s, a = start, 0, F(0)
        for j in range(32):
            k, m = direct_successor(n)
            t = n
            for offset in range(k):
                assert (t & 1) == (1 if offset == 0 else 0)
                t = (3*t+1)//2 if t & 1 else t//2
            assert t == m and t & 1
            dictionary_checks += 1
            assert coordinate_successor(n)[:2] == (k, m)
            a += F(2**s, 3**(j+1))
            s += k
            remainder = F(2**s * m, 3**(j+1))
            assert F(start) == -a + remainder
            assert valuation(F(start)+a) == s
            n = m
            count += 1
    out['finite_identity_and_exact_remainder_checks'] = count
    out['shortcut_run_dictionary_checks'] = dictionary_checks
    # Independent full parity-word inverse test, including words ending in zeros.
    inverse_count = 0
    for length in range(1, 13):
        mod = 2**length
        seen = set()
        for word in range(mod):
            x, j = 0, 0
            for d in range(length):
                if (word >> d) & 1:
                    x -= 2**d * pow(3**(j+1), -1, mod)
                    j += 1
            x %= mod
            seen.add(x)
            n, got = x, 0
            for d in range(length):
                bit = n & 1
                got |= bit << d
                n = (3*n+1)//2 if bit else n//2
            assert got == word
            inverse_count += 1
        assert len(seen) == mod
    out['all_parity_words_lengths_1_to_12'] = inverse_count
    # Exact K prefix fixes a cylinder modulo 2^(s_J+1), not just 2^s_J.
    cylinders = 0
    for length in range(1, 5):
        for word in itertools.product(range(1, 5), repeat=length):
            s, a = 0, F(0)
            for j, k in enumerate(word):
                a -= F(2**s, 3**(j+1))
                s += k
            center = a + F(2**s, 3**length)
            mod = 2**(s+1)
            residue = center.numerator * pow(center.denominator, -1, mod) % mod
            for lift in range(3):
                n = residue + lift*mod
                for k in word:
                    got, n = direct_successor(n)
                    assert got == k
            cylinders += 1
    out['exact_run_prefix_cylinders_three_positive_lifts_each'] = cylinders
    cycles = 0
    for length in range(1, 5):
        for word in itertools.product(range(1, 5), repeat=length):
            start = n = periodic(word)
            for k in word:
                assert valuation(n) == 0
                assert valuation(3*n+1) == k
                n = (3*n+1)/2**k
            assert n == start
            cycles += 1
    out['periodic_rational_words_checked'] = cycles
    out['constant_run_examples'] = {str(k): str(periodic((k,))) for k in range(1, 6)}
    carries = {}
    for base in (2, 4):
        states, frontier = {1}, [1]
        while frontier:
            c = frontier.pop()
            for a in range(base):
                nxt = (3*a+c)//base
                if nxt not in states:
                    states.add(nxt)
                    frontier.append(nxt)
        assert states == {0, 1, 2}
        carries[str(base)] = sorted(states)
    out['reachable_multiply_3_add_1_carries'] = carries
    out['gamma_code_lengths_vs_raw_run_bits'] = {
        str(k): {'gamma': 2*k.bit_length()-1, 'raw': k} for k in (1,2,3,4,8,16,64)
    }
    out['status'] = 'PASS'
    target = Path(__file__).with_name('COLLATZ-TAIL-0003-EXPERIMENTS.json')
    target.write_text(json.dumps(out, indent=2)+'\n')
    print(target.read_text())

if __name__ == '__main__':
    main()
