## Hint 1

Adding one only affects the end of the number unless a carry is produced. When does the carry stop moving left?

## Hint 2

A digit below 9 simply increases by one. A 9 becomes 0 and sends the carry to its left neighbor.

## Hint 3

Scan from the right. At the first digit below 9, increment it and return. If the whole number was 9s, prepend a 1 after zeroing everything.
