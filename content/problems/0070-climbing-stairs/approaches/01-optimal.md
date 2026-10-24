## Idea

Track the number of routes to the current step using the two previous counts. The base cases are one route to step 1 and two routes to step 2; each later count is the sum of the previous two.

## Why it works

Every route to step `k` ends in exactly one of two ways: a single step from `k - 1`, or a double step from `k - 2`. Those groups do not overlap and together cover all routes, so the counts add. The rolling variables keep the two values the recurrence needs, and the loop invariant is that they hold the counts for the last two steps.

## Edge cases

- `n = 1`: the loop never runs and the answer is 1.
- `n = 2`: the second base value is returned directly.
- `n = 45`: the result is 1,836,311,903, which fits in a signed 32-bit integer.
- No zero or negative input is allowed, so the base cases cover the whole lower end.
