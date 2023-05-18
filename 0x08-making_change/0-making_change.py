#!/usr/bin/python3
"""Making change Implemenation"""


def makeChange(coins: int, total: int):
    """ARGS: Coins, total
        function that determines the fewest number of coins
        needed to meet a given amount total.
    """
    counter = 0
    if total <= 0:
        return 0
    if not coins:
        return -1
    coins.sort(reverse=True)
    for coin in coins:
        if total <= 0:
            break
        while total >= coin:
            total -= coin
            counter += 1
    if total != 0:
        return -1
    return counter

    # for coin in sorted(coins, reverse=True):
    #     count =int(total // coin)
    #     if count > 0:
    #         result[coin] = count
    #         total -= count * coin
    # return result
