from typing import Optional


def reorder_list(head: Optional[ListNode]) -> None:
    if head is None or head.next is None:
        return

    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None

    prev = None
    while second is not None:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt

    first = head
    second = prev
    while second is not None:
        first_next = first.next
        second_next = second.next
        first.next = second
        second.next = first_next
        first = first_next
        second = second_next
