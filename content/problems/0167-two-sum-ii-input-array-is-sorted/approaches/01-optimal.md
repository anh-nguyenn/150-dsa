## Idea

Put one pointer at each end. Compare the sum with the target, then move the pointer that cannot possibly be part of a better pair.

## Why it works

If the current sum is below the target, the largest available partner still is not large enough, so the smallest value cannot form the target with anything in the remaining range. Symmetrically, a sum above the target rules out the largest value. Each step discards one value, so the correct pair cannot be skipped.

## Edge cases

The two values may be adjacent, negative, or equal in value at different positions. A pair at the two ends is found on the first comparison. The problem guarantees one answer, but returning an empty list keeps the function total if no pair exists.
