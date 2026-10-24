An Eulerian path walks through every edge of a graph exactly once. For a directed graph such a path exists only when the in-degree and out-degree of every node match, except possibly one node with one extra outgoing edge (the start) and one with one extra incoming edge (the end). Hierholzer's algorithm builds the path by following unused edges until it gets stuck, then splicing in detours from earlier nodes.

### Everyday examples

- **A walking tour.** You want to cross every bridge in a city once without repeating a bridge. When you reach a dead end, you back up to the last place where you skipped an unused bridge.
- **A delivery route.** Every parcel must be dropped once. If a chosen street leads nowhere useful, you return to a junction that still has an undelivered stop.

### How it shows up here

Tickets are directed edges and airports are nodes. We need an Eulerian path that begins at `"JFK"`. To make the result lexicographically smallest, always consume the smallest available outgoing ticket first. When a node has no unused tickets left, it is appended to the route; reversing the collected route at the end yields the itinerary.
