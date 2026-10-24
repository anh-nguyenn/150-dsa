You are given a rectangular grid of integers. Starting from any cell, you may move one step up, down, left, or right, but only onto a cell whose value is strictly larger. Return how many cells the longest such path contains. Diagonal moves are not allowed, and a path never revisits a cell.

**Example**

```text
matrix = [[9, 9, 4],
          [6, 6, 8],
          [2, 1, 1]]  ->  4
```

One best path is `1 -> 2 -> 6 -> 8`. The two `9`s do not extend it because moves must increase.

**Constraints, in plain words**

- The grid has between 1 and 200 rows and between 1 and 200 columns.
- Cell values are ordinary 32-bit signed integers, so they may be negative.
- Moves are limited to the four orthogonal directions.

[Longest Increasing Path in a Matrix on LeetCode](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)
