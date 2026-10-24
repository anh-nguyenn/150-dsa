Backtracking is a way of exploring a series of choices by building an answer one step at a time. At each step you make a choice, continue deeper, and then undo the choice so you can try the next one. The undo step is what makes it possible to reuse the same working list for many branches.

### Everyday examples

- **Packing a bag.** For each item on a table you either put it in the bag or leave it out. Every complete set of decisions gives a different collection of items.
- **Choosing pizza toppings.** Each topping is a yes-or-no decision. The empty pizza is still a valid choice, and so is the pizza with every topping.

### How it shows up here

Each number in the list is an include-or-skip decision. A subset is just the list of numbers you decided to include. Because order inside a subset does not matter, the recursion only moves forward: after considering index `i`, it never goes back to an earlier index. That rule keeps `[1, 2]` and `[2, 1]` from both being produced.

Every node in the decision tree is already a valid subset, not only the leaves. That is why the current partial list is recorded before the recursive calls.
