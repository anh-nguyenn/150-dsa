## Hint 1

How would you count one island completely before moving on, and what would you change so it is not counted again?

## Hint 2

When you stand on land, which neighboring cells belong to the same island? What should happen to a cell after you visit it?

## Hint 3

Scan every cell. On unvisited land, increment a counter and run a flood fill with a stack or queue, marking cells as you reach them.
