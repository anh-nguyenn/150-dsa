import heapq


def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    graph = [[] for _ in range(n + 1)]
    for u, v, w in times:
        graph[u].append((v, w))

    dist = [float("inf")] * (n + 1)
    dist[k] = 0
    heap = [(0, k)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    answer = max(dist[1:])
    return -1 if answer == float("inf") else answer
