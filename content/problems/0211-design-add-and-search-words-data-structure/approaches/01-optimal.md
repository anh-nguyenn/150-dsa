## Idea

Build a trie from the stored words, with a marker at each node that ends a complete word. Search with a recursive function that consumes one pattern character per call.

A literal character has only one possible child. A dot branches into every child, and the search succeeds as soon as any branch reaches the end marker at the same pattern position.

## Why it works

The recursion maintains the invariant that `index` characters of the pattern have matched the path to the current node. A literal advances only when the child exists, and a dot tries exactly the children that could supply the next character. If a branch reaches the end of the pattern on a marked node, that stored word matches the full pattern.

## Edge cases

- A pattern consisting only of dots succeeds if any stored word has the same length.
- Dots never match zero characters, so pattern length must equal word length.
- An empty stored word is marked at the root, and an empty pattern then matches it.
- A missing literal child prunes that branch immediately.
- Multiple dots multiply the branching factor, which is why the worst-case search cost depends on the number of dots.
