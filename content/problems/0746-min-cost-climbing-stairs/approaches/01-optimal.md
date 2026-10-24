## Idea

Define `dp[i]` as the minimum toll paid to stand on step `i`, with `dp[0] = dp[1] = 0` because either starting step is free. For each later position, add the cost of the step you leave to the cheaper of the two possible origins. The answer is `dp[n]`, the virtual step past the end.

## Why it works

A cheapest route to step `i` must have come from `i - 1` or `i - 2`; any other predecessor skips over `i` or overshoots. Paying `cost[i-1]` or `cost[i-2]` respectively accounts for the toll of the step being left. Since only the last two values are read, rolling variables preserve the recurrence without a table.

## Edge cases

- A one-element list: the top is reachable for free from the starting position, so the answer is 0.
- Two steps: the answer is the smaller of the two tolls.
- Zero-cost steps: the recurrence still works and may produce 0.
- Starting on step 1 is always allowed, which is why `dp[1]` is 0 rather than `cost[0]`.
