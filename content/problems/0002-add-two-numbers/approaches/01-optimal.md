## Idea

Use a dummy result list and a tail pointer. At each position, add the current digits that exist plus the carry. Append the units digit to the result and keep the tens digit as the next carry. The loop continues while either input remains or a carry is left over.

## Why it works

The lists store digits least-significant first, so advancing both heads walks the numbers in the same order as hand addition. `divmod(total, 10)` separates the output digit from the carry. Processing until the carry is zero guarantees that a final overflow such as `5 + 5 = 10` gets its extra node.

## Edge cases

- Both numbers are zero: the result is a single zero node.
- One list is shorter: missing digits are treated as zero.
- A carry survives after both lists end, adding one new most-significant node.
- Different lengths and multiple carries are handled by the same loop.
- The input lists are not modified.
