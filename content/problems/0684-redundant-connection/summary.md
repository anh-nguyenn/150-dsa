An undirected graph was built as a tree on nodes `1` through `n`, then one additional edge was inserted. The edge list has exactly `n` entries. Return the extra edge that can be deleted so the remaining edges form a tree again. If several deletions would work, return the one that appears last in the input.

**Examples**

```text
edges = [[1,2],[1,3],[2,3]]          -> [2,3]
edges = [[1,2],[2,3],[3,4],[4,1]]    -> [4,1]
```

**Constraints, in plain words**

- Between 3 and 1,000 nodes.
- The number of edges equals the number of nodes.
- Every edge joins two distinct labels within `1..n`.
- No edge is repeated, and the graph is connected.

[Redundant Connection on LeetCode](https://leetcode.com/problems/redundant-connection/)
