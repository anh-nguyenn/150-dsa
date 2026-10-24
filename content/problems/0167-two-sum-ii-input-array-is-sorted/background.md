When data is sorted, two pointers can squeeze the search range from both sides. The smallest remaining value and the largest remaining value tell you which side can be discarded.

### Everyday examples

- **Meeting on a path.** Two walkers start at opposite ends. If they are too far apart, one of them moves one step inward; they never need to revisit ground they have passed.
- **Choosing two items on a price shelf.** The cheapest and most expensive items give a quick estimate. If the total is too low, the cheapest item cannot work with anything cheaper, so it is safe to look at the next cheapest.

### How it shows up here

Point one pointer at the beginning and one at the end. If their sum is too small, every partner for the left value is at most the current right value, so the left value cannot be part of the answer with any later value; move left inward. If the sum is too large, the right value is too big for every remaining left value, so move right inward. Equal sums give the pair.
