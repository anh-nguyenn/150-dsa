## Idea

Simulate long multiplication in a digit array whose indices represent decimal places, resolving carries as each pair of digits is multiplied.

## Why it works

The digit at index `i` in the first string has place value `10^(m-1-i)`, and similarly for the second. Their product therefore belongs at place `10^(m+n-2-i-j)`, which the array stores at indices `i + j` and `i + j + 1`. Adding the product to the lower slot and carrying into the higher slot keeps every slot a decimal digit after it has been used. Every pair is processed, so the array holds the full product; trimming leading zeros yields the canonical string.

## Edge cases

- A zero in either input returns `"0"` immediately.
- Multiplying by `"1"` returns the other operand unchanged.
- Products that need a new leading digit, such as `"9" * "9"`, use the extra first slot.
- Trailing zeros in the operands produce trailing zeros in the product.
- Leading zeros in the result array are skipped before joining the digits.
