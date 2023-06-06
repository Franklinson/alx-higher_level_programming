#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./101-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""


import sys


def solve_nqueens(N):
    def is_safe(board, row, col):
        # Check if there is any queen in the same column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check if there is any queen in the upper-left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check if there is any queen in the upper-right diagonal
        i, j = row, col
        while i >= 0 and j < N:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def backtrack(board, row):
        if row == N:
            # Found a solution, print the board
            for i in range(N):
                print(' '.join(board[i]))
            print()
        else:
            for col in range(N):
                if is_safe(board, row, col):
                    # Place a queen in the current position
                    board[row][col] = 'Q'
                    # Move to the next row
                    backtrack(board, row + 1)
                    # Remove the queen from the current position
                    board[row][col] = '.'

    # Check if N is an integer
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty board
    board = [['.' for _ in range(N)] for _ in range(N)]

    # Start the backtracking algorithm
    backtrack(board, 0)

# Check the command-line arguments


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
    solve_nqueens(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)
