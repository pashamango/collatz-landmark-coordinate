"""Exact finite K-prefix certificates for positive odd Collatz states.

The runs select one odd residue modulo 2**(S+1), where S is their total
length.  One nonnegative quotient then selects the ordinary integer in that
cylinder.  The quotient is the only unbounded datum needed beyond the prefix.
"""

from typing import Any

from .landmark_coordinate import direct_successor


def _residue(runs: tuple[int, ...]) -> tuple[int, int]:
    """Return (residue, modulus) for the exact prefix's odd cylinder."""
    if not runs or any(type(k) is not int or k < 1 for k in runs):
        raise ValueError("runs must be a nonempty tuple of positive integers")
    total = sum(runs)
    modulus = 1 << (total + 1)
    value = 1  # any odd terminal value has the same residue modulo 2**(S+1)
    inv3 = pow(3, -1, modulus)
    for k in reversed(runs):
        value = ((1 << k) * value - 1) * inv3 % modulus
    return value, modulus


def encode_prefix(n: int, steps: int) -> dict[str, Any]:
    """Encode the first ``steps`` accelerated runs of positive odd ``n``."""
    if type(n) is not int or n <= 0 or n % 2 == 0:
        raise ValueError("n must be a positive odd integer")
    if type(steps) is not int or steps < 1:
        raise ValueError("steps must be a positive integer")
    state = n
    runs: list[int] = []
    for _ in range(steps):
        k, state = direct_successor(state)
        runs.append(k)
    residue, modulus = _residue(tuple(runs))
    if n < residue or (n - residue) % modulus:
        raise AssertionError("prefix residue construction failed")
    return {"runs": runs, "quotient": (n - residue) // modulus}


def decode_certificate(certificate: dict[str, Any]) -> tuple[int, tuple[int, ...]]:
    """Verify and decode a certificate, returning (n, exact trajectory runs)."""
    if not isinstance(certificate, dict):
        raise ValueError("certificate must be an object")
    runs_raw = certificate.get("runs")
    quotient = certificate.get("quotient")
    if not isinstance(runs_raw, list):
        raise ValueError("runs must be a list")
    if type(quotient) is not int or quotient < 0:
        raise ValueError("quotient must be a nonnegative integer")
    runs = tuple(runs_raw)
    residue, modulus = _residue(runs)
    n = residue + modulus * quotient
    if n <= 0 or n % 2 == 0:
        raise ValueError("decoded state is not positive odd")
    state = n
    for expected in runs:
        actual, state = direct_successor(state)
        if actual != expected:
            raise ValueError("run prefix is not exact for decoded state")
    return n, runs
