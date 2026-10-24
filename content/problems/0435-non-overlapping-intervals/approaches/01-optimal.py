def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0

    intervals = sorted(intervals, key=lambda interval: interval[1])
    removed = 0
    last_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start < last_end:
            removed += 1
        else:
            last_end = end

    return removed
