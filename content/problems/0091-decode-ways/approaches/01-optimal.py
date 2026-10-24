def num_decodings(s: str) -> int:
    if not s:
        return 0
    two_back = 1
    one_back = 0 if s[0] == "0" else 1
    for index in range(1, len(s)):
        current = 0
        if s[index] != "0":
            current += one_back
        pair = int(s[index - 1:index + 1])
        if 10 <= pair <= 26:
            current += two_back
        two_back, one_back = one_back, current
    return one_back
