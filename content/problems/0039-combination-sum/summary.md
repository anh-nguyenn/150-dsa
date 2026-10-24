You are given distinct positive integers and a target. Return every combination of numbers that adds up to the target. You may use each number as many times as you like, and combinations may be returned in any order.

**Example**

```text
candidates = [2, 3, 6, 7], target = 7
-> [[2, 2, 3], [7]]
```

`[2, 2, 3]` works because `2` is reused, and `[3, 2, 2]` is the same combination, not a new one.

**Constraints, in plain words**

- Up to 30 distinct candidates.
- Candidates and the target are positive.
- The target is at most 40, so the search depth stays small.
- Reuse is allowed; reordering a combination is not a new answer.

[Combination Sum on LeetCode](https://leetcode.com/problems/combination-sum/)
