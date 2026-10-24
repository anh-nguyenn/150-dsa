Design a `WordDictionary` class that stores words and supports searching with a pattern. A dot in the pattern matches any single letter; every other character must match exactly. `addWord` stores a word, and `search` reports whether any stored word fits the pattern.

**Example**

```text
addWord("bad")
search("bad")   -> true
search(".ad")   -> true
search("b..")   -> true
```

**Constraints, in plain words**

- Stored words contain lowercase English letters.
- Search patterns contain lowercase letters and dots.
- A word or pattern has length between 1 and 25.
- At most 30,000 operations are performed.
- A dot matches exactly one character, never zero characters.

[Design Add and Search Words Data Structure on LeetCode](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
