## Idea

Let `prev[j]` be the best answer for the first `i - 1` characters of the row string and the first `j` characters of the column string, and let `cur[j]` be the same for the first `i` characters. If the new row character equals the column character at `j`, extend the diagonal answer by one. Otherwise carry forward the better answer obtained by skipping a character from either string.

## Why it works

When the two current characters match, some optimal common subsequence can end with that matched pair, so extending the diagonal is safe. When they do not match, any common subsequence must omit at least one of the two current characters, which is exactly what the two carry-forward options represent. Processing prefixes from short to long makes every needed smaller state available.

## Edge cases

- An empty string on either side gives `0`.
- Identical strings have the full length as their answer.
- Strings with no character in common give `0`.
- A single character matches at most once, even if it repeats in the other string.
- Swapping the inputs does not change the answer, which is why the shorter string can be placed along the columns.
