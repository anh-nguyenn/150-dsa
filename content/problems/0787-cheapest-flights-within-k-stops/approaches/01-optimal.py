def find_cheapest_price(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    infinity = float("inf")
    prices = [infinity] * n
    prices[src] = 0

    for _ in range(k + 1):
        nxt = prices[:]
        for u, v, price in flights:
            if prices[u] != infinity and prices[u] + price < nxt[v]:
                nxt[v] = prices[u] + price
        prices = nxt

    return -1 if prices[dst] == infinity else prices[dst]
