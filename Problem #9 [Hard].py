"""Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5

Follow-up: Can you do this in O(N) time and constant space?

"""

#This problem was asked by Airbnb.

def find_max_sum(nums):
    n = len(nums)
    
    # If the list is empty, return 0
    if n == 0:
        return 0
    
    # If the list has only one element, return the element
    if n == 1:
        return nums[0]
    
    # Initialize two variables to track the maximum sums
    prev_max_sum = 0
    curr_max_sum = 0
    
    # Iterate over the list
    for i in range(n):
        # Calculate the new maximum sum by considering the current element
        new_max_sum = max(curr_max_sum, prev_max_sum + nums[i])
        
        # Update the previous and current maximum sums
        prev_max_sum = curr_max_sum
        curr_max_sum = new_max_sum
    
    # Return the final maximum sum
    return curr_max_sum


# Test the function
nums1 = [2, 4, 6, 2, 5]
print(find_max_sum(nums1))  # Output: 13

nums2 = [5, 1, 1, 5]
print(find_max_sum(nums2))  # Output: 10
