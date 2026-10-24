Backtracking can enforce rules while it builds an answer, rather than generating everything and filtering afterward. If a partial answer already breaks a rule, no extension of it can repair the damage, so the entire branch can be abandoned.

### Everyday examples

- **Opening and closing a door.** You cannot close a door that was never opened. At every moment, the number of closes so far cannot exceed the number of opens.
- **Nested boxes.** Each box must be closed after it is opened, and a small box can sit inside a larger one. The nesting has to remain properly balanced at every step.

### How it shows up here

Build the string one character at a time while tracking how many opens and closes have been used. An opening parenthesis is allowed whenever fewer than `n` have been placed. A closing parenthesis is allowed only when it would not outnumber the opens. Reaching length `2n` means all pairs are used, and the string is automatically balanced.

This pruning is why the search never visits invalid prefixes. It directly generates the Catalan-number answers instead of generating all `2^(2n)` strings and testing them.
