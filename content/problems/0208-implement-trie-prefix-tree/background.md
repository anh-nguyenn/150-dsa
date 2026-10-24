A trie is a tree of characters. Each path from the root spells a prefix, so words that begin the same way share the same early nodes. A terminal marker at a node records that the path ending there is a complete stored word.

### Everyday examples

- **Search suggestions.** Typing `car` can suggest `car`, `card`, and `care` because they share the same first three letters.
- **File paths.** Directories share common parent folders, so looking up a path only requires walking the components that actually exist.

### How it shows up here

Each node holds a map from the next character to a child node plus a flag saying whether a word ends there. Insertion walks or creates the path and marks the final node. `search` and `startsWith` walk the same path, but only `search` checks the terminal flag at the end.
