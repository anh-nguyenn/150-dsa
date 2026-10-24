Given a binary search tree and two values `p` and `q` that both appear in it, return the value of their lowest common ancestor: the deepest node that has both values somewhere in its subtree.

In this exercise the function takes the two values directly, not node objects, and it returns the ancestor's value. For the BST `[6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]`, `p = 2` and `q = 8` give `6`, while `p = 3` and `q = 5` give `4`.

**Constraints, in plain words**

- The tree has between 2 and 100,000 nodes and is a valid binary search tree.
- All node values are unique and between -10^9 and 10^9.
- `p` and `q` are different values and both exist in the tree.

[Lowest Common Ancestor of a Binary Search Tree on LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
