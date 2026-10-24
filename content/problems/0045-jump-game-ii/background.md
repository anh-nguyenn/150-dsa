This is a shortest-path problem on a line, but the edges are implicit: from an index you may jump anywhere up to its value. Shortest paths can be found layer by layer. Each layer contains every position reachable with the same number of jumps, and those positions form one contiguous range.

### Everyday examples

- **Bus transfers.** Each route from a stop can take you up to a certain distance. The minimum number of buses is the number of reachable ranges you must cross, not the exact route.
- **Board game pieces.** A piece may move forward up to the number on its square. To finish with the fewest dice rolls, you care about how far the current roll's range extends, not every individual landing square.

### How it shows up here

Think of the positions reachable with `k` jumps as a range ending at `end`. While scanning inside that range, compute the farthest position any of those positions can reach. Once the scan reaches `end`, the next jump layer is complete: increment the jump count and move `end` to that farthest position. Stop before the final index so the last extension is not counted extra.

Because the reachable positions form a single interval, one pass is enough and no queue is needed.
