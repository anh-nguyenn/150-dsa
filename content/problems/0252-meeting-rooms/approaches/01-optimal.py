def can_attend_meetings(intervals: list[list[int]]) -> bool:
    intervals = sorted(intervals)
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True
