Each step in `cost` charges a toll when you leave it. You may begin on step `0` or step `1`, and every move climbs one or two steps. Return the smallest total toll needed to get past the final step.

**Examples**

```text
cost = [10, 15, 20]  ->  15     # start on step 1, pay 15, jump past the top
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]  ->  6
```

**Constraints, in plain words**

- Between 2 and 1,000 steps.
- Every toll is between 0 and 999.
- The top is one position beyond the last step, so reaching it means leaving the last step you stood on.

[Min Cost Climbing Stairs on LeetCode](https://leetcode.com/problems/min-cost-climbing-stairs/)
