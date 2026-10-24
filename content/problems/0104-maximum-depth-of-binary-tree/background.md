The depth of a tree is the length of its longest downward path, counted in nodes. This is also called the tree's height in many descriptions. Only descent matters: a path never reverses direction or visits two branches.

### Everyday examples

- **Nested folders.** A folder inside a folder inside a folder has depth three. The deepest chain of folders is what you report, not the total number of folders.
- **Family generations.** If you count from an ancestor down to the most distant descendant, you get the number of generations along the longest line.

### How it shows up here

At any node, the longest path below it must start by entering either the left child or the right child. So the node's depth is one plus whichever child subtree is deeper. Empty subtrees contribute zero, which gives the recursion a natural stopping point.
