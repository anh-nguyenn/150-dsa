A Cartesian product combines one choice from each group. If the first group has three options and the second has three, there are nine ordered pairs, one for every way to pick an option from each group.

### Everyday examples

- **A set menu.** You choose one appetizer, one main, and one dessert. Every full meal is one combination, and the order of the courses is fixed.
- **A bicycle lock.** Each dial contributes one symbol. The code is the sequence of chosen symbols from left to right.

### How it shows up here

Each digit is a group of letters, and a result chooses exactly one letter from each digit's group. The recursion processes one digit at a time. At each position it tries every letter that the current digit maps to, appends it to the partial string, and moves to the next digit. When no digits remain, the partial string is complete.

Because the digits are processed in order, the letters in a result line up with the input digits. The number of results is the product of the group sizes, which is at most `4^n`.
