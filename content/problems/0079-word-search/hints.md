## Hint 1

The word can start at any cell whose letter matches its first character. How many starting points might you need to try?

## Hint 2

From a matched cell, which neighbors are legal next steps, and how do you stop the path from stepping on a cell twice?

## Hint 3

Use depth-first search with row, column, and word index. Mark the current cell, explore the four neighbors, then restore the cell when backtracking.
