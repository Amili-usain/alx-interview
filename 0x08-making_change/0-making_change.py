#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """ Generate changes needed to reach total

    Args:
        coins (List[int]): List of coins available
        total (int): Total amount needed
    """
    if total <= 0:
        return 0

    coin_count = 0  # Number of coins used
    current_total = 0  # Current total while checking coins
    coins.sort(reverse=True)

    for coin in coins:
        while current_total < total:
            current_total += coin
            coin_count += 1

        if current_total == total:
            return coin_count

        current_total -= coin
        coin_count -= 1

    return -1
