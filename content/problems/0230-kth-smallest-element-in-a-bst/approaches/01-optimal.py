from typing import Optional


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    stack: list[TreeNode] = []
    node = root
    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right
    return -1
