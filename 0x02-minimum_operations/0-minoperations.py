#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to get n H characters
given a text file with a single character H and two operations:
Copy All and Paste.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The fewest number of operations needed to get n H characters.
Returns 0 if n is not possible to achieve.
    """
    if n <= 1:
        return 0

    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
        if n == 1:
            break

    if not factors:
        return 0

    return sum(factors)


if __name__ == '__main__':
    n = 9
    print(minOperations(n))
