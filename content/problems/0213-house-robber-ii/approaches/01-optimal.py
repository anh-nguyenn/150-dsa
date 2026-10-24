def rob(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    def rob_line(lo: int, hi: int) -> int:
        two_back = 0
        one_back = 0
        for i in range(lo, hi):
            two_back, one_back = one_back, max(one_back, two_back + nums[i])
        return one_back

    return max(rob_line(0, len(nums) - 1), rob_line(1, len(nums)))
