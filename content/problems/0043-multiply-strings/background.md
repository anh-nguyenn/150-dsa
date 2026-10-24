Long multiplication breaks a product into many single-digit products. Each pair of digits contributes to two neighboring places, because a digit's value depends on its position. The final answer is obtained by adding all those contributions while resolving carries from right to left.

### Everyday examples

- **Multiplying prices on paper.** You multiply each digit of one price by each digit of the other and line up the partial answers by place value.
- **An abacus.** Beads in different columns represent different powers of ten, and carrying moves extra beads from one column to the next.

### How it shows up here

If positions are counted from the right, the digit at position `i` of the first number and the digit at position `j` of the second contribute to positions `i + j` and `i + j + 1`. An array of length `m + n` is just enough to hold every place, including the final carry. After all digit pairs are processed, leading zeros are trimmed to produce the string.
