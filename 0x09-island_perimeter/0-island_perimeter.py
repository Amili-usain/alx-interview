#!/usr/bin/python3

"""
Module to calculate the perimeter of an island
"""


def island_perimeter(grid):
    """
    Calculates and returns the perimeter of an island
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    n = len(grid)
    for i, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            top = i == 0 or grid[i - 1][j] == 0
            right = j == m - 1 or row[j + 1] == 0
            bottom = i == n - 1 or grid[i + 1][j] == 0
            left = j == 0 or row[j - 1] == 0
            perimeter += top + right + bottom + left
    return perimeter
