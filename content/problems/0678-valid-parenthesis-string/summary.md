You are given a string containing `'('`, `')'`, and `'*'`, where each star may stand for an opening parenthesis, a closing parenthesis, or nothing at all. Decide whether some choice of star meanings makes the whole string a valid parenthesis sequence.

**Examples**

```text
s = "(*)"   ->  true
s = "(*))"  ->  true
s = "(((*"  ->  false
```

In `"(*)"`, the star can act as a closing parenthesis.

**Constraints, in plain words**

- The string has between 1 and 100 characters.
- Only `'('`, `')'`, and `'*'` appear.
- Every star is chosen independently.
- A valid sequence never has more closing than opening parentheses at any prefix, and ends with none left open.

[Valid Parenthesis String on LeetCode](https://leetcode.com/problems/valid-parenthesis-string/)
