You are given a grid of rooms. `-1` is a wall, `0` is a gate, and `2147483647` (the largest 32-bit integer) is an empty room. Fill every empty room with its distance to the nearest gate, counting one step per room moved up, down, left, or right. Rooms that cannot reach any gate stay at `2147483647`. Modify the grid in place.

**Example**

```text
[[2147483647, 0, 2147483647]]
```

becomes

```text
[[1, 0, 1]]
```

**Constraints, in plain words**

- The grid has at least one row and one column.
- Movement is only horizontal or vertical.
- Walls cannot be crossed.
- A gate has distance 0.

[Walls and Gates on LeetCode](https://leetcode.com/problems/walls-and-gates/)
