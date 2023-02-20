#!/usr/bin/python3
"""calculates the fewest number of operations needed"""


def minOperations(n):
    """calculates the fewest number of operations
    needed to result in exactly n H characters
    """
    operations = 0
    i = 2
    while i <= n + 1:
        if n % i == 0:
            operations += i
            n = n / i
            i = 2
        else:
            i += 1

    return operations
