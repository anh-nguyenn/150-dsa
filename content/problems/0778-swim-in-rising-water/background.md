Sometimes the cost of a route is not the sum of its edge weights but the largest weight along it. This is a bottleneck or minimax path: you want the route whose worst step is as small as possible. It can be solved by a Dijkstra-style search in which the distance to a cell is the maximum height seen so far, not a sum.

### Everyday examples

- **Mountain hike.** You want a trail whose highest pass is as low as possible, even if the trail is longer.
- **Truck clearance.** A truck needs a route where the lowest bridge is as high as possible above the road.
- **Water flooding.** As the water level rises, the first moment two cells become connected is governed by the highest ground on the best connecting route.

### How it shows up here

The grid is a graph whose nodes are cells and whose edge weights are cell heights. The water level needed to follow a route is the maximum height on that route. The earliest arrival time at the goal is therefore the minimax distance from the start. A priority queue ordered by that running maximum explores the cheapest bottleneck first.
