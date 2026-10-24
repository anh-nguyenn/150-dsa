## Idea

Put pointers at the two ends. Compute the area, then move inward the pointer whose line is shorter, because that shorter line is the bottleneck.

## Why it works

For the current pair, the shorter line caps the area. While that line stays in place, any narrower pair using it has no more height and less width, so none can beat the current area. Discarding it is therefore safe. Every pair is either evaluated or eliminated by this argument, so the maximum is found.

## Edge cases

Two lines produce the only possible area. A zero-height line yields zero area. Equal heights can be handled by moving either pointer. The array is scanned once, so very tall or very short lines do not change the logic.
