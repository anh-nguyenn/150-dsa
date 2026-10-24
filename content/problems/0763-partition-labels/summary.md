You are given a string of lowercase letters. Cut it into the largest possible number of contiguous parts so that no letter appears in more than one part. Return the lengths of the parts in left-to-right order.

**Example**

```text
s = "ababcbacadefegdehijhklij"  ->  [9, 7, 8]
```

The parts are `"ababcbaca"`, `"defegde"`, and `"hijhklij"`. Each letter appears in only one of them.

**Constraints, in plain words**

- The string has between 1 and 500 lowercase letters.
- Parts must be contiguous and cover the whole string.
- Once a letter appears in a part, it may not appear in any other part.
- More parts are better, as long as the rule holds.

[Partition Labels on LeetCode](https://leetcode.com/problems/partition-labels/)
