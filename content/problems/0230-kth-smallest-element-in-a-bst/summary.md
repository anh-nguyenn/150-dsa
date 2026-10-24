Given the root of a binary search tree and a 1-indexed integer `k`, return the `k`-th smallest value in the tree.

In-order traversal of a BST visits values from smallest to largest, so the answer is the `k`-th value produced by that traversal.

**Examples**

```text
tree = [3, 1, 4, null, 2], k = 1  ->  1
tree = [3, 1, 4, null, 2], k = 3  ->  3
```

**Constraints, in plain words**

- The tree has between 1 and 10,000 nodes.
- `k` is between 1 and the number of nodes.
- Node values are non-negative and fit in a signed 32-bit integer.

[Kth Smallest Element in a BST on LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
