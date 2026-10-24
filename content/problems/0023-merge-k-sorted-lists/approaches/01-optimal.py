import heapq
from typing import Optional


def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for index, node in enumerate(lists):
        if node is not None:
            heapq.heappush(heap, (node.val, index, node))

    dummy = ListNode()
    tail = dummy
    while heap:
        _, index, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next is not None:
            heapq.heappush(heap, (node.next.val, index, node.next))

    tail.next = None
    return dummy.next
