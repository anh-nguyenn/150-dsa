def max_profit(prices: list[int]) -> int:
    min_price = float("inf")
    best = 0
    for price in prices:
        best = max(best, price - min_price)
        min_price = min(min_price, price)
    return best
