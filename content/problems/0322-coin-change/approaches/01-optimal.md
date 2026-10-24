## Idea

Create a table where entry `x` holds the fewest coins for amount `x`. Initialize amount zero to zero and every other amount to an impossible sentinel. For each amount in increasing order, try each coin that fits and keep the cheapest `1 + dp[x - coin]`.

## Why it works

Any solution for `x` ends with some coin `c`, and removing that coin leaves a solution for `x - c` that cannot be improved without improving the whole solution. Because `x - c < x`, the table already contains that smaller answer when it is needed. Taking the minimum over all final coins therefore finds the global optimum.

## Edge cases

- Amount zero needs no coins, so the answer is zero.
- A coin larger than the amount is skipped.
- If no combination reaches the target, the sentinel survives and `-1` is returned.
- One denomination that divides the amount produces a simple exact count.
- Duplicate denominations do not break the recurrence; they just repeat the same candidate.
