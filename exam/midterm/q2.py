# Sudoku Question

from functools import partial
from itertools import islice

sudoku_values = set(range(1, 10))


# Function recipe to return first n items of the iterable as a list
def take(n, iterable):
    return list(islice(iterable, n))


def list_to_grid(lst):
    return list(iter(partial(take, 9, iter(lst)), []))


def find_unknown_coordinates(lst):
    coordinates = []

    for row_idx, row_vals in enumerate(lst):
        for col_idx, col_val in enumerate(row_vals):
            if col_val == 0:
                coordinates.append((row_idx, col_idx))

    return coordinates


def find_missing_values_row(lst, row_idx):
    return list(sudoku_values - set(lst[row_idx]))


def find_missing_values_column(lst, col_idx):
    ret_set = []
    for row_idx in range(9):
        ret_set.append(lst[row_idx][col_idx])

    return list(sudoku_values - set(ret_set))


def find_missing_values_subgrid(lst, row_idx, col_idx):
    for i in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
        if row_idx in i:
            row = i
        if col_idx in i:
            col = i
    ret_set = []
    for x in row:
        for y in col:
            ret_set.append(lst[x][y])

    return list(sudoku_values - set(ret_set))


# NOTE: This is a very simple, bruteforce-based, incomplete, partial and slow Sudoku solver used for the purposes of the SUTD DW 2020 Mid-Term Examination
def solve_grid(lst):
    answer = list_to_grid(lst)
    coords = find_unknown_coordinates(answer)

    # Bruteforce trial method through all the missing coordinates
    for row_idx, col_idx in coords:
        possible_values = list(set(find_missing_values_subgrid(answer, row_idx, col_idx)).intersection(set(
            find_missing_values_row(answer, row_idx))).intersection(set(find_missing_values_column(answer, col_idx))))

        for poss_val in possible_values:
            answer[row_idx][col_idx] = poss_val

            # Construct column
            col_set = []
            for i in range(9):
                col_set.append(answer[i][col_idx])

            # Construct subgrid
            for j in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
                if row_idx in j:
                    row = j
                if col_idx in j:
                    col = j
            subgrid_set = []
            for x in row:
                for y in col:
                    subgrid_set.append(answer[x][y])

            # Check validity of solution
            if set(answer[row_idx]) == sudoku_values and set(col_set) == sudoku_values and set(subgrid_set) == sudoku_values:
                break

    return answer