Given a rectangular board of letters and a list of words, return every word that can be traced through neighbouring cells. Moves go up, down, left, or right, and a single board cell may not be used twice within one word. The result may be returned in any order.

**Example**

```text
board = [[o, a, a, n],
         [e, t, a, e],
         [i, h, k, r],
         [i, f, l, v]]
words = [oath, pea, eat, rain]
-> [oath, eat]
```

**Constraints, in plain words**

- The board has between 1 and 12 rows and columns.
- Every board cell is a lowercase English letter.
- There are between 1 and 30,000 words, each of length 1 to 10.
- A word must use adjacent cells without reusing any cell.
- Duplicate words in the input should appear only once in the answer.

[Word Search II on LeetCode](https://leetcode.com/problems/word-search-ii/)
