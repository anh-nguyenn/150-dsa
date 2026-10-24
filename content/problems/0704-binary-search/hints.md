## Hint 1

After comparing the middle value with the target, which part of the array can you safely ignore?

## Hint 2

What invariant should the two boundary indices maintain, and when should the loop stop?

## Hint 3

Keep a closed range `[lo, hi]`. Compare the midpoint, move one boundary past it, and return -1 once `lo` passes `hi`.
