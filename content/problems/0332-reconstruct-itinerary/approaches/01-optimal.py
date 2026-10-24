from collections import defaultdict
import heapq


def find_itinerary(tickets: list[list[str]]) -> list[str]:
    graph = defaultdict(list)
    for src, dst in tickets:
        heapq.heappush(graph[src], dst)

    route = []

    def visit(airport: str) -> None:
        while graph[airport]:
            visit(heapq.heappop(graph[airport]))
        route.append(airport)

    visit("JFK")
    return route[::-1]
