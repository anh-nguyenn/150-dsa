## Idea

Use the first row and first column as flags for the rest of the grid, and save those two edges' own status in two booleans before changing anything.

## Why it works

A zero found in the inner grid writes a marker into its row's first cell and its column's first cell. In the second pass, an inner cell is cleared exactly when one of its markers is zero. Because the inner cells are handled before the first row and first column are overwritten, the markers remain readable until they are no longer needed. The two booleans handle the only rows and columns that cannot store a marker for themselves.

## Edge cases

- A `1 x 1` zero: both flags are true, so the single cell is cleared.
- A `1 x 1` nonzero value: both flags are false and nothing changes.
- A single row: there are no inner rows, so only the first-row flag is applied.
- A single column: only the first-column flag is applied.
- A zero in the first row and a zero in the first column are treated independently by the flags.
