This is a subset-sum problem, a close relative of the 0/1 knapsack. The question is not which elements to pick, but whether some subset hits exactly half of the total.

### Everyday examples

- **Splitting a bill.** Two people want to pay the same amount, and each charge must be assigned whole to one person.
- **Balancing two bags.** Packing items of fixed weights so both bags weigh the same is the same reachability question.
- **Dividing chores.** Assigning whole tasks of known effort to two people so their loads match asks for a subset with half the total effort.

### How it shows up here

If the total is odd, equal halves are impossible. Otherwise the target is half the total, and the task becomes: can some subset sum to the target? Sweep the numbers while tracking which sums are reachable, updating from high to low so each number is used at most once.
