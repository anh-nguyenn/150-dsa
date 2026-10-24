## Hint 1

If you knew the length, you could walk to the node before the target. Can you find that node without a separate pass?

## Hint 2

Start one pointer `n` steps ahead of another. What does that gap tell you when the leader reaches the end?

## Hint 3

Put a dummy node before the head. Advance a fast pointer `n` steps, then move fast and slow until fast is last. Skip the node after the slow pointer.
