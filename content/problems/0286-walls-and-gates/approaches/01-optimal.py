from collections import deque


def walls_and_gates(rooms: list[list[int]]) -> None:
    if not rooms or not rooms[0]:
        return

    rows, cols = len(rooms), len(rooms[0])
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == 2147483647:
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))
