#!/usr/bin/python3
"""calculates the fewest number of operations needed"""


def minOperations(n):
    """calculates the fewest number of operations
    needed to result in exactly n H characters
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        operations = 0
        i = 2
        while i * i <= n:
            while n % i == 0:
                operations += 1
                n = n // i
            i += 1
        if n > 1:
            operations += 1
        return operations
