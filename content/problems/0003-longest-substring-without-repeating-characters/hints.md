## Hint 1

Imagine a window that must contain only distinct characters. What should happen when the new character is already inside?

## Hint 2

You do not need to move the left edge one step at a time; where is the earliest place the window can restart?

## Hint 3

Remember the last position of each character. When a repeat falls inside the current window, jump the left edge just past that position, then update the answer.
