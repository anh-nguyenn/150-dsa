## Idea

Let `dp[j]` be the number of ways to form the first `j` characters of `t` using characters of `s` processed so far. Initially only the empty prefix has one way. For each character of `s`, scan `t` from the end and add `dp[j-1]` into `dp[j]` whenever the characters match.

## Why it works

When the current source character equals `t[j-1]`, every way of forming the first `j-1` target characters can be extended by this character to form the first `j`. Characters may also be skipped, which is already represented by leaving `dp[j]` unchanged. Scanning backwards is essential: `dp[j-1]` must still refer to the state before the current source character, otherwise one character could be used multiple times. Finally, `dp[len(t)]` counts all ways to form the whole target.

## Edge cases

- An empty target has exactly one subsequence, the empty one, so the answer is 1 for any source.
- An empty source cannot form a non-empty target, so the answer is 0.
- If the target is longer than the source, no subsequence can match; the loop naturally leaves the count at 0.
- Repeated characters are counted by position, which the backward update handles correctly.
- The count may be large but the problem guarantees it fits in a 32-bit signed integer.
