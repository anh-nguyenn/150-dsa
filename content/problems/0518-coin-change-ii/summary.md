Given coin denominations and a target amount, count how many ways to choose coins that add up exactly to the amount. Each denomination may be used any number of times, and different orders of the same coins are considered the same combination.

For `amount = 5` and `coins = [1, 2, 5]` there are `4` ways: `1+1+1+1+1`, `1+1+1+2`, `1+2+2`, and `5`. For `amount = 3` and `coins = [2]` there are `0` ways.

**Constraints, in plain words**

- The amount is between 0 and 5000.
- There are at most 300 denominations, each between 1 and 5000.
- Coins are distinct, and a denomination can be reused without limit.
- The count can be large; Python integers handle it safely.

[Coin Change II on LeetCode](https://leetcode.com/problems/coin-change-ii/)
