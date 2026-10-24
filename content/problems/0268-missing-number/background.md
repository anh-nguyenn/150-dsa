XOR has a cancellation property: a value XORed with itself gives 0, and XORing with 0 changes nothing. If you XOR a complete set of values together with the same set minus one element, every matched value cancels and the missing element remains.

This is useful whenever you can compare two collections that should match except for one item without sorting either one.

### Everyday examples

- **Pairing socks.** Matching pairs cancel as you compare a pile against a checklist; the sock left without a mate is the answer.
- **Two guest lists.** Comparing equal names from two lists one by one leaves only the person who appears on just one list.

### How it shows up here

The complete range is 0 through `n`, while the array has every value except one. Starting from 0, XOR every index from 0 to `n` and every array value. Every value present in both places cancels, leaving only the missing number.
