## Idea

Treat each cell as a node whose required water level is its height. The cost of a route is the maximum height along it, so the search keeps, for each cell, the smallest such maximum found so far. A min-heap processes cells in increasing required level. When the goal is popped, its level is the earliest reachable time.

## Why it works

Extending a route can only raise its maximum, never lower it, so edge costs are monotone and the problem behaves like shortest paths in a graph where the path value is the largest node weight. The heap always expands the smallest known bottleneck, which means no later route can reach the goal at a lower level. Popping the goal therefore yields the true minimum.

## Edge cases

- A one-cell grid has no movement; the answer is that cell's height.
- The goal is at least as high as its own cell, so the answer is never below `grid[n-1][n-1]`.
- Routes may need to detour through low cells to avoid a high wall.
- Different routes are compared by their highest cell, not by their length.
