from typing import Optional


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def valid(node: Optional[TreeNode], low: Optional[int], high: Optional[int]) -> bool:
        if node is None:
            return True
        if low is not None and node.val <= low:
            return False
        if high is not None and node.val >= high:
            return False
        return valid(node.left, low, node.val) and valid(node.right, node.val, high)

    return valid(root, None, None)
