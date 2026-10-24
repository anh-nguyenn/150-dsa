## Hint 1

How does the binary form of `i` relate to the binary form of `i // 2`?

## Hint 2

The only difference is the last bit, which is either 0 or 1.

## Hint 3

Build the table in increasing order: reuse the count for `i >> 1` and add `i & 1`.
