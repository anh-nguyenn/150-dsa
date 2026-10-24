def max_profit(prices: list[int]) -> int:
    hold = float("-inf")
    sold = 0
    rest = 0
    for price in prices:
        prev_hold, prev_sold, prev_rest = hold, sold, rest
        hold = max(prev_hold, prev_rest - price)
        sold = prev_hold + price
        rest = max(prev_rest, prev_sold)
    return max(sold, rest)
