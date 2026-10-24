Given a string of digits from 2 to 9, return every letter combination that the digits could represent on a phone keypad. The combinations may be returned in any order.

**Example**

```text
digits = "23"
-> ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```

`2` maps to `abc`, `3` maps to `def`, and each digit contributes exactly one letter.

**Constraints, in plain words**

- The input contains between 0 and 4 digits in the official version.
- Each digit is between 2 and 9; 0 and 1 are not used.
- Every digit must contribute one letter to every result.
- An empty input produces an empty answer, not a list containing the empty string.

[Letter Combinations of a Phone Number on LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
