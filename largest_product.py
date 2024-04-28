"""Entry point script to test the solution of finding the
greatest product of four adjacent numbers in the same direction."""

import grids_to_test as grid


def diagonal_max_product(grid, max_product, rows, columns):
    """This function checks and finds out the greatest
    product in our grid's diagonals, from top left to
    bottom right, and from bottom left to top right."""

    for i in range(rows - 3):
        for j in range(columns - 3):

            tl_br_d1_product = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
            max_product = max(max_product, tl_br_d1_product)

            bl_tr_d2_product = grid[i + 3][j] * grid[i + 2][j + 1] * grid[i + 1][j + 2] * grid[i][j + 3]
            max_product = max(max_product, bl_tr_d2_product)

    return max_product


def horizontal_vertical_max_product(grid, rows, columns):
    """This function checks and finds out the greatest
    product in our grid's horizontal and vertical axis (rows
    and columns)."""

    max_product = 0

    for i in range(rows):
        for j in range(columns - 3):

            horizontal_product = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
            max_product = max(max_product, horizontal_product)

            vertical_product = grid[j][i] * grid[j + 1][i] * grid[j + 2][i] * grid[j + 3][i]
            max_product = max(max_product, vertical_product)

    return max_product


def max_product_in_grid(grid):
    """This function is responsible for calling the
    horizontal_vertical_max_product() and diagonal_max_product()
    functions, to respectively calculate the greatest product
    in our grid via its horizontal and vertical axis, and its
    diagonals.
    """

    rows = len(grid)

    if rows == 0:
        return 0

    columns = len(grid[0])

    if not rows == columns:
        return 0

    max_product = horizontal_vertical_max_product(
        grid=grid,
        rows=rows,
        columns=columns
    )

    max_product = diagonal_max_product(
        grid=grid,
        max_product=max_product,
        rows=rows,
        columns=columns
    )

    return max_product


if __name__ == "__main__":
    greatest_product = max_product_in_grid(grid=grid.twenty_by_twenty)
    print("Greatest product is:", greatest_product)  # 70600674

    greatest_product = max_product_in_grid(grid=grid.five_by_five)
    print("Greatest product is:", greatest_product)  # 1523200

    greatest_product = max_product_in_grid(grid=grid.zero_by_zero)
    print("Greatest product is:", greatest_product) # 0

    greatest_product = max_product_in_grid(grid=grid.five_by_three)
    print("Greatest product is:", greatest_product) # 0
