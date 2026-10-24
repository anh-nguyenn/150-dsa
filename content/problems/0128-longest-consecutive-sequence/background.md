A hash set answers exact membership questions in constant time on average. To find consecutive runs without sorting, you can use membership to decide where a run starts and then expand it one step at a time. The key trick is to begin only at values that have no predecessor.

### Everyday examples

- **Shuffled page numbers.** A stack of loose pages is out of order. If page 17 has no page 16 in the stack, it must begin a run; counting upward from there measures that run.
- **Hotel room keys.** Keys are scattered on a table. A key with no key for the room just before it starts a block of occupied rooms, and you can count how far the block continues.

### How it shows up here

Every value is placed in a set. A value whose predecessor is also present is in the middle of a run, so it can be skipped. Only true run starts trigger counting, and the longest count is the answer.
