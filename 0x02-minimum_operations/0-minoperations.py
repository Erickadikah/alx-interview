#!/usr/bin/python3
"""Using prime factorization to compute the minimum number of operations
    n: represents the number of operations
    ops: represents operations
"""


def minOperations(n):
    """checks if n is less than if it is returns 0
        keeping track of number of operation perfomed
    """
    if n < 2:
        return 0
    ops = 0
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            ops += divisor
            n /= divisor
        else:
            divisor += 1
    return ops
