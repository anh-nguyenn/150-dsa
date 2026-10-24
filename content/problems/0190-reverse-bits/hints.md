## Hint 1

How can you read just the least significant bit of the input?

## Hint 2

Each answer bit should receive the next input bit while shifting the answer left.

## Hint 3

Repeat exactly 32 times: append `n & 1` to the answer, then shift the answer left and the input right as needed.
