## Idea

For each word, sort its letters to get a canonical key. Store words in a dictionary keyed by that canonical form, then return the dictionary's groups.

## Why it works

Sorting removes only the information that anagram equivalence ignores: the original order of letters. Words that are anagrams have identical sorted strings, so they share a key and land in the same bucket. Words that are not anagrams have different multisets of letters, so their sorted strings differ and they cannot share a bucket.

## Edge cases

- An empty string has an empty sorted key and groups with other empty strings.
- A single word forms one group by itself.
- Duplicate words belong in the same group and should both be kept.
- Words of different lengths can never be anagrams, so their keys differ.
- The output order of groups and of words within a group is arbitrary.
