## Hint 1

A part cannot end before the final occurrence of every letter it contains. What information about each letter would let you know when a part is safe to close?

## Hint 2

While sweeping, a new letter inside the current part may force the part's endpoint farther to the right. Keep extending the endpoint until the current index catches up with it.

## Hint 3

Precompute each letter's last index. Close a part when the scan reaches the farthest last occurrence seen so far, then begin the next part.
