## Idea

Fill the permutation left to right. At every position try each number whose index is not currently used, mark it used, recurse, then unmark it so another branch can place it elsewhere.

## Why it works

A permutation is exactly a sequence of all indices with no repetition. The recursion considers every unused index at every position, so every such sequence is generated once. Backtracking removes each choice before trying the next one, which keeps the state correct across branches. Copying the path only at full length ensures partial orderings are not reported.

## Edge cases

- A single number has exactly one permutation.
- An empty input returns `[[]]`, the empty ordering.
- Negative numbers are placed like any other value.
- Distinct input values mean no duplicate permutations need to be filtered.
