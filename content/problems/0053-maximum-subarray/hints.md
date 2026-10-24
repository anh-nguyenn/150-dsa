## Hint 1

Focus on slices that end at the current position. What single number from the previous position would let you update that best?

## Hint 2

If the best slice ending just before the current position has a negative sum, adding it only hurts. The current value is a better fresh start.

## Hint 3

Carry a running best-ending-here and a global best. Update both as you move left to right, and the global best is the answer.
