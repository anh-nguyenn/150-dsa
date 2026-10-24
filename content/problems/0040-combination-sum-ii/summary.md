You are given a list that may contain duplicate numbers and a target. Return every unique combination that adds up to the target. Each position in the input may be used at most once, and combinations may be returned in any order.

**Example**

```text
candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
-> [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
```

The two `1`s are separate positions, so `[1, 1, 6]` is allowed, but it is reported only once.

**Constraints, in plain words**

- Up to 100 candidates.
- Each candidate is between 1 and 50.
- The target is between 1 and 30.
- A value can appear more than once in the input, but an input position can be used only once.
- Two combinations with the same values are considered duplicates even if they came from different positions.

[Combination Sum II on LeetCode](https://leetcode.com/problems/combination-sum-ii/)
