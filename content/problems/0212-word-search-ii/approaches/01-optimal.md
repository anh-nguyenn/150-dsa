## Idea

Insert all target words into a trie, marking terminal nodes with the word itself. Run a depth-first search from every board cell, passing the current trie node along the path.

At each step, follow the child matching the cell letter. If that child ends a word, record it and clear the marker so duplicates are not added again. Mark the cell as visited, explore its four neighbours, then restore it. Remove a trie node when it has no children left.

## Why it works

The DFS enumerates exactly the sequences of adjacent cells that avoid reuse, and the trie accepts only sequences that are prefixes of target words. Clearing a word marker after the first match gives the required uniqueness. Pruning leaf nodes is safe because no remaining word passes through that path, so future searches cannot discover anything there.

## Edge cases

- A one-cell board can match a one-letter word.
- Words that cannot start from any board letter are never explored.
- The same word listed twice is inserted twice but recorded once because its marker is cleared.
- A word cannot reuse a cell; the temporary `#` marker enforces that during each path.
- Shared prefixes such as `do`, `dog`, and `door` are explored together and each match is recorded independently.
- Restoring the board cell after the search keeps later starting positions independent.
