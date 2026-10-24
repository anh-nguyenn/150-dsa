def count_components(n: int, edges: list[list[int]]) -> int:
    parent = list(range(n))
    rank = [0] * n
    components = n

    def find(node: int) -> int:
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    for a, b in edges:
        root_a = find(a)
        root_b = find(b)
        if root_a == root_b:
            continue
        if rank[root_a] < rank[root_b]:
            root_a, root_b = root_b, root_a
        parent[root_b] = root_a
        if rank[root_a] == rank[root_b]:
            rank[root_a] += 1
        components -= 1

    return components
