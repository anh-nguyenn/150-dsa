Structural equality compares two trees position by position. It is not enough for both trees to contain the same values in some order; each value must sit in the same place, and missing children must match as well.

### Everyday examples

- **Two copies of a folder tree.** They match only when each folder contains the same subfolders in the same structure, not merely the same set of file names somewhere inside.
- **Two family trees.** The people and their parent-child relationships must line up at every position for the charts to be identical.

### How it shows up here

At a pair of corresponding nodes, first verify that both exist and hold the same value. Then the problem repeats on the left pair and on the right pair, which makes a direct recursive comparison natural.
