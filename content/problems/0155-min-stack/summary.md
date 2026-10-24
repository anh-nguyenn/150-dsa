Build a stack that supports `push`, `pop`, `top`, and `getMin`, all in constant time. `getMin` returns the smallest value currently in the stack.

```text
push(-2), push(0), push(-3)
getMin()  ->  -3
pop()
getMin()  ->  -2
```

**Constraints, in plain words**

- Values fit in a signed 32-bit integer.
- Between 1 and 30,000 method calls occur.
- `pop`, `top`, and `getMin` are only called when the stack is non-empty.
- Every operation should run in O(1) time.

[Min Stack on LeetCode](https://leetcode.com/problems/min-stack/)
