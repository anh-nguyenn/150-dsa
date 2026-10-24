# Stack

A stack stores the most recent thing first. That makes it the natural structure for nesting, for matching open and close tokens, and for maintaining a monotonic sequence of unresolved candidates.

Reach for it when the next element invalidates or resolves a suffix of previous elements, or when the problem has a natural undo order. A monotonic stack is just a stack with a rule about what may remain on it.

It assumes you can say what each stack entry represents and when it is popped.
