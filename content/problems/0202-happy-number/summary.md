A number is happy when repeatedly replacing it with the sum of the squares of its digits eventually reaches 1. Return whether the given positive integer is happy.

**Example**

```text
19 -> 1^2 + 9^2 = 82 -> 8^2 + 2^2 = 68 -> ... -> 100 -> 1   (happy)
2  -> 4 -> 16 -> 37 -> ... -> 4                              (unhappy)
```

**Constraints, in plain words**

- The input is a positive integer up to about 2.1 billion.
- The process either reaches 1 or falls into a repeating cycle.
- A constant amount of extra memory is enough.

[Happy Number on LeetCode](https://leetcode.com/problems/happy-number/)
