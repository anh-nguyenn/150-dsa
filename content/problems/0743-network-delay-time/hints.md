## Hint 1

What single number summarizes when a broadcast is finished, once you know the earliest arrival time at each node?

## Hint 2

Edge weights differ, so a plain breadth-first search is not enough. Can you always extend the currently cheapest known route?

## Hint 3

Use a min-heap keyed by arrival time. Settle a node the first time it leaves the heap, relax its outgoing edges, and take the maximum settled time.
