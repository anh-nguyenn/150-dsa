The XOR operation compares two bits and outputs 1 only when they differ. Two useful consequences follow: anything XORed with itself becomes 0, and anything XORed with 0 stays unchanged. XOR is also commutative and associative, so the order in which values are combined does not matter.

### Everyday examples

- **Light switches.** Flipping the same switch twice returns it to its original position. A pair of flips has no lasting effect.
- **Canceling entries.** Two identical receipts in a ledger cancel each other out, leaving only the entry without a partner.

### How it shows up here

Each value that appears twice will cancel itself when the whole array is XORed together. The one value without a partner has nothing to cancel it, so it survives as the final result. This avoids extra memory and does not depend on sorting.
