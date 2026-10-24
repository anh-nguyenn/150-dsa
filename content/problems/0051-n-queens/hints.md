## Hint 1

If you place exactly one queen in each row, which kinds of conflicts are already impossible?

## Hint 2

How can you identify a diagonal with a single number? Compute `row + col` and `row - col` for a few squares and look for a pattern.

## Hint 3

Place queens row by row, tracking used columns and both diagonal sums. Try every column in the current row, recurse, then undo the placement and its three marks.
