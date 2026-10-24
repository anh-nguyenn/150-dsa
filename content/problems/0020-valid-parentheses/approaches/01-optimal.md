## Idea

Scan left to right with a stack of opening brackets. A closing bracket is only legal if it matches the top opener; then that opener is removed. At the end, every opener must have found a partner.

## Why it works

Proper nesting means the most recent unmatched opener is always the one a closer must match. The stack keeps exactly those unmatched openers in the order they appeared. If a closer disagrees with the top, or arrives when the stack is empty, no later character can repair the crossing or the unmatched closer. Conversely, if every closer matches and the stack empties, the pairs are nested correctly.

## Edge cases

- A closer on an empty stack, as in `"]"` or `")("`, is invalid.
- Leftover openers, as in `"(("`, are invalid at the end.
- Adjacent independent pairs such as `"()[]{}"` are valid.
- A single character, whether opener or closer, is invalid.
- The empty string is outside the stated constraints but is handled as valid.
