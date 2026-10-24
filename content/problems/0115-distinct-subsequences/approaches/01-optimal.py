def num_distinct(s: str, t: str) -> int:
    n = len(t)
    dp = [0] * (n + 1)
    dp[0] = 1

    for ch in s:
        for j in range(n, 0, -1):
            if t[j - 1] == ch:
                dp[j] += dp[j - 1]

    return dp[n]
