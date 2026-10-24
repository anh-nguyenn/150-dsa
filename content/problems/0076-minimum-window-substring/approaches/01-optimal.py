from collections import Counter


def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""
    need = Counter(t)
    missing = len(t)
    left = 0
    best_start = 0
    best_len = float("inf")
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_start = left
            leaving = s[left]
            need[leaving] += 1
            if need[leaving] > 0:
                missing += 1
            left += 1
    if best_len == float("inf"):
        return ""
    return s[best_start:best_start + best_len]
