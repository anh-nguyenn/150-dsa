from typing import Optional


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        tokens: list[str] = []

        def walk(node: Optional[TreeNode]) -> None:
            if node is None:
                tokens.append("null")
                return
            tokens.append(str(node.val))
            walk(node.left)
            walk(node.right)

        walk(root)
        return ",".join(tokens)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        tokens = iter(data.split(","))

        def build() -> Optional[TreeNode]:
            token = next(tokens)
            if token == "null":
                return None
            node = TreeNode(int(token))
            node.left = build()
            node.right = build()
            return node

        return build()
