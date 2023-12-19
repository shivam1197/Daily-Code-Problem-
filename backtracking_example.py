"""
The N queens puzzle
The N queens puzzle is the classic backtracking problem. The question is this:

You have an N by N board. Write a function that returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other,
i.e. no two queens share the same row, column, or diagonal.
"""


def is_safe(board, row, col):
    # Check if there is a queen in the same column up to the current row
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, row):
    count = 0
    n = len(board)

    if row == n:
        return 1

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            count += solve_n_queens_util(board, row + 1)
            board[row][col] = 0  # Backtrack

    return count


def total_n_queens(n):
    board = [[0] * n for _ in range(n)]
    return solve_n_queens_util(board, 0)


# Example usage:
n = 10
print(f"Number of possible arrangements for {n} queens: {total_n_queens(n)}")
