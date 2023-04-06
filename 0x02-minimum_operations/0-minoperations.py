#!/usr/bin/env python3
"""Using prime factorization to compute the minimum number of operations
    n: represents the number of operations
    ops: represents operations
"""


def minOperations(n):
    """checks if n is less than if it is returns 0"""
    if n < 2:
        return 0
    """keeping track of number of operation perfomed"""
    ops = 0
    divisor = 2
    while n > 1:
        """keeps executing untill n is educed to 1 rep
            desired string legth
        """
        if n % divisor == 0:
            """checks if divisor is a factor of n
                represents a copy operation
                continues until divisor in not afactor of n
            """
            ops += divisor
            n /= divisor
        else:
            divisor += 1
    return ops
