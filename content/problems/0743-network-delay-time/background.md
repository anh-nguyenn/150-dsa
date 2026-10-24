Finding the shortest path in a weighted graph is a core graph task. When every edge has a positive cost, Dijkstra's algorithm grows a cloud of settled nodes outward from the source, always expanding the cheapest unfinished route next. A priority queue keeps the frontier ordered.

### Everyday examples

- **Subway travel.** Stations are nodes and ride times are edge weights. The fastest arrival time to each station comes from repeatedly extending the currently quickest reachable trip.
- **Package delivery.** A depot sends parcels along roads with different travel times. The moment the slowest parcel arrives is the maximum of the per-destination shortest times.
- **Network broadcast.** A message fans out across links. The broadcast finishes when the last reachable machine has been updated.

### How it shows up here

The nodes are machines, the directed edges are links with transmission delays, and the source is the machine that starts the broadcast. Dijkstra gives the earliest arrival time at every node. The answer is the largest of those times, because the broadcast is complete only when the slowest node hears it. If any node is never settled, it cannot be reached and the answer is `-1`.
