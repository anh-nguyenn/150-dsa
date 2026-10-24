## Hint 1

If you sorted every value seen so far, where would the kth largest value sit? Which end of the sorted order changes when a new value arrives?

## Hint 2

You do not need to remember values that are already too small to enter the top k. Which single value is safe to drop when a new value arrives?

## Hint 3

Keep a min-heap containing at most k values. After inserting a value, remove the heap minimum if the size exceeds k; the minimum is then the kth largest.
