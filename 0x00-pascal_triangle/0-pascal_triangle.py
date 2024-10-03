#!/usr/bin/python3
"""
Pascals Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascals triangle of n
    """

    if n <= 0:
        return []

    list_of_lists = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(list_of_lists[i - 1][j - 1] + list_of_lists[i - 1][j])
        row.append(1)
        list_of_lists.append(row)
    return list_of_lists
