Design a fixed-capacity least-recently-used cache. `get(key)` returns the stored value and marks the key as recently used, or returns `-1` if the key is absent. `put(key, value)` inserts or updates a key; if the cache is full, it evicts the least recently used key first.

**Example** with capacity 2

```text
put(1, 1)   cache: [1]
put(2, 2)   cache: [2, 1]
get(1) -> 1 cache: [1, 2]
put(3, 3)   evicts 2, cache: [3, 1]
get(2) -> -1
```

**Constraints, in plain words**

- Capacity is between 1 and 3,000.
- Keys and values are between 0 and 10,000.
- Up to 200,000 calls may be made.
- Every operation should run in constant time on average.

[LRU Cache on LeetCode](https://leetcode.com/problems/lru-cache/)
