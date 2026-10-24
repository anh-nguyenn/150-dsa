A deterministic process that repeatedly applies the same rule either reaches a fixed endpoint or eventually repeats a state. Once a state repeats, the future is locked into the same loop forever. Detecting that repetition is enough to decide which outcome occurred.

### Everyday examples

- **A circular walkway.** If you keep following the same path without a map, returning to a place you have already stood means you will keep going around the same loop.
- **A thermostat stuck in a cycle.** The room keeps switching between the same two temperatures; observing the same reading twice signals that it will never settle.

### How it shows up here

The rule is the digit-square sum. Starting from the given number, apply the rule over and over. The sequence either reaches 1 or enters a cycle that never contains 1. Rather than remembering every number seen, two runners can move through the sequence at different speeds: if there is a cycle, the fast runner eventually laps the slow one. If the fast runner reaches 1 first, the number is happy.
