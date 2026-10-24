import bisect


def length_of_lis(nums: list[int]) -> int:
    tails: list[int] = []
    for value in nums:
        position = bisect.bisect_left(tails, value)
        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value
    return len(tails)
