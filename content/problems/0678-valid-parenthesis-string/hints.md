## Hint 1

A star can act as an opening parenthesis, a closing parenthesis, or nothing. What range of unmatched-open counts is possible after a prefix?

## Hint 2

An opening raises the whole range, a closing lowers it, and a star stretches it in both directions. The lower end never needs to go below zero.

## Hint 3

If the upper end ever goes negative, too many closes have accumulated. At the end, check whether zero is still inside the range by testing the lower end.
