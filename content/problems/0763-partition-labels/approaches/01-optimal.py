def partition_labels(s: str) -> list[int]:
    last = {char: index for index, char in enumerate(s)}
    sizes = []
    start = 0
    end = 0
    for index, char in enumerate(s):
        end = max(end, last[char])
        if index == end:
            sizes.append(end - start + 1)
            start = index + 1
    return sizes
