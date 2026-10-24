You are given a reference to one node of an undirected connected graph. Each node holds a value and a list of neighbor nodes. Return a deep copy: new nodes with the same values and the same neighbor relationships, sharing no node objects with the original.

**Example**

```text
adjacency: [[2,4],[1,3],[2,4],[1,3]]
```

describes four nodes arranged in a cycle. The returned graph should produce the same adjacency list.

**Constraints, in plain words**

- A non-empty graph has up to 100 nodes, numbered 1 through n.
- The graph is connected, and a single node may have no neighbors.
- There are no repeated edges and no self-loops.
- An empty graph is passed as `None` and must be returned as `None`.

[Clone Graph on LeetCode](https://leetcode.com/problems/clone-graph/)
