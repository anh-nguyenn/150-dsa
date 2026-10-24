## Hint 1

Think about prefixes. How many decodings does the first `k` digits have, and what could the final piece of such a decoding look like?

## Hint 2

The last letter comes from either the final digit alone or the final two digits together. Which values make each option legal?

## Hint 3

Let `dp[i]` count decodings of the first `i` digits. Add `dp[i-1]` when the last digit is not zero, and add `dp[i-2]` when the last two digits form a number from 10 to 26. Two rolling values are enough.
