## Idea

Keep two stacks in step: one holds every value, and the other holds the minimum for the current height. Push onto the minimum stack only when the new value ties or beats the old minimum. On pop, remove the minimum entry exactly when the departing value was that minimum.

## Why it works

At every height, the top of the minimum stack is the smallest value among the values currently stored. A new value changes that minimum only if it is no larger than the current one. When a value leaves, the minimum changes only if that value was the recorded minimum, in which case the entry beneath it is the correct earlier minimum. Thus `getMin` is always a direct lookup, and all four operations touch only stack ends.

## Edge cases

- Pushing a value equal to the current minimum still adds a minimum entry, so removing one copy does not lose the minimum.
- Popping a value larger than the minimum leaves the minimum stack alone.
- A one-element stack returns the same value from `top` and `getMin`.
- Negative values are handled like any other value.
- The operations are guaranteed to be valid, so the code does not need empty-stack guards.
