Make a deep copy of a linked list whose nodes each have a `next` pointer and a `random` pointer. The copy must have the same values and the same pointer relationships, and no copied node may point into the original list.

**Example**

```text
[[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]
```

Each pair is `[value, random_index]`, where `random_index` is the position of the node referenced by `random`, or `null` for no reference.

**Constraints, in plain words**

- The list holds between 0 and 1,000 nodes.
- Values are between -10,000 and 10,000.
- A `random` pointer is either `null` or points to a node in the same list.
- The empty list is allowed.

[Copy List With Random Pointer on LeetCode](https://leetcode.com/problems/copy-list-with-random-pointer/)
