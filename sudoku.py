# pylint: disable=missing-docstring
def sudoku_validator(grid):

    def is_valid_group(group):
        return set(group) == set(range(1, 10))

    # Satır kontrolü
    for i in range(9):  # i = satır indexi
        row = grid[i]
        if not is_valid_group(row):
            return False

    # Sütun kontrolü
    for j in range(9):  # j = sütun indexi
        column = [grid[i][j] for i in range(9)]
        if not is_valid_group(column):
            return False

    # 3x3 kare kontrolü
    for box_i in range(0, 9, 3):  # 3x3 blok satır başlangıcı
        for box_j in range(0, 9, 3):  # 3x3 blok sütun başlangıcı
            box = []
            for i in range(3):  # blok içindeki satır
                for j in range(3):  # blok içindeki sütun
                    box.append(grid[box_i + i][box_j + j])
            if not is_valid_group(box):
                return False

    return True
