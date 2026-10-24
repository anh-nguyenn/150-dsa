Compute `x` raised to the integer power `n`, where `n` may be zero or negative, and return a floating-point result.

**Example**

```text
x = 2.0, n = 10  -> 1024.0
x = 2.0, n = -2  -> 0.25
```

**Constraints, in plain words**

- `x` is between -100 and 100 and may have a fractional part.
- `n` is a 32-bit signed integer, so its smallest value is -2,147,483,648.
- The result fits in a double-precision number.
- Multiplying `x` by itself `n` times is too slow when `n` is large.

[Pow(x, n) on LeetCode](https://leetcode.com/problems/powx-n/)
