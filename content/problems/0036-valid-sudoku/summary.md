Given a 9 by 9 Sudoku board, decide whether the filled cells follow the rules. Each row, each column, and each of the nine 3 by 3 boxes may contain each digit at most once. Empty cells are written as `.` and are ignored. The board does not need to be complete or solvable.

**Example**

```text
Two 5s in the same row        ->  False
Every placed digit is unique
in its row, column, and box   ->  True
```

**Constraints, in plain words**

- The board is exactly 9 by 9.
- Every cell is a digit from `1` to `9` or a dot.
- Only the digits currently placed matter.

[Valid Sudoku on LeetCode](https://leetcode.com/problems/valid-sudoku/)
