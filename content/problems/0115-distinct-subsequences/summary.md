Given two strings `s` and `t`, count how many different subsequences of `s` are exactly equal to `t`. A subsequence keeps the original order but may skip characters. Two ways of choosing positions count as different even if the resulting text is identical.

**Example**

```text
s = "rabbbit", t = "rabbit"  ->  3
```

The three choices differ in which of the three `b`s is skipped.

**Constraints, in plain words**

- Both strings contain only lowercase English letters.
- Each string has at most 1,000 characters.
- The final count fits in a 32-bit signed integer.

[Distinct Subsequences on LeetCode](https://leetcode.com/problems/distinct-subsequences/)
