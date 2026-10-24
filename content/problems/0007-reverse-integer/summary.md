Reverse the decimal digits of a signed 32-bit integer. If the reversed value would fall outside the signed 32-bit range, return 0 instead.

**Examples**

```text
x = 123   ->  321
x = -120  ->  -21
x = 1534236469  ->  0
```

The last reversal exceeds the largest signed 32-bit value, so the answer is 0.

**Constraints, in plain words**

- The input is between -2^31 and 2^31 - 1.
- Leading zeros in the reversed digits are dropped.
- Return 0 if the result is outside the signed 32-bit range.

[Reverse Integer on LeetCode](https://leetcode.com/problems/reverse-integer/)
