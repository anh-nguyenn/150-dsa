A linked list is a chain of boxes, where each box holds a value and an arrow to the next box. The chain has no index table, so reaching the end means following arrows one at a time. Reversing the chain means changing the direction of every arrow, not moving the values around.

### Everyday examples

- **Turning a line of people around.** Each person keeps hold of the person in front, but to face the other way everyone must let go and reconnect in the opposite direction. You cannot let go of the next person until you remember who that is.
- **Re-hanging a chain of paper clips.** To hang the same clips in the opposite order, you detach one clip at a time and attach it to a growing chain, while keeping the untouched remainder in view.

### How it shows up here

The task is exactly this re-linking. The tricky part is that once a node's `next` arrow is redirected, the rest of the list becomes unreachable unless that remainder was saved first. A small set of pointers keeps the reversed part, the current node, and the unprocessed part separate.
