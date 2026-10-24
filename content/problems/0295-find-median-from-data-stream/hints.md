## Hint 1

Which two values matter for the median when the count is even? For an odd count, which single value matters?

## Hint 2

If you split the numbers into a lower half and an upper half, what do you need to know about the largest lower value and the smallest upper value?

## Hint 3

Keep a max-heap for the lower half and a min-heap for the upper half. Rebalance after each insertion so their sizes differ by at most one, then read the roots.
