Decide whether a binary tree satisfies the binary search tree property: every value in a node's left subtree is strictly smaller than the node, and every value in its right subtree is strictly larger. The whole tree must satisfy this, not just each parent-child pair.

**Examples**

```text
tree = [2, 1, 3]                    ->  true
tree = [5, 1, 4, null, null, 3, 6]  ->  false
```

The second tree fails because `3` sits in the right subtree of `5` but is smaller than `5`.

**Constraints, in plain words**

- The tree has between 1 and 10,000 nodes.
- Node values span the full signed 32-bit range, including its minimum and maximum.
- Duplicate values make the tree invalid.

[Validate Binary Search Tree on LeetCode](https://leetcode.com/problems/validate-binary-search-tree/)
