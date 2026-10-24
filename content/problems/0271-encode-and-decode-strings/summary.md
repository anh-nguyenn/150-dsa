Design a `Codec` class with two methods. `encode` takes a list of strings and returns one string. `decode` takes that string and returns the original list. Any encoding is acceptable as long as decoding recovers the exact list, including empty strings and strings that contain punctuation.

**Example**

```text
["lint", "code", "love", "you"]
-> encode -> some string -> decode -> ["lint", "code", "love", "you"]
```

**Constraints, in plain words**

- Between 0 and 200 strings.
- Each string has length 0 to 200 and may contain any character, including digits, colons, and non-ASCII text.
- The round trip must preserve order, duplicates, and empty strings.

[Encode and Decode Strings on LeetCode](https://leetcode.com/problems/encode-and-decode-strings/)
