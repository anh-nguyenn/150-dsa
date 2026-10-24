You are given a grid where `0` is empty, `1` is a fresh orange, and `2` is a rotten orange. Each minute, every rotten orange turns its four orthogonal fresh neighbors rotten. Return the number of minutes until no fresh orange remains, or `-1` if some fresh orange can never be reached.

**Example**

```text
[[2,1,1],
 [1,1,0],
 [0,1,1]]
```

takes 4 minutes. A fresh orange sealed off from every rotten one would stay fresh forever.

**Constraints, in plain words**

- The grid is rectangular with at least one cell.
- Each cell is empty, fresh, or rotten.
- Rotting spreads one step per minute, only up, down, left, and right.

[Rotting Oranges on LeetCode](https://leetcode.com/problems/rotting-oranges/)
