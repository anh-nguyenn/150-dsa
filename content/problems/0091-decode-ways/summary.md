A message is written as a string of digits. Each letter maps to a number (`A` = 1 through `Z` = 26), so the string can be split into one- or two-digit pieces. Return how many different valid splits exist.

A piece may not start with zero, and a two-digit piece must be between 10 and 26.

**Example**

```text
"12"  -> 2   (1|2 or 12)
"226" -> 3   (2|2|6, 22|6, 2|26)
```

**Constraints, in plain words**

- Between 1 and 100 digits.
- Only digit characters appear.
- The string may contain zeros.

[Decode Ways on LeetCode](https://leetcode.com/problems/decode-ways/)
