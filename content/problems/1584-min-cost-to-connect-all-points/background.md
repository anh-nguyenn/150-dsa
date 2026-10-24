A minimum spanning tree connects every vertex of a weighted graph with the smallest possible total edge weight and no cycles. Two classical ways to build one are Kruskal's algorithm, which adds cheap edges while avoiding cycles, and Prim's algorithm, which grows a single tree by repeatedly attaching the nearest outside vertex.

### Everyday examples

- **Village roads.** Several villages need to be linked by roads. Building the shortest total road network means choosing connections that join everyone without a redundant loop.
- **Circuit wiring.** Pins on a board must share a ground network. The cheapest layout reaches every pin while avoiding extra wire.

### How it shows up here

Every pair of points can be joined, and the edge weight is the Manhattan distance between them. That is a complete weighted graph. With up to 1,000 points there are far too many edges to store comfortably, so Prim's algorithm is a natural fit: keep the best known connection cost from the growing tree to each outside point and repeatedly add the cheapest one. The sum of the added costs is the answer.
