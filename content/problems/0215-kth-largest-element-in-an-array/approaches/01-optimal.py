import heapq


def find_kth_largest(nums: list[int], k: int) -> int:
    heap: list[int] = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
