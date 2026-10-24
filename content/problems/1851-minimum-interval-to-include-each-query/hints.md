## Hint 1

For a single query, how would you find the shortest covering interval if you scanned all intervals?

## Hint 2

If queries were processed in increasing order, which intervals could safely enter consideration, and which could be retired?

## Hint 3

Sort intervals by start and queries by value. Push newly eligible intervals into a heap ordered by length, discard intervals that end before the query, and read the heap top.
