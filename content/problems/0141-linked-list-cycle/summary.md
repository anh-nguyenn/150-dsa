Decide whether a singly linked list contains a cycle. A cycle exists when repeatedly following `next` eventually returns to a node already visited instead of reaching `None`.

**Example**

```text
3 -> 2 -> 0 -> -4
     ^         |
     +---------+          has a cycle  ->  true

1 -> 2 -> None            no cycle     ->  false
```

**Constraints, in plain words**

- The list holds between 0 and 10,000 nodes.
- Values are between -100,000 and 100,000.
- A cycle, if present, starts at some node position; otherwise the list ends normally.
- The empty list has no cycle.

[Linked List Cycle on LeetCode](https://leetcode.com/problems/linked-list-cycle/)
