You are given a list of daily stock prices. You may buy one share and later sell it, repeating as often as you like. Each share must be sold before another is bought, and after a sale you must skip the next day entirely. Return the maximum profit; doing nothing is allowed.

For `[1, 2, 3, 0, 2]` the answer is `3`: buy at `1`, sell at `2` for a profit of `1`, rest on the next day, then buy at `0` and sell at `2` for another `2`. For `[1]` the answer is `0`.

**Constraints, in plain words**

- Up to 5000 days; the official inputs contain at least one price.
- Each price is between 0 and 1000.
- After selling, the following day cannot be used to buy.

[Best Time to Buy and Sell Stock with Cooldown on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
