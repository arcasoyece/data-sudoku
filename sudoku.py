# pylint: disable=missing-docstring
def sudoku_validator(grid):

    def is_valid_group(group):
        return set(group) == set(range(1, 10))

    # Satır kontrolü
    for row in grid:
        if not is_valid_group(row):
            return False

    # Sütun kontrolü
    for col in range(9):
        column = [grid[row][col] for row in range(9)]
        if not is_valid_group(column):
            return False

    # 3x3 kare kontrolü
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = []
            for i in range(3):
                for j in range(3):
                    box.append(grid[box_row + i][box_col + j])
            if not is_valid_group(box):
                return False

    return True
