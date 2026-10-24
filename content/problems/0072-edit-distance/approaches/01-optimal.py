def min_distance(word1: str, word2: str) -> int:
    if len(word1) < len(word2):
        word1, word2 = word2, word1

    width = len(word2)
    previous = list(range(width + 1))

    for i, ch1 in enumerate(word1, start=1):
        current = [i] + [0] * width
        for j, ch2 in enumerate(word2, start=1):
            if ch1 == ch2:
                current[j] = previous[j - 1]
            else:
                current[j] = 1 + min(previous[j], current[j - 1], previous[j - 1])
        previous = current

    return previous[width]
