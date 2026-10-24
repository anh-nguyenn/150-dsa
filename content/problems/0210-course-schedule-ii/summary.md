Each pair `[a, b]` says course `b` must come before course `a`. Return an ordering of all courses that respects every prerequisite, or an empty list when no such ordering exists.

**Examples**

```text
num_courses = 2, prerequisites = [[1, 0]]         -> [0, 1]
num_courses = 2, prerequisites = [[0, 1], [1, 0]] -> []
```

The order is not necessarily unique in general; any valid one is acceptable.

**Constraints, in plain words**

- Between 1 and 2,000 courses, labeled `0` through `num_courses - 1`.
- Up to 5,000 prerequisite pairs, with no pair repeated.
- Each pair names a course and one of its prerequisites.
- Return every course exactly once, or return nothing if the requirements conflict.

[Course Schedule II on LeetCode](https://leetcode.com/problems/course-schedule-ii/)
