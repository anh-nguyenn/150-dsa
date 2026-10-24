Given intervals, remove the fewest possible so that the remaining intervals do not overlap. Intervals that only touch at an endpoint are compatible.

**Example**

```text
[[1,2],[2,3],[3,4],[1,3]]  ->  1
```

Removing `[1,3]` leaves three compatible intervals.

**Constraints, in plain words**

- Between 1 and 100,000 intervals.
- Each interval is `[start, end]` with `start < end`.
- Touching endpoints are allowed, so `[1,2]` and `[2,3]` do not conflict.
- Return the count of removed intervals, not the list.

[Non Overlapping Intervals on LeetCode](https://leetcode.com/problems/non-overlapping-intervals/)
