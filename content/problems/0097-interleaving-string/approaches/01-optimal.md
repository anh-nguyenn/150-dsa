## Idea

Keep a boolean row where `dp[j]` says whether the current prefix of `s1`, together with the first `j` characters of `s2`, can build the corresponding prefix of `s3`. The value before an update at column `j` comes from the previous row (using the next character of `s1`), and `dp[j - 1]` comes from the current row (using the next character of `s2`). Either path works if its source character matches the next character of `s3`.

## Why it works

Any interleaving prefix ends by consuming the next character of either `s1` or `s2`. If that character matches the corresponding character of `s3`, and the prefix without it was already reachable, then the new prefix is reachable. Conversely, every reachable cell has such a last step, so the recurrence is exact. The length check rules out inputs that cannot possibly consume everything.

## Edge cases

- All three strings empty: the answer is `true`.
- One source empty: the other must equal `s3` exactly.
- Length mismatch: immediately `false`.
- A character may match the fronts of both sources; either choice must be explored, which the boolean OR handles.
- Repeated characters can create several valid paths to the same state, but the boolean state merges them safely.
