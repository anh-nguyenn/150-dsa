def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    total = 0
    tank = 0
    start = 0
    for index in range(len(gas)):
        surplus = gas[index] - cost[index]
        total += surplus
        tank += surplus
        if tank < 0:
            start = index + 1
            tank = 0
    return start if total >= 0 else -1
