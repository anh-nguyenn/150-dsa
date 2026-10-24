A prefix product accumulates everything before a position, and a suffix product accumulates everything after it. The product excluding one position is simply the prefix ending just before it multiplied by the suffix starting just after it.

### Everyday examples

- **Bill without one item.** If you know the total cost of everything before an item and everything after it, the total without that item is the product of those two parts.
- **Discount factors.** A sequence of multipliers applies to a purchase. To ask what the result would be without one stage, combine all the stages before it and all the stages after it.

### How it shows up here

A forward pass stores the product of everything to the left of each index directly in the output. A backward pass maintains the product of everything to the right and multiplies it into the same slots. The output array is reused, so no extra array is required.
