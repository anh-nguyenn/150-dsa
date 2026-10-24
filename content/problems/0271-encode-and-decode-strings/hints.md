## Hint 1

If you join the strings with a comma, what happens when one of the strings itself contains a comma? Is there any single character guaranteed to be absent?

## Hint 2

To know where a string ends without relying on a forbidden character, what extra information could you store next to its characters?

## Hint 3

Prefix each string with its length and a delimiter. When decoding, read the number, consume exactly that many characters, and repeat. An empty list can encode as an empty string.
