from typing import Optional


def lowest_common_ancestor(root: Optional[TreeNode], p: int, q: int) -> int:
    node = root
    while node is not None:
        if p < node.val and q < node.val:
            node = node.left
        elif p > node.val and q > node.val:
            node = node.right
        else:
            return node.val
    return -1
