#!/usr/bin/python3
"""Prime Game Implementation
    x: is the number of rounds
    nums: is an array of n
"""


def is_prime(num):
    """Checking validity of prime number
    """
    # primes = []
    if num < 2:
        return False
    if num == 2:
        return True
    if num >= 3:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
    return True

    # for i in range(2, num):
    #     if num % i == 0:
    #         return False
    # return True


def get_primes(nums):
    """Getting primes
    """
    primes = []
    for num in nums:
        if is_prime(num):
            primes.append(num)
    return primes


def multiple_primes(value, primes):
    """Getting multiple primes
    """
    multiples = []
    for num in primes:
        if value % num == 0:
            multiples.append(num)
    return multiples


def isWinner(x, nums):
    """Prime game function
    """
    maria = 0
    ben = 0

    # List to store eliminated numbers
    eliminated = []

    if len(nums) < x:
        return None

    for i in range(x):
        primes = get_primes(nums)

        if len(primes) % 2 == 0:
            ben += 1
        else:
            maria += 1

        for n in primes:
            eliminated.append(n)
            multiples = multiple_primes(n, nums)
            eliminated.extend(multiples)

        nums = [num for num in nums if num not in eliminated]

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
