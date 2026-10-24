You are given intervals and a list of query points. For each query, find the length of the shortest interval that contains that point. Length is `end - start + 1`. If no interval contains the query, answer `-1`.

**Example**

```text
intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]  ->  [3,3,1,4]
```

At query 4, the single-point interval `[4,4]` has length 1 and wins.

**Constraints, in plain words**

- Up to 100,000 intervals and 100,000 queries.
- Each interval has `start <= end`.
- A query on an interval's endpoint counts as inside.
- Answers must follow the original query order.
- Length includes both endpoints.

[Minimum Interval to Include Each Query on LeetCode](https://leetcode.com/problems/minimum-interval-to-include-each-query/)
