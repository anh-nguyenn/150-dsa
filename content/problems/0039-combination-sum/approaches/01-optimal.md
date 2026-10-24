## Idea

Sort the candidates and recursively spend the target. At each call, try each candidate from the current index onward, subtract it, and recurse with the same index so it can be used again. Stop the loop as soon as a value exceeds the remaining target.

## Why it works

Sorting means the current candidate and everything after it are at least as large as the current value, so once one is too big, all later choices are too big as well. Keeping the same index on the recursive call models unlimited reuse, while never moving backward keeps each combination in non-decreasing order and avoids permutations of the same answer.

## Edge cases

- If the smallest candidate is larger than the target, no branch can succeed and the result is empty.
- A candidate exactly equal to the target forms a one-element combination.
- Reusing a small candidate many times is allowed, so `[1, 1]` is valid for target 2 with candidate 1.
- The target is positive; no zero-length combination is returned.
