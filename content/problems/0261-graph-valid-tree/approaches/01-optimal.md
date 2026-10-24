## Idea

First require exactly `n - 1` edges, which is the only possible count for a tree. Then process the edges with a disjoint-set structure. Each edge should join two different components; if its endpoints already share a root, adding it would close a cycle. Accept the graph only when the edge count is correct and no edge closes a cycle.

## Why it works

A tree on `n` nodes must have exactly `n - 1` edges, so the early check is necessary. With exactly `n - 1` edges, the graph is a tree precisely when it is acyclic. Starting with `n` separate components, every edge that joins two different components reduces the number of components by one. If no edge closes a cycle, `n - 1` successful joins leave a single component, which proves connectivity as well.

## Edge cases

- A single node with no edges is a valid tree.
- Two nodes with one edge is valid.
- Too few edges leaves nodes isolated and is rejected immediately.
- Too many edges is rejected even if the graph is connected, because some cycle must exist.
- A cycle with the correct edge count is caught when an edge joins endpoints in the same component.
- A disconnected forest has the wrong edge count or fails the cycle check.
