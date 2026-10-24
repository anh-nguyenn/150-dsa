## Hint 1

Start with the smallest inputs. For two steps, what are the only ways to get past the top, and what does each cost?

## Hint 2

Define the cheapest cost of standing on a particular step. Which earlier steps could you have come from, and what would you have paid to leave them?

## Hint 3

Use `dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])` with `dp[0] = dp[1] = 0`; the top is the virtual step `n`, and two rolling variables are enough.
