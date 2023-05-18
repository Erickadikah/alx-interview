def make_change(coins, total):
    result = {}

    for coin in sorted(coins, reverse=True):
        count = int(total // coin)

        if count > 0:
            result[coin] = count
            total -= count * coin

    return result



coins = [1, 2, 5, 10, 20, 50, 100, 200]
total = 537

change = make_change(coins, total)
print(change)

