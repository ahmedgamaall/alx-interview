#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """In a text file, there is a single character H.
    Your text editor can execute only two operation
    s in this file: Copy All and Paste.
    Given a number n, write a method that
    calculates the fewest number of operation
    s needed to result
    in exactly n H characters in the file
    Returns an integer
    If n is impossible to achieve, return 0
    """
    if n <= 1:
        return 0
    else:
        for i in range(2, n + 1):
            if n % i == 0:
                return minOperations(int(n / i)) + i
