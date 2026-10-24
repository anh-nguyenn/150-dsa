Serialization converts an in-memory structure into a flat sequence that can be stored or sent. Deserialization reverses the process. A tree cannot be recovered from values alone because the shape matters, so the encoding must also record where children are missing. A marker for absent children supplies that information.

### Everyday examples

- **Packing a piece of furniture.** The box needs every part plus labels saying where each part belongs. A list of parts without assembly positions cannot rebuild the furniture.
- **A recipe with substitutions.** If an ingredient is missing, the recipe must say so explicitly. Leaving it out silently changes the dish, just as dropping a missing child changes a tree.

### How it shows up here

A pre-order walk writes a node's value, then encodes its left subtree, then its right subtree. Whenever the walk reaches an empty child, it writes a reserved token such as `null`. The tokens are joined with commas, so values and markers stay separate even for multi-digit numbers.

To decode, read tokens in the same order. A real value creates a node and recursively consumes its left and right encodings; a null token returns an empty child. The reserved marker is safe because the problem's values are integers, not arbitrary strings.
