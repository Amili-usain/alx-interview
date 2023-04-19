#!/usr/bin/python3
"""A function to generate the Pascal's Triangle."""

def pascal_triangle(n):
    """
    Generate the Pascal's Triangle with n rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists of integers representing the Pascal's Triangle.

    Raises:
        ValueError: If n is not a positive integer.

    """

    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    pascal_triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j])
        row.append(1)
        pascal_triangle.append(row)

    return pascal_triangle
