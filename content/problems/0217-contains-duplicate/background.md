A set is a collection that remembers membership rather than position. Asking a set whether a value is present takes constant time on average, and the set silently ignores a value that is already there.

### Everyday examples

- **Guest list.** A volunteer at the door marks each arriving name on a list. If the name is already marked, the same person has arrived twice.
- **Shopping checklist.** As you put items in the cart, you cross each one off. Seeing an item already crossed off means you picked it up twice.

### How it shows up here

Scan the list once and keep a set of the values seen so far. For each new value, check the set before adding it. A hit means a duplicate; a full scan with no hit means the values are all different. The set is the guest list, and the current number is the arriving name.
