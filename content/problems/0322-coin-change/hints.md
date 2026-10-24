## Hint 1

Solve the smallest amounts first. What is the fewest coins needed for amount `x` if you already know the answers for amounts below `x`?

## Hint 2

If the last coin is worth `c`, the remaining amount is `x - c`. That is a smaller instance of the same question.

## Hint 3

Set `dp[0] = 0` and fill upward: `dp[x]` is one plus the best `dp[x-c]` over usable coins. Leave unreachable amounts as a sentinel and return `-1` for the target if it stays unreachable.
