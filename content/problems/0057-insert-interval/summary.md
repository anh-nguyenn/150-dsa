You are given a list of non-overlapping intervals sorted by start time, plus one new interval. Insert the new interval, merging any intervals that now overlap, and return the resulting sorted list.

**Example**

```text
intervals = [[1,3],[6,9]], newInterval = [2,5]  ->  [[1,5],[6,9]]
```

**Constraints, in plain words**

- Up to 10,000 existing intervals.
- Each interval is `[start, end]` with `start <= end`.
- The existing intervals are already sorted and do not overlap.
- Intervals that only touch at an endpoint count as overlapping for merging.
- The result must be sorted and non-overlapping.

[Insert Interval on LeetCode](https://leetcode.com/problems/insert-interval/)
