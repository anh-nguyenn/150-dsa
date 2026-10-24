from collections import deque
from typing import Optional


def right_side_view(root: Optional[TreeNode]) -> list[int]:
    if root is None:
        return []
    visible: list[int] = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for position in range(level_size):
            node = queue.popleft()
            if position == level_size - 1:
                visible.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    return visible
