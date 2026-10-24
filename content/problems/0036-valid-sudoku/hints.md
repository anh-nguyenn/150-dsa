## Hint 1

Every filled cell must pass three independent no-duplicate checks. What are those three groups?

## Hint 2

For a cell at row `r` and column `c`, how can integer division tell you which of the nine 3 by 3 boxes it belongs to?

## Hint 3

Keep one set per row, one per column, and one per box. Process each cell once, and return false as soon as the digit is already in any of its three sets.
