A list of words is sorted according to an unknown alphabet. From the order of the words, infer the order of the letters. Return one valid ordering as a string. If the words contradict each other, return an empty string.

**Example**

```text
words = ["wrt","wrf","er","ett","rftt"]  ->  "wertf"
```

The first differing letters give `w` before `e`, `e` before `r`, `r` before `t`, and `t` before `f`.

**Constraints, in plain words**

- Between 1 and 100 words.
- Each word has between 1 and 100 lowercase letters.
- A shorter word that is a prefix of a longer one is fine, but the reverse is impossible in a sorted list.
- The answer must use every letter that appears.

[Alien Dictionary on LeetCode](https://leetcode.com/problems/alien-dictionary/)
