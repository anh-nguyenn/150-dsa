from collections import defaultdict, deque


def foreign_dictionary(words: list[str]) -> str:
    graph = defaultdict(set)
    indegree = {}
    for word in words:
        for ch in word:
            indegree.setdefault(ch, 0)

    for first, second in zip(words, words[1:]):
        limit = min(len(first), len(second))
        if first[:limit] == second[:limit] and len(first) > len(second):
            return ""
        for i in range(limit):
            if first[i] != second[i]:
                if second[i] not in graph[first[i]]:
                    graph[first[i]].add(second[i])
                    indegree[second[i]] += 1
                break

    queue = deque(sorted(ch for ch, count in indegree.items() if count == 0))
    order = []
    while queue:
        ch = queue.popleft()
        order.append(ch)
        for nxt in sorted(graph[ch]):
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    return "".join(order) if len(order) == len(indegree) else ""
