A fixed-width binary word has a leftmost and a rightmost bit. Reversing the word means the bit at position 0 moves to position 31, position 1 moves to 30, and so on. Leading zeros are part of the word, so they become trailing zeros after reversal.

The task is easier if you build the answer from left to right: take one bit from the input's right end, then shift it into the growing answer.

### Everyday examples

- **Reversing a queue.** The person at the front moves to the back, one at a time, until the whole line has turned around.
- **Flipping a row of books.** Moving the rightmost book to the left of the shelf repeatedly produces the reversed row.

### How it shows up here

In each of 32 rounds, read the input's lowest bit with `n & 1`, append it to the answer with `answer = (answer << 1) | bit`, and discard it from the input with `n >>= 1`. After 32 rounds every original bit has moved across the full width.
