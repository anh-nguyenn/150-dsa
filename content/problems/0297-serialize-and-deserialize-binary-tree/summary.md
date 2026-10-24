Design a `Codec` class that can turn a binary tree into a string and later rebuild an identical tree from that string. There is no required string format; the only requirement is that `deserialize(serialize(root))` reproduces the original structure and values.

**Example**

```text
tree = [1, 2, 3, null, null, 4, 5]
serialize -> some string
deserialize -> [1, 2, 3, null, null, 4, 5]
```

**Constraints, in plain words**

- The tree has between 0 and 10,000 nodes.
- Node values are between -1,000 and 1,000.
- The tree may be empty, skewed, or contain negative values.
- Do not rely on global state between calls; each instance must work independently.

[Serialize and Deserialize Binary Tree on LeetCode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
