## Idea

Maintain a closed range of indices that could still contain the target. Compare the middle element with the target. If it is too small, move the left boundary to the right of the middle; if it is too large, move the right boundary to the left of the middle. Stop when the range is empty.

## Why it works

Sorted order guarantees that if the middle value is less than the target, every value to its left is also less, so none of them can be the target. The symmetric argument holds when the middle is too large. Each comparison therefore discards at least half of the remaining candidates. Either the target is found at a midpoint, or the range empties, proving it is absent.

## Edge cases

- A one-element array is checked once and then the range empties.
- The target may be the first or last element.
- A target smaller than every value or larger than every value returns -1.
- Negative values are handled by ordinary comparison.
- The midpoint calculation stays within bounds for the stated input sizes.
