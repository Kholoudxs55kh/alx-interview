#!/usr/bin/python3
"""
Given a number n, write a method that calculates the fewest operations number
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    returns the fewest operations number needed
    i think i solved this before
    """
    if n <= 1:
        return 0
    else:
        for i in range(2, n + 1):
            if n % i == 0:
                return minOperations(int(n / i)) + i

# n = 4
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

# n = 12
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
