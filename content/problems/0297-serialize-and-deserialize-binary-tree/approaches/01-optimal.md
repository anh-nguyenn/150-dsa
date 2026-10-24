## Idea

Serialize with a pre-order walk: append the current value, then the encoding of the left subtree, then the right subtree, and append a reserved `null` token for every empty child. Join the tokens with commas. Deserialize by reading tokens in the same order: a `null` token becomes an empty child, while any other token creates a node and recursively builds its left and right children.

The null markers are the key. They tell the decoder when a branch has ended, so the token stream is unambiguous even for trees with only one child.

## Why it works

Pre-order encodes a subtree as its root followed by both child encodings, and the decoder consumes tokens in exactly that order. By induction, a real token is matched with its left encoding and then its right encoding, reconstructing the same links. Every node contributes one value token and every missing child contributes one null token, so the decoder always has enough information and finishes at the right place. Both directions visit each node once, with one token per node or missing child.

## Edge cases

- An empty tree serializes to an empty string, which decodes back to no tree.
- A node with only a right child still gets a null token for the missing left child.
- Negative values and multi-digit values are separated by commas and parsed with `int`.
- A long skewed tree uses recursion depth proportional to its height.
- A fresh iterator is created per deserialize call, so repeated use of one codec does not share state.
