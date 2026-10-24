You start at index 0 of a non-empty array, where each value is the maximum forward jump from that index. Return the smallest number of jumps needed to reach the last index. The input is guaranteed to be reachable.

**Examples**

```text
nums = [2, 3, 1, 1, 4]  ->  2
nums = [2, 3, 0, 1, 4]  ->  2
```

In the first case, jump from 0 to 1, then from 1 to 4. Two jumps is the minimum.

**Constraints, in plain words**

- Between 1 and 10,000 positions.
- Each jump length is between 0 and 1,000.
- You may jump fewer steps than the number allows.
- The last index can always be reached.
- A one-element array needs zero jumps.

[Jump Game II on LeetCode](https://leetcode.com/problems/jump-game-ii/)
