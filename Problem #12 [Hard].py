"""There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

# This problem was asked by Amazon.


def climbStairsOptimized(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    # Initialize an array to store the number of ways to climb the staircase with up to N steps
    dp = [0] * (n + 1)

    # Base cases
    dp[1] = 1
    dp[2] = 2

    # Fill the dp array using the recursive formula
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    # Return the number of ways to climb the staircase with N steps
    return dp[n]


# Example usage
n = 5
print(climbStairsOptimized(n))
