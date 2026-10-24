## Idea

Walk the list once with three pointers. `prev` is the already reversed prefix, `cur` is the node being moved, and `nxt` saves the rest of the list before the link is changed. Point `cur.next` at `prev`, then shift `prev` and `cur` one step forward. When `cur` runs out, `prev` is the new head.

## Why it works

Each node is visited once and its outgoing link is redirected once. Saving `nxt` first keeps the unprocessed suffix reachable, so the reversal can continue. No new nodes, recursion stack, or extra collection is needed.

## Edge cases

- Empty list: the loop never runs and `None` is returned.
- One node: its `next` is already `None`, so it comes back unchanged.
- The original head becomes the tail, and its `next` is set to `None`.
- Duplicate or negative values do not affect the pointer work at all.
