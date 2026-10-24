## Hint 1

At every step, which two stones must be removed? What data structure makes finding them fast?

## Hint 2

Python's heap is a min-heap. Can you store the weights in a form that makes the largest weight come out first?

## Hint 3

Use negated weights in a min-heap. Pop twice per round, push the positive difference back when it is nonzero, and continue until the heap has zero or one stone.
