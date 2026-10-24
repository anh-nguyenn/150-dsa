A node is called good when no other node on the path from the root down to it has a larger value. Equivalently, its value is at least the maximum value seen so far on that root-to-node path. Count the good nodes in the tree.

**Examples**

```text
tree = [3, 1, 4, 3, null, 1, 5]  ->  4
tree = [3, 3, null, 4, 2]        ->  3
```

In the first tree the good nodes are the root `3`, the right child `4`, the left grandchild `3`, and the far-right `5`.

**Constraints, in plain words**

- The tree has between 1 and 100,000 nodes.
- Node values are between -10,000 and 10,000.
- Equal values count as good because the definition allows ties.

[Count Good Nodes in Binary Tree on LeetCode](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)
