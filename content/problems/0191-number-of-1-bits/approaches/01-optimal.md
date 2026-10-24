## Idea

Repeatedly remove the lowest set bit with `n & (n - 1)`. Each removal counts one 1 bit, and the loop ends after all set bits are gone.

## Why it works

For any non-zero `n`, subtracting 1 clears the least significant 1 and sets every lower bit to 1. ANDing with the original clears that bit and only that bit. Since each iteration removes exactly one 1, the loop runs once per set bit and terminates at zero.

## Edge cases

- `0` has no set bits, so the loop is skipped and the count is 0.
- Powers of two have exactly one set bit and finish in one iteration.
- The largest 32-bit value has all bits set and needs 32 iterations.
- Using a fixed 32-iteration loop also works, but this approach stops early for sparse numbers.
