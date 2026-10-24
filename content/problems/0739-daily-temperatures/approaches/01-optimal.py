def daily_temperatures(temperatures: list[int]) -> list[int]:
    answer = [0] * len(temperatures)
    stack: list[int] = []
    for day, temperature in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temperature:
            earlier = stack.pop()
            answer[earlier] = day - earlier
        stack.append(day)
    return answer
