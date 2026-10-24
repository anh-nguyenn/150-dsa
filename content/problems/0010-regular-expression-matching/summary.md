Given an input string and a pattern, decide whether the whole input matches the whole pattern. A dot `.` matches any single character, and a star `*` matches zero or more copies of the character immediately before it. Both the string and the pattern must be consumed completely.

**Example**

```text
s = "aab", pattern = "c*a*b"  ->  true
```

`c*` matches the empty string, `a*` matches `aa`, and `b` matches `b`.

**Constraints, in plain words**

- The input and pattern contain lowercase English letters, dots, and stars.
- Each is at most 20 characters long.
- Every star has a valid preceding character.
- Matching covers the entire input, not just a prefix.

[Regular Expression Matching on LeetCode](https://leetcode.com/problems/regular-expression-matching/)
