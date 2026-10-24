You are given a board of `"X"` and `"O"` cells. Capture every region of `"O"` that is completely surrounded by `"X"` by turning all of its cells into `"X"`. A region survives if any of its cells lies on the border, or connects to a border cell through up, down, left, or right neighbors. Modify the board in place.

**Example**

```text
[["X","X","X","X"],
 ["X","O","O","X"],
 ["X","X","O","X"],
 ["X","O","X","X"]]
```

keeps the lone `"O"` on the bottom border, while the connected group in the middle is captured.

**Constraints, in plain words**

- The board has at least one row and one column.
- Each cell is either `"X"` or `"O"`.
- Connections are only up, down, left, and right.
- The board must be changed in place.

[Surrounded Regions on LeetCode](https://leetcode.com/problems/surrounded-regions/)
