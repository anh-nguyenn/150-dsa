Each pair `[a, b]` means course `b` must be completed before course `a`. Given the number of courses and all such pairs, decide whether it is possible to finish every course.

**Examples**

```text
num_courses = 2, prerequisites = [[1, 0]]          -> true
num_courses = 2, prerequisites = [[1, 0], [0, 1]]  -> false
```

**Constraints, in plain words**

- Between 1 and 2,000 courses, labeled `0` through `num_courses - 1`.
- Up to 5,000 dependency pairs, with no pair repeated.
- A pair names a course and one prerequisite of that course.
- A course may have several prerequisites, and some courses may have none.

[Course Schedule on LeetCode](https://leetcode.com/problems/course-schedule/)
