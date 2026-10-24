Given a list that may contain repeated numbers, return every distinct subset, including the empty subset. A subset is identified by its values, so choosing different copies of the same value does not create a new subset.

**Example**

```text
nums = [1, 2, 2]
-> [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
```

`[1, 2]` appears once even though the input has two `2`s.

**Constraints, in plain words**

- The official input has between 1 and 10 numbers.
- Values can repeat.
- Each value is between -10 and 10.
- The answer contains no duplicate subsets, in any order.

[Subsets II on LeetCode](https://leetcode.com/problems/subsets-ii/)
