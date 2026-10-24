## Hint 1

For one position, the answer is the product of everything to its left times the product of everything to its right. Could one of those sides be computed in a single forward pass?

## Hint 2

If the output already holds the left products, what running value during a backward pass would let you finish each slot without a second array?

## Hint 3

Write prefix products into the result from left to right. Then sweep from right to left with a running suffix product, multiplying it into each result slot.
