## Hint 1

Draw the grid and circle one cell. Which neighbors could come next on an increasing path?

## Hint 2

If you already knew the best path length starting at every larger neighbor, how would you compute the answer for the current cell?

## Hint 3

Because values strictly increase, following larger neighbors can never loop. Cache the result for each cell the first time you compute it, then reuse it.
