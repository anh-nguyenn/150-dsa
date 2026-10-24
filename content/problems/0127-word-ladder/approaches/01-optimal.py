from collections import deque, defaultdict


def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    if begin_word == end_word:
        return 1

    words = set(word_list)
    if end_word not in words:
        return 0

    length = len(begin_word)
    patterns: dict[str, list[str]] = defaultdict(list)
    for word in words:
        for i in range(length):
            patterns[word[:i] + "*" + word[i + 1:]].append(word)

    queue = deque([(begin_word, 1)])
    visited = {begin_word}

    while queue:
        word, steps = queue.popleft()
        for i in range(length):
            key = word[:i] + "*" + word[i + 1:]
            for neighbor in patterns.get(key, []):
                if neighbor == end_word:
                    return steps + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
            patterns[key] = []

    return 0
