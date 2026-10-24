## Idea

Process the numbers in order and maintain a sorted list `tails`. For each number, binary search for the first entry that is greater than or equal to it. Replace that entry, or append if no such entry exists. The final list length is the length of the longest increasing subsequence.

## Why it works

`tails[k]` is the smallest possible last value of an increasing subsequence of length `k + 1`. A smaller last value is always at least as easy to extend, so keeping only the minimum is safe. Replacing the first entry not smaller than the current number preserves the invariant, and appending happens exactly when a longer subsequence becomes possible. The list therefore grows to the optimal length.

## Edge cases

- Equal values do not increase the length; the lower-bound search replaces the existing equal tail.
- A strictly decreasing array leaves a list of length one.
- A single element returns one.
- Negative values work normally because only comparisons matter.
- Duplicates in increasing runs are ignored rather than counted twice.
