A rotated sorted array is two increasing runs joined together. The minimum is the first value of the second run, the place where the sequence drops. Binary search can locate that drop without scanning every element, because comparing a middle value with the right end reveals which side contains it.

### Everyday examples

- **A circular tray of numbered cups.** Numbers increase around the tray, but if you start reading from an arbitrary cup, the sequence wraps once.
- **A shifted schedule.** A list of times sorted from morning to night may have been cut and reattached so that it starts in the afternoon; the earliest time is at the seam.
- **A rotated phone book.** If a sorted list of names is rotated, the alphabetically first name sits where the ordering restarts.

### How it shows up here

The rightmost value tells you whether the middle belongs to the higher run or the lower run. If the middle is at most the rightmost value, the minimum is at the middle or to its left. Otherwise the minimum lies strictly to the right. Narrowing this way reaches the seam.
