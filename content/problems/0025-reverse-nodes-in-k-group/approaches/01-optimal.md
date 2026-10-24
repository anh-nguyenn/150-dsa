## Idea

Keep a pointer to the node before the current group. Walk `k` steps ahead; if that walk falls off the list, the remaining tail is shorter than `k` and is left alone. Otherwise, reverse the `k` nodes so their last node becomes the group head, then link the previous group's tail to that new head and continue from the group's old first node, which is now its tail.

## Why it works

Each full group is reversed independently while its outside neighbors are saved. The dummy node makes the first group's predecessor valid, so no head special case is needed. The `k`-step check guarantees that a partial tail is never reversed. Every node is visited a constant number of times, and only pointers are stored.

## Edge cases

- `k = 1`: no group changes order.
- Length is an exact multiple of `k`: every group is reversed.
- Length is not a multiple: the final shorter group stays as it was.
- A single node with `k = 1`: returned unchanged.
- An empty list: the first `k`-step walk immediately reaches `None`.
- Reversing the first group changes the head, which the dummy node handles.
