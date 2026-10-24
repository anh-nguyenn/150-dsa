## Idea

Place one queen per row. For each row, try each column that is not already used and whose two diagonals are not occupied. Record the column, mark the column and both diagonals, recurse to the next row, then unmark everything.

## Why it works

One queen per row removes row conflicts by construction. The column set stops vertical attacks, and the two diagonal sets stop both diagonal directions. A partial board is extended only with legal squares, so every completed board is a valid solution. Undoing the marks after each branch lets sibling branches reuse columns and diagonals that are free for them.

## Edge cases

- `n = 1` has one solution, a board containing a single queen.
- `n = 2` and `n = 3` have no solutions and return an empty list.
- Larger `n` produces many boards; duplicates are avoided because each row is decided in order.
- The four diagonal sums can repeat only on different diagonals, so sets are enough to detect conflicts.
