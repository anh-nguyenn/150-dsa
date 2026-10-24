A path is any sequence of connected nodes in the tree that uses each node at most once. It does not have to pass through the root, and it does not have to end at a leaf. Return the largest possible sum of node values along such a path.

**Examples**

```text
tree = [1, 2, 3]                  ->  6
tree = [-10, 9, 20, null, null, 15, 7]  ->  42
```

The first answer uses the path `2 -> 1 -> 3`. In the second, the best path is `15 -> 20 -> 7`.

**Constraints, in plain words**

- The tree has between 1 and 30,000 nodes.
- Node values are between -1,000 and 1,000.
- Values may be negative, and a path must contain at least one node.

[Binary Tree Maximum Path Sum on LeetCode](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
