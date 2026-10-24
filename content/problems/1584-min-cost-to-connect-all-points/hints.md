## Hint 1

Which points are already connected, and which single new connection would bring an outside point into the network most cheaply?

## Hint 2

You do not need to materialize every possible edge. For each point outside the tree, keep the cheapest distance to any point already inside.

## Hint 3

Start from one point and repeat `n` times: pick the unvisited point with the smallest stored distance, add that distance, then update the stored distances to its neighbors.
