#!/usr/bin/python3
"""
N queens problem solver
"""
import sys


def is_safe(board, row, col):
    """
    Check if placing a queen at board[row][col] is safe
    """
    # Check left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def place_queens(board, col, solutions):
    """
    Recursive helper function to place queens on the board
    """
    if col >= len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            place_queens(board, col + 1, solutions)
            board[row][col] = 0


def solve_nqueens(N):
    """
    Solve the N queens problem
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    place_queens(board, 0, solutions)
    return solutions


if __name__ == '__main__':
    # Verify command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve and print solutions
    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
