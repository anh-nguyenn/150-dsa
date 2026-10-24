def solve(board: list[list[str]]) -> None:
    if not board or not board[0]:
        return

    rows, cols = len(board), len(board[0])

    def mark(r: int, c: int) -> None:
        stack = [(r, c)]
        board[r][c] = "S"
        while stack:
            cr, cc = stack.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    board[nr][nc] = "S"
                    stack.append((nr, nc))

    for r in range(rows):
        for c in (0, cols - 1):
            if board[r][c] == "O":
                mark(r, c)

    for c in range(cols):
        for r in (0, rows - 1):
            if board[r][c] == "O":
                mark(r, c)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "S":
                board[r][c] = "O"
