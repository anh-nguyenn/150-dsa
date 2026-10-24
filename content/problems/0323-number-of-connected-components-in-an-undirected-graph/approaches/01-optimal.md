## Idea

Treat each node as its own component and set the answer to `n`. For every edge, find the roots of its endpoints. If the roots differ, the edge merges two components, so link them and subtract one from the answer. If the roots match, the edge stays inside an existing component and changes nothing. Return the remaining count.

## Why it works

The disjoint-set structure always groups exactly the nodes that are connected by the edges processed so far. A merge happens only for an edge whose endpoints are in different groups, and each merge reduces the number of groups by exactly one. Edges inside a group cannot split or further merge anything, so ignoring them is correct. After all edges are handled, the number of groups is the number of connected components.

## Edge cases

- With no edges, every node is its own component, so the answer is `n`.
- A single node has one component.
- A triangle or larger cycle merges three or more nodes and counts as one component.
- Several edges inside an already merged group do not change the count.
- Isolated nodes remain counted even when other parts of the graph are large.
