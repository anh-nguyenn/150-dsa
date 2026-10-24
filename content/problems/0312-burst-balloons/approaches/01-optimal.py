def max_coins(nums: list[int]) -> int:
    values = [1] + nums + [1]
    n = len(values)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):
        for left in range(0, n - length):
            right = left + length
            for mid in range(left + 1, right):
                coins = values[left] * values[mid] * values[right]
                total = dp[left][mid] + coins + dp[mid][right]
                if total > dp[left][right]:
                    dp[left][right] = total

    return dp[0][n - 1]
