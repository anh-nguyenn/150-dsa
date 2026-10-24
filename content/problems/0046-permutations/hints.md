## Hint 1

How many choices are there for the first position? After choosing one, how many remain for the second?

## Hint 2

You need to know which numbers are already in the current partial ordering. What small piece of state tracks that?

## Hint 3

Recurse position by position, marking a number used when you place it and unmarking it when you undo. When the partial ordering is full, copy it into the result.
