## Idea

Create a dummy node whose `next` is the head. Move `fast` forward `n` times, then move `fast` and `slow` together until `fast` reaches the last node. At that point `slow` is immediately before the node to remove, so skip it with `slow.next = slow.next.next`.

## Why it works

After the initial lead, the distance between `fast` and `slow` is exactly `n`. When `fast` is the last node, the node `n` places ahead of `slow` is no longer reachable past the end, so `slow.next` is the target. The dummy node guarantees that `slow` has a valid predecessor even when the removed node is the original head.

## Edge cases

- `n = 1`: the tail is removed.
- `n` equals the list length: the dummy lets the head be removed.
- Single node: removing it returns an empty list.
- Two nodes: both possible targets are handled by the same gap logic.
- Values never matter, including duplicates.
