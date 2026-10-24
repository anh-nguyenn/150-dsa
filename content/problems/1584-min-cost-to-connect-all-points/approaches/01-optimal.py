def min_cost_connect_points(points: list[list[int]]) -> int:
    n = len(points)
    if n <= 1:
        return 0

    in_tree = [False] * n
    best = [float("inf")] * n
    best[0] = 0
    total = 0

    for _ in range(n):
        u = -1
        for i in range(n):
            if not in_tree[i] and (u == -1 or best[i] < best[u]):
                u = i

        in_tree[u] = True
        total += best[u]
        ux, uy = points[u]

        for v in range(n):
            if not in_tree[v]:
                distance = abs(ux - points[v][0]) + abs(uy - points[v][1])
                if distance < best[v]:
                    best[v] = distance

    return total
