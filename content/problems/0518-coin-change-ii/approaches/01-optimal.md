## Idea

Let `ways[t]` be the number of combinations that make total `t` using the coin types processed so far. Initially only total 0 has one way: the empty combination. For each new coin, scanning totals upward lets `ways[t - coin]` already include combinations that use this coin, so any number of copies is allowed without reordering.

## Why it works

When a coin type is processed, each combination for total `t` either contains none of that coin, already counted in `ways[t]`, or contains at least one copy, in which case removing one copy leaves a combination for `t - coin`. Processing coin types in a fixed outer loop assigns every combination a unique construction order, so permutations are not overcounted.

## Edge cases

- `amount = 0` gives `1`: the empty selection is the only combination.
- If no combination fits, the answer is `0`.
- A single denomination either divides the amount exactly or contributes nothing.
- Coins larger than the amount are skipped by the loop's starting point.
- Large amounts rely on the table size rather than on enumerating combinations.
