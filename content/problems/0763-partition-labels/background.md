A part can end only after the last occurrence of every letter inside it. If a letter seen earlier shows up again later, the current part has to stretch forward to include that occurrence, and the new range may bring in more letters that also need stretching. This is an interval-closing process: each letter defines an interval from its first to its last occurrence, and parts are the connected clusters of overlapping intervals.

### Everyday examples

- **Project scheduling.** Each project has work on several scattered days. If all work for a project must stay in one uninterrupted block, a block started for one project may need to absorb other projects whose days fall inside it.
- **Book chapters.** A recurring character may appear throughout several chapters. To keep all of a character's scenes in one chapter, chapter boundaries must wait until that character's final scene.

### How it shows up here

Record the last index of every letter. Sweep the string with a current part starting at `start` and a boundary `end`. At each index, extend `end` to the letter's last occurrence if that is farther right. When the sweep reaches `end`, every letter in the current part has had its final appearance, so the part can close. Record its length and start a new part at the next index.

Closing as soon as possible maximizes the number of parts.
