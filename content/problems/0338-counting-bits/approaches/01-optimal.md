## Idea

Fill an array from 0 upward. Each entry reuses the count of the number obtained by dropping the last bit, then adds that last bit back.

## Why it works

Right-shifting `i` by one deletes its least significant bit, so `i >> 1 < i`. Its count is already computed. The deleted bit is `i & 1`, which is 0 or 1. Adding it produces exactly the count for `i`, and starting with `bits[0] = 0` anchors the recurrence.

## Edge cases

- `n = 0` returns `[0]`; the loop body never runs.
- Odd and even values are handled by the added `i & 1` term.
- Powers of two correctly get a count of 1 because their shifted value is a previous power of two.
- The maximum `n` only needs a table of length 100,001, which is well within memory limits.
