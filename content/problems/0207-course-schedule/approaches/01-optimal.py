from collections import deque


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph: list[list[int]] = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque(course for course in range(num_courses) if indegree[course] == 0)
    taken = 0

    while queue:
        course = queue.popleft()
        taken += 1
        for dependent in graph[course]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                queue.append(dependent)

    return taken == num_courses
