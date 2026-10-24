## Idea

Maintain one running value and XOR each array element into it. Equal values cancel in pairs, so only the unpaired value remains.

## Why it works

XOR is associative and commutative, so grouping the elements differently cannot change the result. Every value with a twin contributes `x ^ x = 0`, and the sole unpaired value contributes `x ^ 0 = x`.

## Edge cases

- A single-element array returns that element immediately.
- Zero may be the lone value, or it may be one of the repeated values.
- Negative numbers work because XOR is defined bitwise on their two's-complement representation; Python's integer semantics still cancel equal values.
- No sorting or extra storage is needed, so duplicates in any position are handled.
