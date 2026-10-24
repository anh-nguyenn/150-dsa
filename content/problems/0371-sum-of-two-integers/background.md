Binary addition works column by column. At each bit position, the sum bit is the XOR of the two input bits, and a carry is generated when both bits are 1. The carry moves one position to the left, exactly like carrying in ordinary decimal addition.

A computer can perform the same steps with whole-word operations: XOR gives all sum bits without carries, AND gives the positions that generate carries, and a left shift moves those carries into place.

### Everyday examples

- **Adding columns of digits.** You write down the column total and carry the overflow into the next column.
- **Stacking boxes.** Two boxes in the same slot overflow into the next slot, while one or zero boxes stay put.

### How it shows up here

Repeat the step `sum = a ^ b` and `carry = (a & b) << 1`, then set `a = sum` and `b = carry`. When no carry remains, `a` is the answer. Python integers have unlimited width, so masking with 32 bits keeps negative numbers behaving like signed 32-bit hardware and lets the loop terminate.
