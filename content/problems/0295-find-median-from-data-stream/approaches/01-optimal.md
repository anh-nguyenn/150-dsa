## Idea

Store the lower half of the numbers in a max-heap and the upper half in a min-heap. After each insertion, move the largest lower value into the upper heap, then move the smallest upper value back if the upper heap became larger.

This keeps the lower heap equal in size to the upper heap or one larger. The median is the lower root for an odd count, or the average of the two roots for an even count.

## Why it works

Every value in the lower heap is at most every value in the upper heap. With sizes balanced to within one, the roots are the two middle values of the sorted sequence. For an odd count the extra value lives in the lower heap, so its maximum is the single middle value; for an even count the two roots are the pair to average.

## Edge cases

- One value makes the median the value itself.
- Duplicate values are stored independently and do not break the ordering.
- Negative values are handled by the same heap comparisons.
- An even count averages two integers, so the result may be a half-integer.
- The heaps stay balanced after every insertion, including when a value belongs on the other side of the current median.
