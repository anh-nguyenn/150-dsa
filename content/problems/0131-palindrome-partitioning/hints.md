## Hint 1

At a given position, the next piece can end at any later position. Which of those pieces are actually allowed?

## Hint 2

Checking whether a substring is a palindrome splits the problem into a prefix decision and a smaller suffix problem. What is the base case?

## Hint 3

Recurse from a start index. For each possible end, keep the substring only if it reads the same both ways, then recurse from that end. Save the pieces when the start reaches the string's end.
