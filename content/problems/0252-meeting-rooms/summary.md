Given meeting intervals, decide whether one person can attend every meeting. Meetings that merely touch, such as one ending at 10 and another starting at 10, do not conflict.

**Example**

```text
[[0,30],[5,10],[15,20]]  ->  false
```

`[5,10]` overlaps `[0,30]`, so the person cannot attend both.

**Constraints, in plain words**

- Between 0 and 10,000 meetings.
- Each interval is `[start, end]` with `start < end`.
- A meeting may start at the same moment another ends.
- The input is not necessarily sorted.

[Meeting Rooms on LeetCode](https://leetcode.com/problems/meeting-rooms/)
