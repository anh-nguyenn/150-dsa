## Idea

Grow the string one character at a time. Track how many opening and closing parentheses have been used. Add an opening parenthesis while fewer than `n` are open, and add a closing parenthesis only while fewer closes than opens have been used.

## Why it works

The two rules guarantee that every prefix is a prefix of some balanced string: there can never be too many closes, and there can never be more than `n` opens. Since the string stops at exactly `2n` characters, it must contain `n` opens and `n` closes, so it is balanced. Every balanced string follows these choices at every step, so the search generates each one once.

## Edge cases

- `n = 1` returns only `"()"`.
- `n = 0` returns `[""]`, the empty balanced string.
- Larger `n` grows quickly: the count is the nth Catalan number.
- The search never produces prefixes with more closes than opens, so no post-filtering is needed.
