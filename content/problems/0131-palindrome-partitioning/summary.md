Given a string, split it into pieces so that every piece is a palindrome. Return every possible way to do the splitting. The partitions may be returned in any order, but the pieces inside one partition must stay in their original left-to-right order.

**Example**

```text
s = "aab"
-> [["a", "a", "b"], ["aa", "b"]]
```

`"aab"` as a single piece is not a palindrome, so it is not a valid partition.

**Constraints, in plain words**

- The string has between 1 and 16 lowercase English letters.
- Every piece must be a palindrome and must be non-empty.
- The pieces, in order, must spell the original string exactly.
- Different cut positions count as different partitions.

[Palindrome Partitioning on LeetCode](https://leetcode.com/problems/palindrome-partitioning/)
