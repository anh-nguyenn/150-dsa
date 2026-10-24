## Idea

Run Dijkstra from the source. The distance array records the earliest known arrival time at each node, and a min-heap always hands back the unfinalized node with the smallest arrival time. When a node leaves the heap with an out-of-date distance, skip it; otherwise relax its outgoing links. The broadcast time is the largest finalized distance across all nodes.

## Why it works

All edge weights are positive, so once the smallest tentative distance is popped it cannot be improved by a later route. Relaxing every outgoing edge from a settled node therefore preserves the invariant that each stored distance is the best known arrival time. After the search, every reachable node has its true shortest time, and the maximum of those times is exactly when the last node is informed.

## Edge cases

- A single node with no edges finishes at time `0`.
- If the source cannot reach some node, that node keeps an infinite distance and the answer is `-1`.
- Parallel edges between the same pair are harmless; the cheaper one wins during relaxation.
- Cycles cannot lower a settled distance because all weights are positive.
