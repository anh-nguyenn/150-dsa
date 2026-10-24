def solve_n_queens(n: int) -> list[list[str]]:
    result: list[list[str]] = []
    columns: set[int] = set()
    down_diagonals: set[int] = set()
    up_diagonals: set[int] = set()
    queen_columns: list[int] = []

    def backtrack(row: int) -> None:
        if row == n:
            result.append(
                ["." * col + "Q" + "." * (n - col - 1) for col in queen_columns]
            )
            return
        for col in range(n):
            if (
                col in columns
                or row + col in down_diagonals
                or row - col in up_diagonals
            ):
                continue
            columns.add(col)
            down_diagonals.add(row + col)
            up_diagonals.add(row - col)
            queen_columns.append(col)
            backtrack(row + 1)
            queen_columns.pop()
            up_diagonals.remove(row - col)
            down_diagonals.remove(row + col)
            columns.remove(col)

    backtrack(0)
    return result
