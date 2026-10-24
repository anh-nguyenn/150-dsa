def check_inclusion(s1: str, s2: str) -> bool:
    n, m = len(s1), len(s2)
    if n > m:
        return False
    need = [0] * 26
    window = [0] * 26
    for ch in s1:
        need[ord(ch) - ord("a")] += 1
    for i, ch in enumerate(s2):
        window[ord(ch) - ord("a")] += 1
        if i >= n:
            window[ord(s2[i - n]) - ord("a")] -= 1
        if window == need:
            return True
    return False
