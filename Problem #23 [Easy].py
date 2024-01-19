"""
You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
"""

# This problem was asked by Google.

from collections import deque


def isValid(x, y, rows, cols, board, visited):
    return 0 <= x < rows and 0 <= y < cols and not board[x][y] and (x, y) not in visited


def minStepsToReachEnd(board, start, end):
    if not board or not board[0]:
        return None

    rows, cols = len(board), len(board[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
    visited = set()

    while queue:
        x, y, steps = queue.popleft()
        visited.add((x, y))

        if (x, y) == end:
            return steps

        for dx, dy in directions:
            newX, newY = x + dx, y + dy
            if isValid(newX, newY, rows, cols, board, visited):
                queue.append((newX, newY, steps + 1))
                visited.add((newX, newY))

    return None  # End coordinate not reachable


board = [
    [False, False, False, False],
    [True, True, False, False],
    [False, False, False, False],
    [False, False, False, False]
]

start = (3, 0)  # bottom left
end = (0, 0)    # top left

min_steps = minStepsToReachEnd(board, start, end)
print("Minimum steps to reach end:", min_steps)
