import heapq


def swim_in_water(grid: list[list[int]]) -> int:
    n = len(grid)
    best = [[float("inf")] * n for _ in range(n)]
    best[0][0] = grid[0][0]
    heap = [(grid[0][0], 0, 0)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while heap:
        level, r, c = heapq.heappop(heap)
        if r == n - 1 and c == n - 1:
            return level
        if level > best[r][c]:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                next_level = max(level, grid[nr][nc])
                if next_level < best[nr][nc]:
                    best[nr][nc] = next_level
                    heapq.heappush(heap, (next_level, nr, nc))

    return -1
