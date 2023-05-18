#!/usr/bin/python3
"""Making change Implemenation"""

def makeChange(coins: int, total: int):
    """ARGS: Coins, total
        function uses high denoination count
    """
    memo = {}  # Memoization dictionary to store computed results

    def dp(amount):
        # Check if amount is in memo
        if amount in memo:
            return memo[amount]

        if amount == 0:
            return 0

        if amount < 0:
            return -1

        minCoins = float('inf')  # Initialize with infinity

        for coin in coins:
            subproblem = dp(amount - coin)
            if subproblem == -1:
                continue

            minCoins = min(minCoins, subproblem + 1)

        memo[amount] = minCoins if minCoins != float('inf') else -1
        return memo[amount]

    return dp(total)
    # counter = 0
    # if total <= 0:
    #     return 0
    # if not coins:
    #     return -1

    # for coin in sorted(coins, reverse=True):
    #     count =int(total // coin)
    #     if count > 0:
    #         result[coin] = count
    #         total -= count * coin
    # return result
