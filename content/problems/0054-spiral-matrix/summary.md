Read a rectangular grid in spiral order: start at the top-left, move right across the top edge, down the right edge, left across the bottom, up the left, and keep tightening the loop until every cell has been visited. Return the values as one list.

**Example**

```text
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]  ->  [1, 2, 3, 6, 9, 8, 7, 4, 5]
```

**Constraints, in plain words**

- Between 1 and 10 rows, and between 1 and 10 columns.
- Entries are ordinary integers.
- Either dimension can be one, so the grid may be a single row or a single column.

[Spiral Matrix on LeetCode](https://leetcode.com/problems/spiral-matrix/)
