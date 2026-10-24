## Hint 1

The string must capture shape, not just values. How will the decoder know that a node has no left child?

## Hint 2

Write the tree in pre-order and emit an explicit marker whenever a child is empty. Can the decoder follow the same order?

## Hint 3

Join tokens with a delimiter. During decoding, consume the next token: a marker means an empty child, and any other token becomes a node whose two children are decoded recursively.
