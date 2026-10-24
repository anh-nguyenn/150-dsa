## Idea

Grow one connected tree from the first point. `best[v]` stores the cheapest Manhattan distance from `v` to any point already in the tree. Each round chooses the outside point with the smallest `best` value, adds it and its connection cost, then refreshes the stored distances for the remaining points. This is Prim's algorithm without explicitly building all pairs of edges.

## Why it works

The cut property of minimum spanning trees says the cheapest edge crossing from the current tree to any outside vertex is safe to include. Prim's choice is exactly that edge. Updating only the newly reachable distances keeps the invariant that `best[v]` is the cheapest link from `v` to the tree, so every added cost is part of some optimal spanning tree and their sum is minimal.

## Edge cases

- A single point needs no connections, so the cost is `0`.
- Two points simply pay their Manhattan distance.
- Collinear points still connect through the cheapest adjacent links.
- Equal distances are fine; any tie produces the same total cost.
