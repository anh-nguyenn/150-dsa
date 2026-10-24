## Idea

Strip digits from the right of the absolute value and build the answer from the left. Restore the sign, then reject anything outside the signed 32-bit interval.

## Why it works

Each iteration removes one decimal digit and appends it to the reverse, so after the loop every digit is in the opposite position. Using the absolute value avoids Python's floor-division behavior with negative remainders, and applying the sign once at the end preserves the correct sign. The final range check enforces the stated 32-bit limit.

## Edge cases

- `0` has no loop iterations and returns 0.
- Trailing zeros such as `120` become `21` because leading zeros in the reverse are not stored.
- A negative input keeps its sign, for example `-123` becomes `-321`.
- Values whose reverse overflows, such as `1534236469`, return 0; valid near-limit values such as `1463847412` return `2147483641`.
