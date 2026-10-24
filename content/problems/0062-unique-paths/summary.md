Start in the top-left cell of an `m` by `n` grid and finish in the bottom-right cell. Each move goes exactly one cell right or one cell down, so a route is an ordering of `m - 1` down moves and `n - 1` right moves. Return how many distinct routes exist.

For a `3 x 7` grid the answer is `28`. A `3 x 2` grid has `3` routes: right then two downs, down then right then down, or two downs then right.

**Constraints, in plain words**

- Between 1 and 100 rows and columns.
- Moves are only right and down; no left or up moves.
- The count grows quickly, but Python integers handle it without overflow.

[Unique Paths on LeetCode](https://leetcode.com/problems/unique-paths/)
