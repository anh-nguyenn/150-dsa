Each decision has two branches, which suggests a tree of possibilities, but many branches reach the same running total. A table over totals merges those repeated states into one count.

### Everyday examples

- **Balancing a ledger.** You have entries of fixed sizes and want to know how many ways to label each entry as a debit or a credit so the final balance equals a target.
- **Splitting a team.** Divide players with fixed ratings into two sides; asking how many splits differ by a particular score is the same plus/minus counting problem.
- **Planning chores.** Mark each chore as "do now" or "defer" and count plans whose total effort matches a capacity.

### How it shows up here

The signs can be recast as choosing a subset. If `P` is the sum of the numbers given a plus sign and `N` is the sum of the magnitudes given a minus sign, then `P - N = target` and `P + N = total`. Solving gives `P = (total + target) / 2`, so the task becomes counting subsets with that positive sum.
