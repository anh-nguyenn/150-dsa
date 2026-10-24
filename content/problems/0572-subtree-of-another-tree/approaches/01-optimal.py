from typing import Optional


def is_subtree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    def same(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if a is None or b is None:
            return a is b
        return (
            a.val == b.val
            and same(a.left, b.left)
            and same(a.right, b.right)
        )

    if sub_root is None:
        return True
    if root is None:
        return False
    return (
        same(root, sub_root)
        or is_subtree(root.left, sub_root)
        or is_subtree(root.right, sub_root)
    )
