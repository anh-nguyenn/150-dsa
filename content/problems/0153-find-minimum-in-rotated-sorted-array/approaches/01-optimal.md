## Idea

Keep a search range whose right endpoint is a candidate for the minimum. Compare the middle value with the rightmost value. If the middle is no larger, the minimum is in the left part including the middle. If the middle is larger, the minimum is strictly to the right.

## Why it works

Without a wrap, values increase from left to right, and the middle is smaller than the right end, so the minimum is at the left edge of the current range. With a wrap inside the range, the drop is either at or left of the middle when the middle is smaller than the right end, or strictly right of the middle when the middle is larger. The comparison identifies which run the middle belongs to, and the range always keeps the seam. Equal endpoints cannot occur because values are distinct, and the loop ends at the minimum.

## Edge cases

- An unrotated array such as `[11,13,15,17]` returns its first value.
- A single element is already the minimum.
- In a two-element rotated array, the comparison moves the range to the smaller value.
- A rotation that puts the minimum at the last index is found by moving the left edge right.
- Distinct values avoid ambiguity when the middle equals the right endpoint.
