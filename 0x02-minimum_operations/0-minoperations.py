#!/usr/bin/python3
"""Minimum operations solution"""


def minOperations(n):
    """Calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    """
    if n <= 1:
        return 0

    operations = 0
    buffer = 0  # Stores the value of the last successful divisor
    file = 1  # Number of characters in the file

    for _ in range(n):
        if n % file == 0:
            buffer = file
            operations += 1
        file += buffer
        operations += 1

        if file >= n:
            break

    return operations
