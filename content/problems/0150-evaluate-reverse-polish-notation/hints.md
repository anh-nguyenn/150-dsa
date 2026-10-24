## Hint 1

Which values does an operator need, and where should the result go so a later operator can use it?

## Hint 2

When you pop two numbers for subtraction or division, which one is the left operand?

## Hint 3

Use one stack. Push numbers; for an operator, pop `b` then `a`, compute `a op b`, and push the result. Truncate division toward zero.
