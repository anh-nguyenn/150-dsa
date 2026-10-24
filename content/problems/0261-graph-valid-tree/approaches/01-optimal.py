def valid_tree(n: int, edges: list[list[int]]) -> bool:
    if len(edges) != n - 1:
        return False

    parent = list(range(n))
    rank = [0] * n

    def find(node: int) -> int:
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    for a, b in edges:
        root_a = find(a)
        root_b = find(b)
        if root_a == root_b:
            return False
        if rank[root_a] < rank[root_b]:
            root_a, root_b = root_b, root_a
        parent[root_b] = root_a
        if rank[root_a] == rank[root_b]:
            rank[root_a] += 1

    return True
