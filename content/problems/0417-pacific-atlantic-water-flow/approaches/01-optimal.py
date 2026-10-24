def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    if not heights or not heights[0]:
        return []

    rows, cols = len(heights), len(heights[0])

    def reachable(starts: list[tuple[int, int]]) -> set[tuple[int, int]]:
        seen = set(starts)
        stack = list(starts)
        while stack:
            r, c = stack.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in seen
                    and heights[nr][nc] >= heights[r][c]
                ):
                    seen.add((nr, nc))
                    stack.append((nr, nc))
        return seen

    pacific = reachable(
        [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
    )
    atlantic = reachable(
        [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]
    )

    return [[r, c] for r, c in sorted(pacific & atlantic)]
