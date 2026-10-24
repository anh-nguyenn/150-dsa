## Idea

Breadth-first search with a queue. At the start of each round, freeze the queue's size, which is the number of nodes on the current level. Pop exactly that many nodes, collect their values, and enqueue their children for the next round.

## Why it works

A queue processes nodes in the order they were discovered. Since children are appended after all currently queued nodes, every node on one level is removed before any node on the next level. Freezing the size at the start of a round yields exactly one level's worth of nodes. Each node is enqueued and dequeued once, so the work is linear in the number of nodes.

## Edge cases

- An empty tree returns an empty list, not a list containing an empty level.
- A single node returns one level with one value.
- A one-sided chain produces one single-value level per node.
- Missing children are simply skipped; they do not create empty levels.
- Level order is exact: left-to-right order within each level must be preserved.
- Negative values are ordinary values and need no special handling.
