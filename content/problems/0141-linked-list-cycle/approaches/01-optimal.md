## Idea

Start both pointers at the head. Move `slow` one node and `fast` two nodes each round. If the list ends, `fast` or `fast.next` becomes `None`. If a cycle exists, both pointers stay inside it, and the faster pointer closes the gap until they are the same node.

## Why it works

On a finite list, `fast` reaches the end, so the loop terminates with `False`. On a cycle, the distance between the pointers shrinks by one on every step, so they must eventually coincide. Only two references are stored, independent of list length.

## Edge cases

- Empty list: `fast` is `None` immediately, so the answer is `False`.
- One node pointing to itself: both pointers meet on the first step.
- A cycle that begins at the head: the pointers may meet before returning to the head, but a meeting still proves a cycle.
- A list that ends normally after many nodes: `fast` reaches `None`.
- Even-length and odd-length cycles both cause a meeting.
