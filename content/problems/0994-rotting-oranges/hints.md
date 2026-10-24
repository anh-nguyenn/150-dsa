## Hint 1

Which oranges can rot during the same minute, and what determines the end of a minute?

## Hint 2

If all rotten oranges spread together, how can you process one full wave of the queue before counting the next minute?

## Hint 3

Start BFS with every rotten orange, track how many fresh oranges remain, and count completed waves. If any fresh orange is left at the end, return -1.
