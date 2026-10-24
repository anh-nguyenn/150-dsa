## Hint 1

On paper, partial products are shifted by place value. Where does the digit at place `i` of one number meet the digit at place `j` of the other?

## Hint 2

Counting places from the right, a product of two digits lands around places `i + j` and `i + j + 1`. How large must the result array be?

## Hint 3

Use an array of length `m + n`. For each digit pair, add the product into the two neighboring slots and carry immediately. Remove leading zeros at the end.
