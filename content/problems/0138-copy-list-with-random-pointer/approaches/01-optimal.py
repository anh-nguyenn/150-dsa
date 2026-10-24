from typing import Optional


def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    if head is None:
        return None

    copies: dict[Node, Node] = {}
    cur = head
    while cur is not None:
        copies[cur] = Node(cur.val)
        cur = cur.next

    cur = head
    while cur is not None:
        node = copies[cur]
        node.next = copies.get(cur.next)
        node.random = copies.get(cur.random)
        cur = cur.next

    return copies[head]
