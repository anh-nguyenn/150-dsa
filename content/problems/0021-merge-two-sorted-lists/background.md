Merging is the act of combining two ordered sequences by repeatedly taking the smallest available front item. Because both sequences are already sorted, you never need to look beyond their current fronts.

### Everyday examples

- **Two sorted piles of cards.** Flip the top card of each pile and place the lower one on a new pile. Repeat until one pile is empty, then move the rest over.
- **Two appointment queues.** Each queue is ordered by appointment time. The next person served is whichever queue's front has the earlier time.

### How it shows up here

The fronts are the heads of the two linked lists. Comparing `list1.val` with `list2.val` tells you which node should be attached next. A placeholder node in front of the result removes the awkward special case for the very first attachment, and a tail pointer keeps appending cheap.
