## Idea

Treat each cell as a node and connect it to its orthogonal neighbors with larger values. Run a depth-first search from every cell, and store the longest path starting at each cell in a memo table. A cached cell returns immediately, so each cell is expanded only once.

## Why it works

Along every edge the value strictly increases, so the directed graph is acyclic. An acyclic graph has a well-defined longest path from each node, and the recurrence `1 + max(length of larger neighbors)` computes it. Memoization is safe because a cell's answer never depends on how the search arrived there; it depends only on the cell itself.

## Edge cases

- A single cell has no larger neighbor, so the answer is 1.
- A completely flat grid has no valid move, so the answer is 1.
- Negative values are fine; only the comparison between neighbors matters.
- A one-row or one-column grid restricts movement but is handled by the bounds check.
- The helper returns 1 when no larger neighbor exists, which also handles local peaks.
