A cache keeps frequently used data close at hand, but it has limited room. When it is full, a policy decides what to discard. Least-recently-used eviction throws out the item that has gone untouched the longest, on the assumption that recent use predicts future use.

### Everyday examples

- **A small desk with limited papers.** You keep the papers you are actively using on top. When the desk is full, the paper at the bottom, untouched for the longest time, goes into a drawer.
- **Recently used apps on a phone.** The system keeps a short list of recent apps. Opening one moves it to the front; when the list is full, the oldest entry is removed.

### How it shows up here

A dictionary answers "what is the value for this key?" quickly, but dictionaries do not inherently maintain recency order. A doubly linked list does: the front is most recent and the back is least recent. Combining the two gives constant-time lookup, movement to the front, and removal from the back.
