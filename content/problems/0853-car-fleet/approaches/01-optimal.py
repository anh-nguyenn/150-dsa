def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    cars = sorted(zip(position, speed), reverse=True)
    fleets = 0
    latest_arrival = 0.0
    for start, pace in cars:
        arrival = (target - start) / pace
        if arrival > latest_arrival:
            fleets += 1
            latest_arrival = arrival
    return fleets
