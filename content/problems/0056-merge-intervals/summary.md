Given a collection of intervals, merge every group that overlaps and return the non-overlapping result sorted by start time.

**Example**

```text
[[1,3],[2,6],[8,10],[15,18]]  ->  [[1,6],[8,10],[15,18]]
```

**Constraints, in plain words**

- Between 1 and 10,000 intervals.
- Each interval is `[start, end]` with `start <= end`.
- Intervals that share an endpoint count as overlapping.
- The input may arrive in any order.
- The output must be sorted and must not contain overlapping intervals.

[Merge Intervals on LeetCode](https://leetcode.com/problems/merge-intervals/)
