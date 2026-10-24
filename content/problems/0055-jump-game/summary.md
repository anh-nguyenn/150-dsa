You start at the first position of an array. Each number tells you the maximum number of steps you may jump forward from that position. Decide whether you can reach the final position.

**Examples**

```text
nums = [2, 3, 1, 1, 4]  ->  true
nums = [3, 2, 1, 0, 4]  ->  false
```

In the first case you can step from index 0 to 1, then from 1 to 4. In the second, index 3 has a jump length of zero and blocks the way to index 4.

**Constraints, in plain words**

- Between 1 and 10,000 positions.
- Each jump length is between 0 and 100,000.
- You may jump fewer steps than the number allows, including zero.
- Reaching the last index is the goal; you do not need to stop exactly on it from a jump that overshoots.

[Jump Game on LeetCode](https://leetcode.com/problems/jump-game/)
