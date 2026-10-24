Adding multi-digit numbers by hand starts at the ones column and moves left, carrying any overflow into the next column. Linked lists in this problem store the ones digit at the head, which matches that direction of travel perfectly.

### Everyday examples

- **Adding two receipt totals.** You add the cents column first, carry into dollars, then add the dollars.
- **An odometer rolling over.** After `...999` comes `...000` with a carry into the next position; the extra digit may create a new column.

### How it shows up here

Each list head is the ones digit, so walking both lists forward is the same as moving from right to left through the numbers. At each step, add the two digits plus any carry, append the ones digit of that total, and pass the tens digit along. A list may run out before the other, and a final carry may require an extra node.
