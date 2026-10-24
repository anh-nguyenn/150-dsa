Given meeting intervals, return the minimum number of rooms needed so that every meeting has a room and no room hosts overlapping meetings.

**Example**

```text
[[0,30],[5,10],[15,20]]  ->  2
```

The long meeting needs its own room while the other two share one.

**Constraints, in plain words**

- Between 0 and 10,000 meetings.
- Each interval is `[start, end]` with `start < end`.
- A room becomes free exactly when a meeting ends, so touching endpoints can reuse it.
- The input is not necessarily sorted.

[Meeting Rooms II on LeetCode](https://leetcode.com/problems/meeting-rooms-ii/)
