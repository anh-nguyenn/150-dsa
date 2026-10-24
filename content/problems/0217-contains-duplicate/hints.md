## Hint 1

What is different about a list with a repeat compared with a list where every value is new? Comparing every pair would answer it, but what makes that approach slow?

## Hint 2

A set only remembers whether a value has appeared. As you walk through the list, what can you conclude the moment the current value is already in that set?

## Hint 3

Build a set as you scan from left to right. Return true as soon as the current value is already present; if the scan ends without a repeat, return false.
