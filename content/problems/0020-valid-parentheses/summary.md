You get a string made only of round, square, and curly brackets. Decide whether every opening bracket is eventually closed by the same kind, with no crossing pairs.

```text
"()[]{}"  ->  true
"([)]"    ->  false
```

**Constraints, in plain words**

- The string has between 1 and 10,000 characters.
- Only `()[]{}` appear.
- A closing bracket must match the most recent unclosed opener.
- Pairs may nest, but they may not cross.

[Valid Parentheses on LeetCode](https://leetcode.com/problems/valid-parentheses/)
