# Tries

A trie stores words by their prefixes. Each edge is a character, and each node represents the prefix spelled so far. Lookup costs the length of the word, independent of how many words are stored.

Reach for it when many words share prefixes, when you need wildcard search, or when a grid search needs to know quickly whether a partial path can still become a word.

It assumes you can distinguish "this prefix exists" from "this prefix is a complete word".
