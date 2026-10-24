## Hint 1

Checking each word separately against the board repeats the same prefix work. What structure can share prefixes across all target words?

## Hint 2

During a grid walk, how can you tell immediately that the current sequence cannot become any target word and should be abandoned?

## Hint 3

Put every word in a trie. Run DFS from each cell, following a child only when the cell letter matches. Mark words when reached, and prune trie leaves that can no longer produce new matches.
