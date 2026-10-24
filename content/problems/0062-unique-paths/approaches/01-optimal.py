def unique_paths(m: int, n: int) -> int:
    row = [1] * n
    for _ in range(1, m):
        for col in range(1, n):
            row[col] += row[col - 1]
    return row[-1]
