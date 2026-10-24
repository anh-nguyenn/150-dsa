## Idea

Keep a dictionary from key to node for constant-time lookup. Store the nodes in a doubly linked list ordered by recency, with sentinel head and tail nodes. `get` moves a found node to the front. `put` updates and moves an existing node, or inserts a new one at the front and evicts the node just before the tail when capacity is exceeded.

## Why it works

The dictionary finds any node in average constant time. The doubly linked list can detach a node and insert it at the front in constant time because each node knows both neighbors, and sentinels remove boundary special cases. Evicting the least recently used node is just removing `tail.prev` and its dictionary entry.

## Edge cases

- Capacity 1: every new key evicts the previous one.
- Updating an existing key must refresh its recency as well as its value.
- A `get` miss returns `-1` and changes nothing.
- A `get` hit must move the node to the front, or a later eviction may remove the wrong key.
- Repeating a `get` on the same key keeps it at the front without adding duplicates.
