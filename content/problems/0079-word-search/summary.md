Given a rectangular grid of letters and a target word, decide whether the word can be traced through adjacent cells. Consecutive letters must share an edge, and a cell may be used at most once in one path. Return `true` or `false`.

**Example**

```text
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCED" -> true
word = "ABCB"   -> false
```

**Constraints, in plain words**

- The grid has at least one cell and at most 6 rows by 6 columns.
- Every cell contains one letter.
- The word length is between 1 and 15 in the official input.
- Moves are up, down, left, or right; diagonal moves are not allowed.
- A path cannot revisit a cell.

[Word Search on LeetCode](https://leetcode.com/problems/word-search/)
