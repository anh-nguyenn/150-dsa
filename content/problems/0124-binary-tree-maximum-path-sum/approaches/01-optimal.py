from typing import Optional


def max_path_sum(root: Optional[TreeNode]) -> int:
    best = float("-inf")

    def gain(node: Optional[TreeNode]) -> int:
        nonlocal best
        if node is None:
            return 0
        left = max(gain(node.left), 0)
        right = max(gain(node.right), 0)
        best = max(best, node.val + left + right)
        return node.val + max(left, right)

    if root is not None:
        gain(root)
    return best
