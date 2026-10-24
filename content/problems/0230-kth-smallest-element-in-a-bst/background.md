An in-order traversal visits a binary tree's left subtree, then the node, then its right subtree. In a binary search tree, that order is sorted ascending. The same walk can be written with a stack instead of recursion: go as far left as possible, visit that node, then move to its right subtree and repeat.

### Everyday examples

- **Reading a dictionary.** Entries are already alphabetical, so the tenth entry is found by counting forward, not by sorting again.
- **A stack of numbered tickets.** You keep taking the top ticket until the number you need appears. The order is fixed; you only count.

### How it shows up here

The k-th smallest value is a stopping point in the sorted in-order sequence. Instead of storing the whole sequence, an iterative traversal counts nodes as it visits them and stops as soon as the count reaches `k`.

The stack only holds the path from the root to the current node, so the extra memory is proportional to the tree height rather than the number of nodes.
