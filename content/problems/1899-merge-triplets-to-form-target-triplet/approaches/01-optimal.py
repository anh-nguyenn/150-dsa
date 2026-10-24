def merge_triplets(triplets: list[list[int]], target: list[int]) -> bool:
    found = [False, False, False]
    for a, b, c in triplets:
        if a <= target[0] and b <= target[1] and c <= target[2]:
            if a == target[0]:
                found[0] = True
            if b == target[1]:
                found[1] = True
            if c == target[2]:
                found[2] = True
    return all(found)
