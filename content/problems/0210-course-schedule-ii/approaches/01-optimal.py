from collections import deque


def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    graph: list[list[int]] = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque(course for course in range(num_courses) if indegree[course] == 0)
    order: list[int] = []

    while queue:
        course = queue.popleft()
        order.append(course)
        for dependent in graph[course]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                queue.append(dependent)

    return order if len(order) == num_courses else []
