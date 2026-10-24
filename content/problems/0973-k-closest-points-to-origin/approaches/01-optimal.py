import heapq


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    heap: list[tuple[int, int, int]] = []
    for x, y in points:
        distance = x * x + y * y
        heapq.heappush(heap, (-distance, x, y))
        if len(heap) > k:
            heapq.heappop(heap)
    return [[x, y] for _, x, y in heap]
