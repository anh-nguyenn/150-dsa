Given an `n x n` grid of integers, turn the picture a quarter turn clockwise. The change happens inside the given grid, so no second grid is returned.

**Example**

```text
[[1, 2, 3],        [[7, 4, 1],
 [4, 5, 6],   ->   [8, 5, 2],
 [7, 8, 9]]        [9, 6, 3]]
```

The top row becomes the right column, and the left column becomes the top row read backwards.

**Constraints, in plain words**

- The grid is square, with a side length between 1 and 20.
- Entries are ordinary integers.
- Rotate in place; building a replacement grid is not the intended approach.

[Rotate Image on LeetCode](https://leetcode.com/problems/rotate-image/)
