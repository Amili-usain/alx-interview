#!/usr/bin/python3
""" Prime Game: Determine the winner of the game based on the given inputs.
"""


def isWinner(x, nums):
    """
    Determines the winner of a game based on the given inputs.
    Args:
        x (int): The number of rounds to be played.
        nums (List[int]): A list of positive integers representing the number
                          of elements in each round.
    Returns:
        str or None: The name of the winner ('Maria' or 'Ben'), or None i
                     there is no winner.
    """

    # Check for invalid inputs
    if x < 1 or not nums:
        return None

    marias_wins, bens_wins = 0, 0

    # Generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False

    # Determine prime numbers using the Sieve of Eratosthenes algorithm
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    # Count the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    # Determine the winner based on the number of wins
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
