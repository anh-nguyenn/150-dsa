A shallow copy duplicates the outer container but lets the contents share the same underlying objects. A deep copy duplicates every object as well, so changing the copy cannot change the original. When objects point to each other, the copy must preserve the shape of those relationships using copies, not originals.

### Everyday examples

- **Photocopying a family tree.** Each copied person needs an arrow to the copied favorite relative, not an arrow back into the original chart.
- **Duplicating a set of linked folders.** Every copied folder should point to another copied folder, so editing the duplicate leaves the original untouched.

### How it shows up here

The `next` chain is easy to copy in order, but `random` pointers may jump backward or forward to nodes that have not been copied yet. A dictionary keyed by the original node solves this: once every original has a copy, each `next` and `random` can be translated through the map.
