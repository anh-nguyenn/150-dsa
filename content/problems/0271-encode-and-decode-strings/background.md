Serialization turns a structured value into a flat stream, and framing is how the reader knows where one piece ends and the next begins. If a separator character can also appear inside the data, the separator alone is not enough; the format must also carry enough information to find the boundaries.

### Everyday examples

- **Shipping labels.** A box is labeled with its weight or dimensions so the receiver knows how much material belongs to that package, even when several packages arrive together.
- **Messages in a single file.** Each message is preceded by its length. The reader reads the number, then reads exactly that many characters, so a newline inside a message is just content.

### How it shows up here

`encode` writes each string as its length, a delimiter, and the characters themselves. `decode` reads the length, then consumes exactly that many characters. Because the length controls the read, delimiters and digits inside the original strings are harmless.
