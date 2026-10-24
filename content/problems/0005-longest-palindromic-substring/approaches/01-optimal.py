def longest_palindrome(s: str) -> str:
    if not s:
        return ""
    best_start = 0
    best_len = 1

    def expand(left: int, right: int) -> None:
        nonlocal best_start, best_len
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > best_len:
                best_start = left
                best_len = right - left + 1
            left -= 1
            right += 1

    for i in range(len(s)):
        expand(i, i)
        expand(i, i + 1)
    return s[best_start:best_start + best_len]
