## Idea

Reject unequal lengths immediately. Otherwise keep 26 counters for the lowercase letters, incrementing for characters in `s` and decrementing for characters in `t`.

## Why it works

Each position pairs one character from `s` with one from `t`. If the strings are anagrams, those paired characters balance out across the whole alphabet, leaving every counter at zero. If any counter is nonzero, one string has a letter in a different quantity, so no rearrangement can make them equal.

## Edge cases

- Different lengths are impossible anagrams and are rejected before counting.
- Repeated letters matter: `"aacc"` and `"ccac"` have different counts and return false.
- Single-character strings are anagrams only when the characters match.
- Empty strings are anagrams, and the length check handles them cleanly.
- The 26-slot table keeps extra space constant for the stated lowercase alphabet.
