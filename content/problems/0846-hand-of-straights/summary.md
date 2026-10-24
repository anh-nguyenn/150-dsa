You are given a hand of numbered cards and a group size. Decide whether every card can be split into groups of exactly `group_size` cards whose values are consecutive integers.

**Example**

```text
hand = [1, 2, 3, 6, 2, 3, 4, 7, 8], group_size = 3  ->  true
```

The groups can be `[1, 2, 3]`, `[2, 3, 4]`, and `[6, 7, 8]`.

**Constraints, in plain words**

- Between 1 and 10,000 cards.
- Card values are between 0 and 1,000,000,000.
- The group size is between 1 and the number of cards.
- Every card must be used exactly once.
- Within a group, values must increase by one with no gaps.

[Hand of Straights on LeetCode](https://leetcode.com/problems/hand-of-straights/)
