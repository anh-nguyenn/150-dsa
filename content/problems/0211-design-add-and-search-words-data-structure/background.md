A trie shares prefixes among words, which makes exact lookups and prefix lookups efficient. A wildcard adds branching: at a dot, several trie children may be valid continuations. Backtracking explores those branches and abandons any that cannot match the rest of the pattern.

### Everyday examples

- **Crossword helper.** A solver knows some letters and leaves blanks for the others, then looks for dictionary words that fit the known pattern.
- **Log filtering.** A search pattern like `err.r` matches several error labels while still fixing the letters around the unknown position.

### How it shows up here

`addWord` builds the same character tree as a normal trie and marks the final node. `search` walks the pattern recursively. A normal letter follows one child, while a dot tries every child and succeeds if any branch finishes on a marked node.
