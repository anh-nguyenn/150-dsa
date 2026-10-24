Design a `KthLargest` class that tracks a stream of numbers. The constructor receives the rank `k` and an initial list of values. Each call to `add(val)` inserts one value and returns the kth largest value currently in the stream, counting duplicates as separate values.

**Example**

```text
k = 3, nums = [4, 5, 8, 2]
add(3)  -> 4
add(5)  -> 5
```

**Constraints, in plain words**

- `k` is at least 1.
- The initial list has at most 10,000 values.
- There are at most 10,000 calls to `add`.
- Values stay between -10,000 and 10,000.
- Whenever `add` is called, the stream contains enough values to have a kth largest.

[Kth Largest Element in a Stream on LeetCode](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
