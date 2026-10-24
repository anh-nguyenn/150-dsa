def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    n = len(edges)
    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    def find(node: int) -> int:
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    for a, b in edges:
        root_a = find(a)
        root_b = find(b)
        if root_a == root_b:
            return [a, b]
        if rank[root_a] < rank[root_b]:
            root_a, root_b = root_b, root_a
        parent[root_b] = root_a
        if rank[root_a] == rank[root_b]:
            rank[root_a] += 1

    return []
