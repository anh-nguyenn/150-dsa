## Hint 1

For a bar of a given height, how far can it extend before a shorter bar blocks it?

## Hint 2

When a new bar is shorter than the bar on top of the stack, what do you now know about the top bar's right boundary?

## Hint 3

Keep indices with increasing heights. Pop taller bars when a shorter one arrives, use the new index and the index below on the stack as boundaries, and add a zero sentinel at the end.
