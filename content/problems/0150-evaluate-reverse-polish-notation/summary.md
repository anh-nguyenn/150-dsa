Evaluate an arithmetic expression written in reverse Polish notation, where the operator comes after its two operands. Division truncates toward zero.

```text
["2","1","+","3","*"]  ->  9
["4","13","5","/","+"]   ->  6
```

**Constraints, in plain words**

- Between 1 and 10,000 tokens.
- The expression is always valid.
- Tokens are integers or one of `+ - * /`.
- Division between integers truncates toward zero.
- The final answer fits in a signed 32-bit integer.

[Evaluate Reverse Polish Notation on LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
