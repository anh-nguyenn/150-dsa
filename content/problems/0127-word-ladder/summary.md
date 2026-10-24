Starting from `begin_word`, build a chain to `end_word` by changing exactly one letter at a time. Every intermediate word must appear in `word_list`. Return the number of words in the shortest chain, counting both endpoints, or `0` if no chain exists.

**Examples**

```text
begin_word = "hit", end_word = "cog",
word_list = ["hot","dot","dog","lot","log","cog"]  -> 5
```

One shortest chain is `hit -> hot -> dot -> dog -> cog`.

```text
begin_word = "hit", end_word = "cog",
word_list = ["hot","dot","dog","lot","log"]        -> 0
```

**Constraints, in plain words**

- All words have the same length, between 1 and 10 letters.
- Words use lowercase English letters only.
- Up to 5,000 words are available, all distinct.
- The start and target words are different, and the list need not contain every possible word.

[Word Ladder on LeetCode](https://leetcode.com/problems/word-ladder/)
