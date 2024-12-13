#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    """
    Checks if it's safe to place a queen at (row, col) on the N x N board.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens_util(board, col, N):
    """
    solves the N-Queens problem.
    """
    if col >= N:
        return True
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            if solve_n_queens_util(board, col + 1, N):
                return True
            board[i][col] = 0
    return False

def solve_n_queens(N):
    """
    Solves the N-Queens problem and prints all solutions.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_n_queens_util(board, 0, N):
        return
    for i in range(N):
        print('[', end='')
        for j in range(N):
            if(board[i][j] == 1):
                print(f"[{i} , {j}]", end='')
                if(j < N - 1):
                    print(',', end='')
        print(']')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        sys.exit(1)
    if N < 4:
        sys.exit(1)
    solve_n_queens(N)