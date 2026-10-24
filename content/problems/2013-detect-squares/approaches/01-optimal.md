## Idea

Store how many times each point was added. For a query, treat each stored point as the diagonal opposite and look up the two side corners.

## Why it works

If `(x, y)` is diagonally opposite `(px, py)` and the coordinate differences have equal size, then the side corners must be `(x, py)` and `(px, y)`. Conversely, any square using the query point has exactly one such diagonal opposite, so each square is counted once. The three multiplicities are independent choices of copies, which handles duplicate points correctly.

## Edge cases

- Counting before any point is added returns 0.
- A stored point equal to the query is skipped because a square needs nonzero side length.
- Several stored points at different diagonal distances each contribute their own squares.
- Duplicate copies multiply the number of choices, which the frequency factor captures.
- A stored point sharing only a row or only a column with the query is not a diagonal opposite.
