# Two Pointers

Two Pointers replaces a nested scan with two indices that move for a reason. The indices usually start at opposite ends of a sorted array, or both start at one end with a gap between them.

Reach for it when the input is sorted, or when the answer depends on a pair whose relationship only improves in one direction. The hard part is stating the invariant: what does the current window or pair guarantee?

It assumes you can explain why moving one pointer cannot skip a better answer.
