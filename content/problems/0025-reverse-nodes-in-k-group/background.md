Reversing a whole list is straightforward once you keep three pointers. Reversing selected blocks adds two concerns: deciding whether a full block exists, and reconnecting the reversed block to the parts around it without losing either end.

### Everyday examples

- **Turning around every row of exactly `k` seats.** Full rows are turned around; a short final row stays as it is.
- **Reversing batches of photos.** You flip each complete batch of `k` photos, but the last incomplete batch remains in order.

### How it shows up here

A dummy node before the head gives every group a predecessor. For each group, first walk `k` steps to confirm a full group exists. Save the node after the group, reverse the group's links so they point backward, then connect the previous group's tail to the new group head and the reversed group's tail to the saved next node.
