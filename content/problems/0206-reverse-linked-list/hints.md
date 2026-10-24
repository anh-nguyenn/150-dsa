## Hint 1

If you overwrite a node's `next` pointer, what do you lose unless you save it first?

## Hint 2

Keep one pointer to the part already reversed and one to the part still waiting. Which node should become the new head at the end?

## Hint 3

Walk the list once. Save the next node, point the current node back to the previous one, then move both pointers forward. The old tail becomes the new head.
