## Hint 1

For `n` nodes, how many edges must a tree have? Check that first, before looking at connectivity.

## Hint 2

When you add an edge, how can you tell whether its endpoints are already connected through the edges you have added so far?

## Hint 3

Use disjoint sets while adding edges. An edge whose endpoints already share a root creates a cycle. With the right edge count and no such edge, the graph must be connected.
