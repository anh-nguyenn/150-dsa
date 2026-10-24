Maintain a multiset of points on the plane. `add(point)` inserts a point, and `count(point)` returns how many axis-aligned squares have that point as one corner and the other three corners already present. Duplicate points count separately.

**Example**

```text
add [3, 10], add [11, 2], add [3, 2], add [11, 2]
count [11, 10] -> 2
```

The repeated `[11, 2]` can pair with the other corners in two different ways.

**Constraints, in plain words**

- Coordinates are between 0 and 1000.
- A typical run has up to 3,000 operations.
- Points may repeat, and each stored copy can participate in a square.
- A square's sides must be parallel to the axes.

[Detect Squares on LeetCode](https://leetcode.com/problems/detect-squares/)
