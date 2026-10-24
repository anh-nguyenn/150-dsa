## Idea

At every step, use the endpoints to decide which half is sorted. If the left half is sorted, the target can only be there when it lies between the left endpoint and the middle; otherwise it must be in the right half. If the left half is not sorted, the right half is, and the same range test picks a side.

## Why it works

A rotated sorted array has exactly one place where values drop. A midpoint divides the range so that at least one side does not cross that drop, making that side sorted. Within a sorted side, comparing the target with the side's smallest and largest values decides membership exactly. The algorithm always moves to a side that could contain the target, so it never discards a valid answer. Each step halves the range, and an empty range proves absence.

## Edge cases

- A one-element array is checked directly.
- A target equal to the middle is returned immediately.
- The array may not be rotated at all, in which case the left half is always sorted.
- The target may be the smallest or largest value, at the rotation seam.
- Strictly increasing halves let the range tests use inclusive lower and exclusive upper bounds without ambiguity.
