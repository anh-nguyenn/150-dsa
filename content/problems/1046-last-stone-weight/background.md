A priority queue lets a program repeatedly fetch the largest or smallest item without sorting the entire collection again. A max-heap keeps the largest item at the front, so each round of a simulation can remove the current two heaviest items quickly.

### Everyday examples

- **Merging files.** A backup tool always combines the two smallest chunks first, then puts the merged chunk back into the queue.
- **Tournament bracket.** The strongest remaining players are paired first; after a match, the winner returns to the pool with a new ranking.

### How it shows up here

The stone-smashing rule is a direct instruction to process maximum weights. A max-heap, implemented with negated values in Python, delivers the two heaviest stones in logarithmic time. The difference is pushed back when it is nonzero, and the process continues until at most one stone remains.
