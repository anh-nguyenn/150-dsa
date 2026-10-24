## Idea

Reject an odd total immediately. Otherwise let `target` be half the total and create a boolean array of size `target + 1` with only index zero reachable. For each number, walk sums downward from `target` to the number and mark a sum reachable if the sum minus the number was already reachable. Return whether `target` is reachable.

## Why it works

Downward iteration is the 0/1 rule: when updating sum `s`, the value at `s - x` still belongs to the state before the current number, so the number is added at most once. Every subset is represented by the sequence of its elements, and each reachable sum corresponds to at least one such subset. Therefore the final mark at half the total is exactly the condition for an equal partition.

## Edge cases

- A single element cannot be split into two equal positive parts, so the answer is false.
- An odd total is rejected before any DP work.
- Duplicate values are separate items and are handled correctly by processing them one at a time.
- A target reached by one element is valid; the other group takes the rest.
- All numbers equal works when their count is even and fails when it is odd.
