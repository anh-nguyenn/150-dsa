Given two trees `root` and `sub_root`, return true when `sub_root` occurs as a subtree of `root`: some node of `root` and all of its descendants match `sub_root` exactly. A leaf on its own counts as a subtree.

`[3, 4, 5, 1, 2]` contains `[4, 1, 2]`. If a child `0` is added below the `2`, that candidate no longer matches because the larger tree has an extra node inside the compared subtree.

**Constraints, in plain words**

- `root` has between 1 and 2,000 nodes.
- `sub_root` has between 1 and 1,000 nodes.
- Node values are between -10,000 and 10,000.
- Missing children appear as `null` in the level-order input.

[Subtree of Another Tree on LeetCode](https://leetcode.com/problems/subtree-of-another-tree/)
