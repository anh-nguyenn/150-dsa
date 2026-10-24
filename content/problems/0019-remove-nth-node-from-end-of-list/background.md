Removing a node from a singly linked list requires standing at the node just before it, because that is the only node whose `next` can be changed. Counting from the end is awkward when the length is unknown, but two pointers can maintain a fixed distance without a separate length pass.

### Everyday examples

- **A bookmark near the end of a book.** If a friend holds a marker `n` pages ahead of yours, then when the friend reaches the last page, your marker is exactly `n` pages from the end.
- **Two cars keeping a gap.** A lead car stays a fixed distance ahead. When the lead car reaches the finish line, the trailing car is that same distance behind it.

### How it shows up here

Advance a fast pointer `n` steps into the list, then move fast and slow together until fast is at the last node. The gap of `n` means slow is now just before the node to delete. A dummy node before the head makes removing the original head no different from removing any other node.
