Rebuild a binary tree from two lists: its pre-order traversal and its in-order traversal. All values are distinct, so the lists determine exactly one tree.

The first pre-order value is the root. Its position in the in-order list separates the left subtree's values from the right subtree's values.

**Examples**

```text
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]
->  [3, 9, 20, null, null, 15, 7]
```

```text
preorder = [1, 2], inorder = [2, 1]  ->  [1, 2]
```

**Constraints, in plain words**

- Between 1 and 3,000 nodes.
- Every value in the tree is unique.
- Both lists describe the same tree, and each has exactly the same length.

[Construct Binary Tree from Preorder and Inorder Traversal on LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
