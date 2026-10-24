You are given a list of one-way airline tickets, each as `[from, to]`. Every trip begins at `"JFK"`. Use every ticket exactly once to build one continuous itinerary. When several itineraries are possible, return the one that is smallest in dictionary order.

**Example**

```text
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
-> ["JFK","MUC","LHR","SFO","SJC"]
```

**Constraints, in plain words**

- Between 1 and 300 tickets.
- Airport codes are three uppercase letters.
- A valid itinerary is guaranteed for the original problem.
- Compare itineraries airport by airport, like words in a dictionary.

[Reconstruct Itinerary on LeetCode](https://leetcode.com/problems/reconstruct-itinerary/)
