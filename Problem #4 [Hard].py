"""Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place."""

# This problem was asked by Stripe.


def first_missing_positive(nums):
    """
    Finds the first missing positive integer in an array of integers.

    Args:
      nums: The array of integers.

    Returns:
      The first missing positive integer.
    """

    n = len(nums)
    visited = [False] * n

    for i in range(n):
        cond1 = nums[i] > 0
        cond2 = nums[i] <= n
        cond3 = visited[nums[i] - 1]
        if nums[i] > 0 and nums[i] <= n and not visited[nums[i] - 1]:
            visited[nums[i] - 1] = True

    for i in range(n):
        if not visited[i]:
            return i + 1

    return n + 1


# Example usage:
nums = [3, 4, -1, 1]
result = first_missing_positive(nums)
print(result)  # Output: 2

nums = [1, 2, 0]
result = first_missing_positive(nums)
print(result)  # Output: 3
