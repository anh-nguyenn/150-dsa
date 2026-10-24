from typing import Optional


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    best = 0

    def height(node: Optional[TreeNode]) -> int:
        nonlocal best
        if node is None:
            return 0
        left = height(node.left)
        right = height(node.right)
        best = max(best, left + right)
        return 1 + max(left, right)

    height(root)
    return best
