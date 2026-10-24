from collections import deque


def max_area_of_island(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    best = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 1:
                continue
            area = 0
            grid[r][c] = 0
            queue = deque([(r, c)])
            while queue:
                cr, cc = queue.popleft()
                area += 1
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        queue.append((nr, nc))
            best = max(best, area)

    return best
