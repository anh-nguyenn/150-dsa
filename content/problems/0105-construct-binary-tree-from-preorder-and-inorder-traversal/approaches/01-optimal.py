from typing import Optional


def build_tree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    position = {value: index for index, value in enumerate(inorder)}

    def build(pre_start: int, pre_end: int, in_start: int, in_end: int) -> Optional[TreeNode]:
        if pre_start > pre_end:
            return None
        root_value = preorder[pre_start]
        root = TreeNode(root_value)
        split = position[root_value]
        left_size = split - in_start
        root.left = build(pre_start + 1, pre_start + left_size, in_start, split - 1)
        root.right = build(pre_start + left_size + 1, pre_end, split + 1, in_end)
        return root

    return build(0, len(preorder) - 1, 0, len(inorder) - 1)
