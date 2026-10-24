## Idea

View the matrix as one sorted array of length `rows * cols` without actually building it. Binary search flat indices, translating a midpoint into a row with integer division and a column with the remainder.

## Why it works

The row ordering rule makes the flattened sequence sorted: every cell in an earlier row is smaller than every cell in a later row, and each row is already sorted. Binary search is correct on any sorted sequence, so it is correct here. The index translation is exact because each row holds exactly `cols` entries, and every flat index in range maps to a unique cell.

## Edge cases

- A 1-by-1 matrix either matches the target or returns false.
- A single row or single column still works with the flattened indices.
- The target may be smaller than the top-left value or larger than the bottom-right value.
- Negative values compare normally.
- The code assumes the matrix is non-empty, as guaranteed by the constraints.
