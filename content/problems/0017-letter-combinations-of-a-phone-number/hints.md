## Hint 1

How many letters is each digit allowed to contribute to a result? What does that imply about the length of every answer?

## Hint 2

If you have already chosen letters for the first few digits, what is the remaining task for the rest of the digits?

## Hint 3

Recurse over the digit index. At each index, loop over that digit's letters, append one, and recurse to the next index. Collect the string when the index passes the last digit.
