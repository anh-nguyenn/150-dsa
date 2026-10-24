Design a store that saves string values under a key at increasing timestamps. A lookup asks for the value at a key with the largest timestamp not exceeding a given time, or an empty string if no such value exists.

```text
set("foo", "bar", 1)
get("foo", 1)  ->  "bar"
get("foo", 3)  ->  "bar"
set("foo", "baz", 4)
get("foo", 4)  ->  "baz"
```

**Constraints, in plain words**

- Between 1 and 200,000 calls to `set` and `get`.
- Keys and values are lowercase strings of length 1 to 100.
- Timestamps are between 1 and 10^7.
- For a given key, timestamps passed to `set` strictly increase.
- A lookup before a key's first timestamp returns an empty string.

[Time Based Key Value Store on LeetCode](https://leetcode.com/problems/time-based-key-value-store/)
