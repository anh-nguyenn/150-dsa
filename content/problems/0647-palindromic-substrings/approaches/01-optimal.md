## Idea

Visit all `2n - 1` centres. At each centre, expand while the characters match and increment a counter for each matching layer. Summing those counters gives the total number of palindromic substrings.

## Why it works

Each palindrome has a unique centre, and the expansion from that centre meets it exactly once, at a specific radius. Matching layers correspond one-to-one with palindromic substrings, so counting layers counts palindromes without duplicates. Each centre expands at most `O(n)` times, giving `O(n^2)` time and constant extra space.

## Edge cases

- A single character: one odd centre contributes 1.
- All identical characters: every centre contributes its full expansion, giving `n(n+1)/2`.
- Even-length palindromes are counted by the gap centres.
- No matches beyond the first layer simply stop the expansion.
