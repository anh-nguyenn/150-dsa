## Idea

Walk from the least significant digit. Increment the first digit that is not 9; turn every 9 passed along the way into 0.

## Why it works

A digit less than 9 can absorb the carry without propagating further, so the number is complete at that point. A 9 cannot represent the extra one, so it becomes 0 and the carry continues left. If the loop finishes, every original digit was 9, and the only correct representation is a new leading 1 followed by zeros.

## Edge cases

- `[0]` becomes `[1]`.
- `[9]` becomes `[1, 0]`.
- A trailing 9 such as `[1, 9]` becomes `[2, 0]`.
- All 9s require a longer list, which the final prepend handles.
- A number ending in a digit below 9 returns after changing only that digit.
