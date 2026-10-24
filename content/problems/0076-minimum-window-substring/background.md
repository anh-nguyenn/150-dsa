A variable-size sliding window grows until a condition is met, then shrinks as much as possible while the condition still holds. This is useful when the goal is the smallest stretch that covers a requirement.

### Everyday examples

- **A shopping receipt.** You scan a long receipt looking for the shortest consecutive block that includes every item on your list, including duplicates.
- **A camera pan.** You move a frame across a scene until all landmarks are visible, then tighten the frame as much as possible without losing one.

### How it shows up here

Track how many required characters are still missing from the current window. Expand the right edge, decrementing the missing count when a needed character arrives. Once nothing is missing, the window is valid. Shrink the left edge while it stays valid, recording the shortest window each time before a needed character leaves.
