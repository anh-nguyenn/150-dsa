A permutation has the same length and the same letter counts as the original string. Searching for one is therefore a fixed-size window problem: slide a window of that length and compare its counts.

### Everyday examples

- **A word stamp.** You have a stamp that prints the letters of a short word in any order. You want to know whether a long text has a stretch that the stamp could have produced.
- **Inventory matching.** A recipe needs a fixed multiset of ingredients. You check consecutive deliveries to see whether any delivery window contains exactly that multiset.

### How it shows up here

Build a count vector for `s1` and another for the first window of `s2` with the same length. If they match, return true. Otherwise slide the window one position: add the new character and remove the character that just left. Compare again after each slide.
