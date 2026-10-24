## Idea

Keep one array whose entry `row[col]` is the number of routes to the current cell in that column. Initially the array represents the first row, where every cell has exactly one route. For each later row, the old value at `row[col]` is the count from above, while `row[col - 1]` has already been updated to the count from the left. Adding them gives the new cell count.

## Why it works

Every route to cell `(r, c)` ends with either a down move from `(r - 1, c)` or a right move from `(r, c - 1)`. These two groups of routes are disjoint and together contain all routes to the cell, so the recurrence counts each route exactly once. Filling rows in order guarantees both predecessor counts are final.

## Edge cases

- A single row: every cell has one route, so the answer is `1`.
- A single column: likewise, the answer is `1`.
- A `1 x 1` grid: you are already at the destination, so the answer is `1`.
- Large grids produce large counts; the code relies on Python's arbitrary-precision integers.
