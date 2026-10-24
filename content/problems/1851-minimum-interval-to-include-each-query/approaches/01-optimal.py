import heapq


def min_interval(intervals: list[list[int]], queries: list[int]) -> list[int]:
    ordered_intervals = sorted(intervals)
    indexed_queries = sorted((value, index) for index, value in enumerate(queries))
    result = [-1] * len(queries)
    heap = []
    j = 0

    for value, index in indexed_queries:
        while j < len(ordered_intervals) and ordered_intervals[j][0] <= value:
            start, end = ordered_intervals[j]
            heapq.heappush(heap, (end - start + 1, end))
            j += 1

        while heap and heap[0][1] < value:
            heapq.heappop(heap)

        if heap:
            result[index] = heap[0][0]

    return result
