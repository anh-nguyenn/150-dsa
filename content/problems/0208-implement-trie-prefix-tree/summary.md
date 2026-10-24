Design a `Trie` class that stores lowercase words and answers three kinds of requests: insert a word, check whether a complete word exists, and check whether any stored word starts with a given prefix.

**Example**

```text
insert("apple")
search("apple")     -> true
search("app")       -> false
startsWith("app")   -> true
```

**Constraints, in plain words**

- Words and prefixes contain lowercase English letters.
- Each word or prefix has length between 1 and 2,000.
- At most 30,000 operations are performed.
- `search` requires the exact word, while `startsWith` only requires a matching beginning.

[Implement Trie Prefix Tree on LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/)
