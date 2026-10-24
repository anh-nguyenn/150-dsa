def min_cost_climbing_stairs(cost: list[int]) -> int:
    two_back = 0
    one_back = 0
    for i in range(2, len(cost) + 1):
        current = min(one_back + cost[i - 1], two_back + cost[i - 2])
        two_back, one_back = one_back, current
    return one_back
