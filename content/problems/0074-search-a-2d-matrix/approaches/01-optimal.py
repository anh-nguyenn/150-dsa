def search_matrix(matrix: list[list[int]], target: int) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])
    low, high = 0, rows * cols - 1
    while low <= high:
        middle = (low + high) // 2
        value = matrix[middle // cols][middle % cols]
        if value == target:
            return True
        if value < target:
            low = middle + 1
        else:
            high = middle - 1
    return False
