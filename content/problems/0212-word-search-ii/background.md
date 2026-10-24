Backtracking explores a grid by choosing a cell, moving through neighbours, and undoing the choice when a path stops being useful. A trie complements backtracking by grouping words with shared prefixes, so one grid walk can test many words at once and stop as soon as no dictionary word continues along that path.

### Everyday examples

- **Word puzzles.** In a letter grid, a player traces words by moving between touching squares without lifting a finger or revisiting a square.
- **Route planning with shared roads.** Several destinations share the same early roads, so one exploration can branch toward all of them instead of starting over for each destination.

### How it shows up here

All target words go into a trie. Starting from every board cell, a depth-first search follows the trie only when the board letter has a matching child. Hitting a terminal node records that word once, and dead trie branches are removed so later searches skip them.
