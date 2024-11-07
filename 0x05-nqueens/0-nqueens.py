#!/usr/bin/python3
"""Write a program that solves the N queens problem."""
import sys


def n_queens(n, board, row, result):
    """Usage: nqueens N, followed by a new line,
    and exit with the status 1"""
    if row == n:
        result.append(list(board))
        return
    for col in range(n):
        if is_valid_col(board, row, col, n):
            board[row] = col
            n_queens(n, board, row + 1, result)


def is_valid_col(board, row, col, n):
    """where N must be an integer greater or equal to 4
    If N is not an integer, print N must be a number,
    followed by a new line, and exit with the status 1
    If N is smaller than 4, print N must be at least 4,
    followed by a new line, and exit with the status 1"""
    for i in range(row):
        if board[i] == col or \
                abs(board[i] - col) == abs(i - row):
            return False
    return True


def main():
    """The N queens puzzle is the challenge of placing
    N non-attacking queens on an N×N chessboard."""
    if len(sys.argv) != 2:
        exit(1)
    if not sys.argv[1].isdigit():
        exit(1)
    n = int(sys.argv[1])
    if n < 4:
        exit(1)
    board = [-1 for i in range(n)]
    result = []
    n_queens(n, board, 0, result)
    for sol in result:
        print(sol)


if __name__ == "__main__":
    main()
