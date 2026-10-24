An `n x n` grid gives the height of the ground at each cell. At time `t`, water has risen to level `t`, and you may stand on any cell whose height is at most `t`. Starting at the top-left cell and moving up, down, left, or right, return the earliest time at which you can reach the bottom-right cell.

**Example**

```text
grid = [[0,2],
        [1,3]]  ->  3
```

The route through heights 0, 1, 3 needs water level 3.

**Constraints, in plain words**

- The grid is square, at most 50 by 50.
- Every height is distinct and lies between 0 and n^2 - 1.
- Movement is only to edge-sharing neighbors.
- You may wait for the water to rise.

[Swim In Rising Water on LeetCode](https://leetcode.com/problems/swim-in-rising-water/)
