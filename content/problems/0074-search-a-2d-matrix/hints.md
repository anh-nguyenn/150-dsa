## Hint 1

Because of the ordering between rows, what happens if you read the matrix row by row into one list?

## Hint 2

Given a flat index in that imagined list, how do you find its row and column?

## Hint 3

Binary search over indices from 0 to `rows * cols - 1`, converting each midpoint with division and remainder by the number of columns.
