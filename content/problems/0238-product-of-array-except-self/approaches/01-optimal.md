## Idea

Fill the result with the product of all elements to the left of each index, then sweep backward with a running product of the elements to the right and multiply it into each slot.

## Why it works

Before the backward pass, `result[i]` is the product of `nums[0]` through `nums[i-1]`. During the backward pass, `suffix` is the product of `nums[i+1]` through the end. Multiplying them gives every element except `nums[i]`. Each element is used once in each pass, so the time is linear, and the output array is the only list allocated.

## Edge cases

- A single zero makes every answer zero except the position of that zero, which gets the product of the nonzero values.
- Two or more zeros make every answer zero.
- Negative values are handled automatically; an odd number of negatives gives a negative product.
- The minimum length of 2 removes the need to special-case an empty input.
- A single-element input would return 1 for its only position, consistent with an empty product.
