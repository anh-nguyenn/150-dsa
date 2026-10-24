Counting combinations is different from counting permutations: the order in which coins are added must not create a new answer. Dynamic programming can enforce a canonical order by deciding about one denomination at a time.

### Everyday examples

- **Making change at a till.** A cashier wants the number of distinct sets of coins that add up to a price, not the number of sequences in which those coins could be handed over.
- **Packing a bag with item types.** You have item types of fixed sizes and want the number of distinct multisets that fill a capacity exactly.
- **Choosing a meal by category.** Picking one dish from each of several categories gives a combination; listing the same dishes in a different order does not create a new meal.

### How it shows up here

Process denominations one by one and maintain a one-dimensional table of counts for every total. Because a denomination is introduced only once, in the outer loop, combinations are built in a fixed order and permutations of the same coins can never be counted twice.
