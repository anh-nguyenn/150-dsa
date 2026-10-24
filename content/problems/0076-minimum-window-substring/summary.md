Given strings `s` and `t`, return the shortest contiguous substring of `s` that contains every character of `t` at least as many times as `t` does. If no such substring exists, return an empty string.

**Example**

```text
s = "ADOBECODEBANC", t = "ABC"  ->  "BANC"
s = "a", t = "a"                ->  "a"
s = "a", t = "aa"               ->  ""
```

**Constraints, in plain words**

- `s` and `t` have between 1 and 100,000 characters.
- Characters are uppercase and lowercase English letters.
- Multiplicity matters: two `A`s in `t` require two `A`s in the window.
- The answer is unique when it exists.

[Minimum Window Substring on LeetCode](https://leetcode.com/problems/minimum-window-substring/)
