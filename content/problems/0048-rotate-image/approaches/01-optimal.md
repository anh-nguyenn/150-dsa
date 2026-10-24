## Idea

Swap each cell with its mirror across the main diagonal, then reverse the order of every row.

## Why it works

The transpose sends the cell at row `i`, column `j` to row `j`, column `i`. Reversing a row then changes its column `c` to `n - 1 - c`. Together they send `(i, j)` to `(j, n - 1 - i)`, exactly the clockwise quarter-turn destination. Every swap is done in place, so no cell is overwritten before it moves.

## Edge cases

- A `1 x 1` grid is already rotated; both loops do nothing.
- A `2 x 2` grid still needs the diagonal swap and the row reversal.
- Equal entries or all zeros do not change the logic, only the visible values.
- The diagonal loop starts at `j = i + 1`, so diagonal cells are not swapped with themselves.
