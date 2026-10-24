## Idea

Try each of the `2n - 1` centres. For a character centre start with `(i, i)`; for a gap centre start with `(i, i + 1)`. Expand outward while the characters match, recording the longest span. Return the substring at the best start with the best length.

## Why it works

Any palindrome is determined by its centre and radius, and expanding stops exactly when the next pair differs or the string ends. Every centre is tried, so the longest palindrome is found. The comparison only moves outward, so each centre costs at most `O(n)` and the whole scan is `O(n^2)`.

## Edge cases

- A one-character string: the odd expansion records length 1 and the loop ends.
- All identical characters: the odd centre in the middle expands to the whole string.
- Even-length answers such as `"bb"`: the gap centre handles them.
- Ties are harmless here: the code keeps the first span of maximal length it encounters, and any longest answer is valid.
