from typing import Optional


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if kth is None:
                return dummy.next

        group_next = kth.next
        prev = group_next
        cur = group_prev.next
        while cur is not group_next:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        old_first = group_prev.next
        group_prev.next = kth
        group_prev = old_first
