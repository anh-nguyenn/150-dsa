## Hint 1

In a rotated sorted array, where does the minimum sit relative to the place where the order wraps?

## Hint 2

Compare the middle value with the value at the right end. If the middle is smaller or equal, which side holds the minimum?

## Hint 3

Keep a range ending at a candidate minimum. Move the right edge to the middle when the middle is no larger than the right value; otherwise move the left edge past the middle.
