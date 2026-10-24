## Idea

Walk through the tokens once. Numbers are pushed onto a stack. An operator removes the top two numbers, applies itself in the correct order, and pushes the result. After the final token, the stack contains exactly one value: the answer.

## Why it works

In postfix order, every operator's operands are the most recently produced values that have not yet been consumed. The stack holds precisely those pending values. Popping gives the right operand first and the left operand second, which matters for subtraction and division. Because the input is a valid expression, the stack never underflows and finishes with one value.

## Edge cases

- A single number with no operator is a valid expression and returns that number.
- Negative results from subtraction require keeping the operand order.
- Division truncates toward zero: `7 / -2` becomes `-3`, not `-4`. Python's `//` rounds down, so use truncation instead.
- Division by a negative number follows the same truncation rule.
- Large intermediate values are safe because the final result is guaranteed to fit in 32 bits.
