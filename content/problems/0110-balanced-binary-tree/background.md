A height-balanced tree keeps its two sides at every node within one level of each other. The rule is local at each node but applies everywhere: a tree can look even at the root and still be unbalanced deep inside one branch.

### Everyday examples

- **A hanging mobile.** Each hook must hold two sides of similar weight and length. One lopsided lower hook spoils the whole mobile even if the top looks level.
- **A staircase.** Every step should rise by roughly the same amount. One unusually tall step makes the climb uneven, no matter how regular the other steps are.

### How it shows up here

The check needs two pieces of information from each subtree: its height and whether it is already balanced. Trying to recompute heights at every node would repeat work. A single bottom-up pass can return the height when the subtree is balanced and a sentinel value when it is not, letting the failure propagate to the root.
