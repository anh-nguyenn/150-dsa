def word_break(s: str, word_dict: list[str]) -> bool:
    words = set(word_dict)
    if not s:
        return True
    max_length = max((len(word) for word in words), default=0)
    reachable = [False] * (len(s) + 1)
    reachable[0] = True
    for end in range(1, len(s) + 1):
        for length in range(1, min(max_length, end) + 1):
            start = end - length
            if reachable[start] and s[start:end] in words:
                reachable[end] = True
                break
    return reachable[len(s)]
