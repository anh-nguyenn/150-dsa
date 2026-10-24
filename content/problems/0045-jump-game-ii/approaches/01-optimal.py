def jump(nums: list[int]) -> int:
    jumps = 0
    end = 0
    farthest = 0
    for index in range(len(nums) - 1):
        farthest = max(farthest, index + nums[index])
        if index == end:
            jumps += 1
            end = farthest
    return jumps
