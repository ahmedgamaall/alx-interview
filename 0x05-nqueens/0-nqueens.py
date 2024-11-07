#!/usr/bin/python3
"""N queens puzzle"""
import sys


def isSafe(board, row, col, n):
    """nqueens N
        If the user called the program with the wrong number of arguments,
        print Usage: nqueens N, followed by a new line,
        and exit with the status 1
        where N must be an integer greater or equal to 4
        If N is not an integer, print N must be a number,
        followed by a new line, and exit with the status 1
        If N is smaller than 4, print N must be at least 4,
        followed by a new line, and exit with the status 1
        The program should print every possible solution to the problem
        One solution per line
        Format: see example
        You don’t have to print the solutions in a specific order
        You are only allowed to import the sys module
        """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
