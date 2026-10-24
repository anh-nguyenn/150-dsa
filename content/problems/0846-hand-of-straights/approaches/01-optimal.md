## Idea

Count each card value. Repeatedly take the smallest value that still has cards, and consume that many consecutive runs beginning there. If every required consecutive value has enough copies, the hand can be grouped; otherwise it cannot.

## Why it works

The smallest remaining card has no smaller neighbor available, so it cannot be anything but the first card of a run. Every copy of it must start a separate run, fixing how many runs begin there. If the following consecutive values are available in sufficient quantity, consuming them is forced and safe. If not, no other ordering can rescue that card, so the instance is impossible.

## Edge cases

- A group size of one accepts any hand, since each card forms its own group.
- A hand whose length is not divisible by the group size fails immediately.
- Duplicate values are handled by starting several runs at once.
- A gap in values makes the missing consecutive card fail the check.
- A single card works only when the group size is one.
- A group size larger than the number of cards is rejected by the divisibility check.
