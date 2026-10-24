Backtracking handles problems where you make a sequence of choices and need to collect every sequence that meets a condition. A useful refinement is pruning: if a choice cannot possibly lead to a solution, skip that whole branch instead of exploring it.

### Everyday examples

- **Making exact change.** You have coin denominations and want every way to total a price. Using the same coin twice is allowed, but the order in which you list the coins does not create a different way.
- **Filling a crate.** You pack items of various sizes until the crate is exactly full. Once an item is too large for the remaining space, there is no reason to keep trying it.

### How it shows up here

Sorting the candidates makes pruning easy. During the search you track how much of the target is still needed. If the next candidate is larger than that remainder, every later candidate is also too large, so the loop can stop. Because a value can be reused, the recursive call keeps the same index available; it does not advance to the next candidate.

The current combination is stored in non-decreasing order because candidates are considered from left to right. That convention prevents the same combination from appearing in a different order.
