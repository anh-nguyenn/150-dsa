## Idea

Separate the addition into a carry-free sum and a set of carries. XOR produces the sum bits, AND plus a left shift produces the carries, and feeding the carries back in repeats the process until none remain.

## Why it works

At every bit, XOR matches the sum without carry, and AND marks positions where both bits are 1. Shifting that mask left places each carry in the next column. Iterating until the carry word is zero means no position needs further adjustment, so the accumulated sum is final. Masking to 32 bits models fixed-width signed arithmetic and prevents Python's unbounded negative representation from looping forever.

## Edge cases

- Adding 0 to a value returns that value without any carry iterations.
- Opposite signs such as `-1` and `1` cancel to 0.
- Two negative values produce a negative result after the final sign conversion.
- The inputs fit in 32 bits, so no overflow beyond the masked word occurs.
