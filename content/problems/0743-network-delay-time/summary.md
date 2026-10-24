A directed network has `n` nodes numbered `1` through `n`. Each `[u, v, w]` in `times` means a signal takes `w` time to travel from `u` to `v`. A signal starts at node `k`. Return how long it takes for every node to receive it, or `-1` if some node stays unreachable.

**Example**

```text
times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2  ->  2
```

From node 2, nodes 1 and 3 are one second away and node 4 is two seconds away, so the last node hears the signal after 2 seconds.

**Constraints, in plain words**

- At most 100 nodes and about 6,000 directed edges.
- Edge weights are positive.
- The source is always a valid node.
- A node can be reached only by following edges in their given direction.

[Network Delay Time on LeetCode](https://leetcode.com/problems/network-delay-time/)
