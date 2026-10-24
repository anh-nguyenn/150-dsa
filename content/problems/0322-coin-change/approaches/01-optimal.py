def coin_change(coins: list[int], amount: int) -> int:
    unreachable = amount + 1
    best = [0] + [unreachable] * amount
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
    return -1 if best[amount] == unreachable else best[amount]
