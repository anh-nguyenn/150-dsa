def set_zeroes(matrix: list[list[int]]) -> None:
    rows = len(matrix)
    cols = len(matrix[0])
    first_row_zero = any(matrix[0][column] == 0 for column in range(cols))
    first_col_zero = any(matrix[row][0] == 0 for row in range(rows))

    for row in range(1, rows):
        for column in range(1, cols):
            if matrix[row][column] == 0:
                matrix[row][0] = 0
                matrix[0][column] = 0

    for row in range(1, rows):
        for column in range(1, cols):
            if matrix[row][0] == 0 or matrix[0][column] == 0:
                matrix[row][column] = 0

    if first_row_zero:
        for column in range(cols):
            matrix[0][column] = 0
    if first_col_zero:
        for row in range(rows):
            matrix[row][0] = 0
