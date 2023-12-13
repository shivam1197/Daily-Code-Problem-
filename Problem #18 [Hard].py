"""
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
"""


from collections import deque


def max_of_subarrays(nums, k):
    if not nums or k <= 0:
        return

    deque_max = deque()

    # Process the first window of size k separately
    for i in range(k):
        # Remove elements smaller than the current element from the deque's rear
        while deque_max and nums[i] >= nums[deque_max[-1]]:
            deque_max.pop()
        deque_max.append(i)

    # Process the rest of the elements
    for i in range(k, len(nums)):
        print(nums[deque_max[0]])

        # Remove elements outside the current window from the deque's front
        while deque_max and deque_max[0] <= i - k:
            deque_max.popleft()

        # Remove elements smaller than the current element from the deque's rear
        while deque_max and nums[i] >= nums[deque_max[-1]]:
            deque_max.pop()
        deque_max.append(i)

    print(nums[deque_max[0]])  # Print the maximum of the last window


# Example usage:
# array = [10, 5, 2, 7, 8, 7]
array = [1, 1, 1, 1]

k = 2
max_of_subarrays(array, k)
