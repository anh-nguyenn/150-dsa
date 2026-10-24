Given the root of a binary tree, imagine standing on the right side of it and looking toward the left. Return the values of the nodes you can see, ordered from top to bottom.

Only the rightmost node on each level is visible. A node on the left can still be visible when the right side of that level is empty.

**Examples**

```text
tree = [1, 2, 3, null, 5, null, 4]  ->  [1, 3, 4]
tree = [1, null, 3]                 ->  [1, 3]
```

**Constraints, in plain words**

- The tree has between 1 and 100 nodes.
- Node values fit in a signed 32-bit integer.
- The input uses level-order order, with `null` marking a missing child.

[Binary Tree Right Side View on LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/)
