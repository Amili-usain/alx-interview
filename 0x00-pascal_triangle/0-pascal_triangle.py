#!/usr/bin/python3
"""A function to generate the Pascal's Triangle."""


def pascal_triangle(n):
    """returns a list of lists of numbers representing
    the pascal triangle of n."""

    pascal_triangle = []  # list to hold the complete triangle

    if n <= 0:
        return pascal_triangle   # return triangle
    for i in range(n):
        new_list = []   # list for each row i of the triangle

        for j in range(i+1):
            if j == 0 or j == i:
                new_list.append(1)
            else:
                a = pascal_triangle[i - 1][j]
                b = pascal_triangle[i - 1][j - 1]
                new_list.append(a + b)
        pascal_triangle.append(new_list)

    return pascal_triangle     # print(triangle)
