## Idea

Binary search a cut in the shorter array. The cut in the longer array is determined by the size of the left half. Accept the cut when the largest value left of both cuts is no larger than the smallest value right of both cuts. Then the median is either the maximum left value or the average of the maximum left and minimum right values.

## Why it works

Every valid split puts exactly `(m + n + 1) // 2` elements on the left, with one cut in each array. If `left1 <= right2` and `left2 <= right1`, all left values are no larger than all right values, so the merged middle values must be `max(left1, left2)` and `min(right1, right2)`. If `left1 > right2`, the cut in the first array is too far right and must move left; otherwise it is too far left and must move right. Searching the shorter array keeps the derived cut in range. The sentinels handle cuts at the array edges.

## Edge cases

- One array may be empty; the median comes entirely from the other.
- An odd total returns the single middle value as a float.
- An even total averages the two middle values.
- Duplicate values are fine because the condition uses `<=` and `<` consistently.
- Cuts at the beginning or end use negative and positive infinity sentinels, so no boundary check is needed around the comparison.
- Swapping arrays ensures the binary search runs on the shorter one, keeping the other cut valid.
