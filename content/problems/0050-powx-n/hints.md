## Hint 1

How many multiplications does it take to build `x^8` if you keep squaring the current value instead of multiplying by `x` eight times?

## Hint 2

The binary form of the exponent marks which powers of two add up to it. Which bits should cause the current squared power to be folded into the answer?

## Hint 3

For a negative exponent, invert `x` and make the exponent positive. Then repeatedly square the base and halve the exponent, multiplying into the result when the low bit is set.
