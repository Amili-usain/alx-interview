#!/usr/bin/python3
"""A function to generate the Pascal's Triangle."""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.
    Args:
    - n (int): number of rows to generate
    Returns:
    - list of lists of integers: Pascal's triangle up to n rows,
      where each row is represented as a list of integers.

    """

    # Return an empty list if n is less than or equal to zero
    if n <= 0:
        return []

    # Initialize the triangle with the first row, which is always [1]
    triangle = [[1]]

    # Generate each subsequent row
    for i in range(1, n):
        row = [1]  # First element is always 1

        # Iterate over the indices in the previous row
        for j in range(1, i):
            prev_row = triangle[i-1]
            row.append(prev_row[j-1] + prev_row[j])  # Add adjacent elements together

        row.append(1)  # Last element is always 1
        triangle.append(row)  # Add the completed row to the triangle

    return triangle
