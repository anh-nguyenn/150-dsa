from typing import Optional


def good_nodes(root: Optional[TreeNode]) -> int:
    count = 0

    def walk(node: Optional[TreeNode], highest: int) -> None:
        nonlocal count
        if node is None:
            return
        if node.val >= highest:
            count += 1
        highest = max(highest, node.val)
        walk(node.left, highest)
        walk(node.right, highest)

    if root is not None:
        walk(root, root.val)
    return count
