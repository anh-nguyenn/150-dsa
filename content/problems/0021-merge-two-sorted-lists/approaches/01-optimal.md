## Idea

Create a dummy node and let `tail` follow the end of the merged list. While both inputs have nodes, compare their heads, attach the smaller one, and advance that input. When one input runs out, attach the remainder of the other list in one step.

## Why it works

Both input lists are sorted, so the smallest unplaced value is always at one of the two current heads. Choosing the smaller head therefore produces the next value of a sorted merge. Every node is attached once, and only a constant number of pointers are maintained.

## Edge cases

- Both lists empty: the dummy's `next` stays `None`.
- One list empty: the entire other list is attached unchanged.
- Duplicate values: the `<=` comparison keeps them in a stable order.
- One list is completely smaller: the loop drains it, then the whole other list is appended.
- The merge reuses nodes rather than copying values.
