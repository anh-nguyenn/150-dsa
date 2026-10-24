When objects must be grouped into consecutive runs, the smallest remaining object is the most constrained. Nothing smaller can precede it, so it is forced to be the first item of some run. Greedily building that run and removing its cards is safe; it never creates a worse choice for the remaining cards.

### Everyday examples

- **Rummy-style card runs.** A player must lay down every card in sequences of the same length. The lowest card left cannot be played later in a run, so it must start one now.
- **Consecutive house numbers.** A courier wants to bundle flyers for houses on consecutive numbers, with the same bundle size. The lowest unassigned house has to begin a bundle, and the neighboring numbers must still be available.

### How it shows up here

Count how many copies of each value are in the hand. Sort the distinct values. For the smallest value with cards left, use as many copies as possible to start groups. Each group needs the next `group_size - 1` consecutive values to have at least that many copies. If any is short, the grouping is impossible. Otherwise subtract the copies and continue.

If the hand size is not divisible by the group size, the answer is immediately false.
