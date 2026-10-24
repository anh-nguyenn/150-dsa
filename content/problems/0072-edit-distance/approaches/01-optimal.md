## Idea

Fill a table over prefixes. The first row and column hold the cost of building a prefix from nothing, which is just its length. For each pair of prefixes, equal final characters inherit the diagonal cost; unequal ones take one plus the best of the three neighboring costs.

## Why it works

Any edit script for the two prefixes must end by either deleting the last character of the first prefix, inserting the last character of the second, or pairing the two last characters. The three neighbors in the table represent exactly those cases. When the last characters match, pairing them is never worse than any alternative, so the diagonal value is optimal. The recurrence fills every state from states with smaller total prefix length, so the final cell is the minimum edit distance.

## Edge cases

- Two empty strings need zero edits.
- Converting an empty string to a non-empty one costs its length in insertions.
- Converting a non-empty string to an empty one costs its length in deletions.
- Identical strings return 0.
- Strings of length one differ by exactly one replacement when their characters differ.
- Swapping the arguments when the second is longer keeps the row width at `min(m, n)` without changing the answer.
