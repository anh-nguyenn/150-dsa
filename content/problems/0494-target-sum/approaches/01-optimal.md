## Idea

Convert the sign choices into a subset sum. Let `goal` be the sum the plus-signed numbers must have. A one-dimensional table counts subsets for every sum up to `goal`. Each number is considered once, and totals are updated downward so that a number can be included at most once in any subset.

## Why it works

The equations `P - N = target` and `P + N = total` are equivalent to the original sign problem, and integer feasibility requires the parity and magnitude checks. Every sign assignment corresponds to exactly one plus-subset summing to `goal`, so counting those subsets counts the assignments. Descending updates preserve the once-per-number rule.

## Edge cases

- An odd `total + target` cannot split into two integer groups, so the answer is `0`.
- If `abs(target)` exceeds the total, no assignment can reach it.
- Zeros double the count because each zero has two signs but does not change the sum.
- A single number may or may not match the target.
- An empty list has one assignment, the empty sum, so it produces `1` only for target `0`.
