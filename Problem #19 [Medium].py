"""
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
"""

# This problem was asked by Facebook.


def min_cost_to_build_houses(costs):
    if not costs or len(costs) == 0:
        return 0

    n = len(costs)
    k = len(costs[0])

    if n == 1:
        return min(costs[0])

    # Initialize dp array to store minimum costs
    dp = [[0] * k for _ in range(n)]

    # Set initial costs for the first row
    for i in range(k):
        dp[0][i] = costs[0][i]

    for i in range(1, n):
        for j in range(k):
            min_cost = float('inf')
            for m in range(k):
                if m != j:
                    min_cost = min(min_cost, dp[i - 1][m])
            dp[i][j] = costs[i][j] + min_cost

    return min(dp[-1])


# Example usage:
cost_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = min_cost_to_build_houses(cost_matrix)
print("Minimum cost to build houses:", result)
