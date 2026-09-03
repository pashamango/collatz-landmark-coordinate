# Collatz landmark-coordinate verification

This repository is a minimal, reproducible handoff for a finite computational
test: an independent landmark-coordinate evaluator produced the same one-step
accelerated Collatz transitions as the ordinary direct evaluator over the
specified finite samples. This is not a proof of the Collatz conjecture.

## Evaluators

For a positive odd integer `n`, define the landmark coordinates by

```text
r(k) = ceil(k/2)
L_k = (4^r(k) - 1)/3
MATCH: maximal k >= 1 with n ≡ L_k (mod 2^k)
STRIP: q = (n - L_k)/2^k
RE-CENTER correction: c_k = 1 if k even, 2 if k odd
m_coordinate = 3q + c_k
```

The direct evaluator computes

```text
w = 3n + 1
k = v2(w)
m = w / 2^k
```

The comparison is meaningful because the coordinate decomposition gives the
algebraic identity

```text
3n + 1 = 2^k (3q + c_k)
```

The coordinate implementation does not call the direct evaluator or `v2`. It
discovers `k` from the landmark congruence and constructs the successor only as
`3*q + c_k`. Deterministic AST tests enforce this source-level separation.

## Observed finite result

```text
required cases: 1000
required transitions: 1000
required mismatches: 0
64-bit stretch cases: 1000
64-bit stretch mismatches: 0
seed: 0xC011A7
runtime used in original verification: Python 3.12.0
```

This is finite computational verification of an implementation and algebraic
identity, not evidence establishing the Collatz conjecture.

## Reproduction

Only the Python standard library is required.

```sh
python3 -m unittest tests.test_landmark_coordinate -v
python3 -m unittest discover -s tests -v
```

## Provenance

This publication repository is a distilled formal handoff of the merged result
from [`pashamango/minutta-rp-pr-cycle-lab`](https://github.com/pashamango/minutta-rp-pr-cycle-lab)
at immutable merge commit
`b8566df48946eea9a6748c63c90cdc42e5884ddd` (source PR #24). The implementation,
tests, and finite verification report are copied unchanged; only the report was
relocated from `rps/` to `report/`, and this README was added for the public
handoff.
