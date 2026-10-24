## Idea

Create a copy of the starting node and store the pairing in a dictionary. Walk the original graph; the first time a neighbor appears, create its copy and push it, then always append the mapped copy to the current copy's neighbor list.

## Why it works

The dictionary guarantees one copy per original node. Because a node is enqueued only when its copy is first created, every node is processed once, and using the mapped copy for every edge preserves the neighbor structure while avoiding links back into the original graph.

## Edge cases

- `None` represents an empty graph and returns `None`.
- A single node with an empty neighbor list copies to a new node with no neighbors.
- Cycles are handled because the start node is already in the map when the walk returns to it.
- A node reached by several paths still gets exactly one copy.
- The result must not share any node objects with the input.
