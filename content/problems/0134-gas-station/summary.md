There are gas stations arranged in a circle. Station `i` gives you `gas[i]` fuel, and driving from station `i` to the next one costs `cost[i]`. Starting with an empty tank, return the index of a station from which you can complete the full circuit, or `-1` if no such station exists. If a valid start exists, it is unique.

**Example**

```text
gas  = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]  ->  3
```

Starting at station 3 gives enough fuel to travel around and return to station 3.

**Constraints, in plain words**

- Both arrays have the same length, between 1 and 100,000.
- Fuel amounts and costs are non-negative.
- The tank starts empty.
- You must complete the loop in order, without running dry.
- If a solution exists, only one starting station works.

[Gas Station on LeetCode](https://leetcode.com/problems/gas-station/)
