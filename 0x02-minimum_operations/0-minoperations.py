#!/usr/bin/python3
"""
Minoperations project
"""


def minOperations(n):
    """Gets the min number of operations needed
    to result in exactly n H characters
    """
    if (n < 2):
        return 0
    operations, root = 0, 2
    while root <= n:
        if n % root == 0:
            operations += root
            n = n / root
            root -= 1
        root += 1
    return operations
