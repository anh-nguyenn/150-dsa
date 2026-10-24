def longest_common_subsequence(text1: str, text2: str) -> int:
    if len(text1) < len(text2):
        text1, text2 = text2, text1

    prev = [0] * (len(text2) + 1)
    for ch in text1:
        cur = [0] * (len(text2) + 1)
        for j, other in enumerate(text2, start=1):
            if ch == other:
                cur[j] = prev[j - 1] + 1
            else:
                cur[j] = max(prev[j], cur[j - 1])
        prev = cur
    return prev[-1]
