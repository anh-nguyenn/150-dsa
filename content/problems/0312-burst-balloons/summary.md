Each balloon has a number written on it. Bursting a balloon earns the product of its number and the numbers on its current left and right neighbors. If a neighbor is missing, treat its value as 1. Choose an order that bursts every balloon and return the maximum total coins.

**Example**

```text
nums = [3, 1, 5, 8]  ->  167
```

Bursting `1`, then `5`, then `3`, then `8` earns `15 + 120 + 24 + 8 = 167`, which is optimal.

**Constraints, in plain words**

- There are between 0 and 300 balloons.
- Each balloon value is between 0 and 100.
- Missing neighbors count as 1.

[Burst Balloons on LeetCode](https://leetcode.com/problems/burst-balloons/)
