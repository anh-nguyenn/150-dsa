You are given a grid of heights. The Pacific Ocean touches the top and left edges, while the Atlantic Ocean touches the bottom and right edges. Rain on a cell can flow to an adjacent cell whose height is less than or equal to its own, and eventually into an ocean. Return the `[row, column]` coordinates of every cell whose water can reach both oceans. The order of the coordinates is free.

**Example**

```text
[[1,2],
 [4,3]]
```

returns `[[0,1],[1,0],[1,1]]`: the top-left cell is too low to escape toward the Atlantic.

**Constraints, in plain words**

- The grid has at least one row and one column.
- Water moves only up, down, left, and right.
- Water may move to an equal or lower height.
- Coordinates may be returned in any order.

[Pacific Atlantic Water Flow on LeetCode](https://leetcode.com/problems/pacific-atlantic-water-flow/)
