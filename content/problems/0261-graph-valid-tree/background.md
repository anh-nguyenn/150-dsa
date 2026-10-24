A tree is the leanest connected network possible. Every node can reach every other node, and between any two nodes there is exactly one route. Adding an edge to a tree creates a cycle; removing an edge disconnects it. For `n` nodes, those properties combine into a useful rule: a connected graph is a tree exactly when it has `n - 1` edges and no cycle.

### Everyday examples

- **Roads.** A set of towns linked by roads is tree-like when you can travel between any pair and there is no loop that lets you return home without retracing your path.
- **Family trees.** Each person has a parent above them, with no circular ancestry.
- **Office wiring.** Every desk should be reachable, but a loop of cable between the same rooms is wasted wiring.

### How it shows up here

The nodes are already named, so the job is to test the edges. A quick edge-count check rules out impossible inputs. Then a disjoint-set structure adds edges one at a time: if both endpoints already belong to the same group, the new edge closes a cycle and the graph cannot be a tree. If the count is right and no edge closes a cycle, the graph is necessarily connected.
