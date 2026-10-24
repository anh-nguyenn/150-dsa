Treat the input as a fixed 32-bit binary word and reverse the order of its bits. Return the resulting non-negative integer.

**Example**

```text
n = 43261596  ->  964176192
```

The input's 32-bit form ends in `...0011100`, and those bits become the leading bits of the answer.

**Constraints, in plain words**

- The input is a non-negative integer below 2^32.
- Exactly 32 bit positions are reversed, including leading zeros.
- Return an integer, not a binary string.

[Reverse Bits on LeetCode](https://leetcode.com/problems/reverse-bits/)
