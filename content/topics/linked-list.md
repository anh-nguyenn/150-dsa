# Linked List

A linked list trades random access for cheap local edits. Most problems are pointer surgery: keep the nodes you still need, rewire a few links, and never lose the rest of the list.

Reach for it when the problem asks for in-place reordering, removal, merging, or cycle detection. Dummy heads, a slow/fast pair, and a temporary next pointer prevent most mistakes.

It assumes you can draw the list before and after each pointer change.
