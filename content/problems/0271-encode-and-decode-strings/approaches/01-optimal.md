## Idea

Encode every string as its character count, a colon, and the characters. Decode by reading the count up to the colon, then taking exactly that many characters.

## Why it works

The decoder never guesses where a word ends from its contents; it uses the recorded length. A colon or digit inside a word is consumed as part of the fixed-size chunk, so it cannot be mistaken for framing. Every encoded word contributes a length, a colon, and exactly that many characters, so the decoder's position advances past one word at a time and stops precisely at the end of the stream.

## Edge cases

- An empty list encodes to an empty string and decodes back to an empty list.
- An empty string is encoded with length 0 and remains a single empty element.
- Strings containing colons, digits, or the delimiter text are safe because their length is explicit.
- Non-ASCII characters are fine as long as Python string slicing is used consistently.
- Duplicate strings are preserved in order.
