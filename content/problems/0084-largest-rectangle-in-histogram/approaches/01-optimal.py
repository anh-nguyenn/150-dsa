def largest_rectangle_area(heights: list[int]) -> int:
    best = 0
    stack: list[int] = []
    for index, height in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > height:
            bar_height = heights[stack.pop()]
            left = stack[-1] if stack else -1
            best = max(best, bar_height * (index - left - 1))
        stack.append(index)
    return best
