Given points on a plane, connect all of them so that every point is reachable from every other point. The cost of a connection is the Manhattan distance between its endpoints: `|x1 - x2| + |y1 - y2|`. Return the smallest possible total cost.

**Example**

```text
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]  ->  20
```

One cheapest network uses edges of cost 4, 3, 4, and 9.

**Constraints, in plain words**

- Between 1 and 1,000 points.
- Coordinates are between -10^6 and 10^6.
- All points are distinct.
- Connections may cross; only the total distance matters.

[Min Cost to Connect All Points on LeetCode](https://leetcode.com/problems/min-cost-to-connect-all-points/)
