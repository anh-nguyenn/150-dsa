## Idea

XOR every index and every value. The indices stand in for the complete range 0 through `n`, so the only value without a match is the one missing from the array.

## Why it works

The complete range is represented by the indices 0 through `n - 1` together with the initial value `n`. Every array value that also belongs to that range cancels with its matching index or with `n`. Because the array has distinct values and only one is absent, exactly one value remains.

## Edge cases

- When the missing value is `n`, no index equals it; the initial `missing = len(nums)` supplies it after all other values cancel.
- When the missing value is 0, index 0 cancels with nothing in the array and survives.
- A single-element array `[0]` returns 1, while `[1]` returns 0.
- Values need not be sorted, and no extra memory is required.
