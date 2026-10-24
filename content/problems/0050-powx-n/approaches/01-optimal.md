## Idea

Repeatedly square the base while reading the exponent in binary, multiplying the current base into the answer whenever the low bit is set.

## Why it works

After `k` rounds the base holds `x^(2^k)`, so the powers needed for the binary expansion of `n` are available exactly when their bit is set. Multiplying those selected powers together gives `x^n`. Halving `n` each round discards the bit just examined, and the loop ends when no bits remain. Inverting the base for a negative exponent uses `x^(-n) = (1/x)^n`.

## Edge cases

- `n = 0` returns `1.0` even when `x` is zero.
- A negative exponent inverts the base first; a zero base with a negative exponent is outside the stated domain.
- The smallest 32-bit exponent is safe in Python because negating it does not overflow.
- Negative bases keep their sign when the exponent is odd and lose it when the exponent is even.
- Underflow for very large negative exponents produces `0.0`, matching floating-point behavior.
