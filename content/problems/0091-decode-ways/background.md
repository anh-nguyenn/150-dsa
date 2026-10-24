Dynamic programming is what you use when a big question can be answered by combining answers to smaller versions of itself. Instead of re-deciding the whole string, you record how many ways each prefix can be read and extend that knowledge one character at a time.

### Everyday examples

- **Stairs.** The number of ways to reach step 10 depends on the ways to reach steps 8 and 9, because the last move is either two steps or one.
- **Tiles.** Laying a strip with tiles of two lengths: the final tile covers either the last unit or the last two units, and the earlier part is an independent smaller problem.
- **Coupon codes.** A scanner can read a code as single symbols or as paired symbols; counting valid readings follows the same prefix pattern.

### How it shows up here

A decoding of the string either ends with one digit (a letter from 1 to 9) or with two digits (a letter from 10 to 26). Those two cases do not overlap and together cover every decoding. That makes the count for a prefix the sum of the counts for the previous one or two prefixes, as long as the final piece is legal. The only subtlety is zero: it cannot stand alone, and it can only be the second digit of 10 or 20.
