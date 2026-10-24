## Hint 1

How could you tell whether the last binary digit is 1?

## Hint 2

What happens to the binary representation when you subtract 1 from a number?

## Hint 3

Use `n & (n - 1)` to erase the lowest set bit, and repeat until the number becomes zero.
