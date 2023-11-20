"""Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?"""
# This problem was asked by Uber


# def product_except_self(nums):
#     total_product = 1
#     result = []

#     # Compute the total product of all elements
#     for num in nums:
#         total_product *= num

#     # Generate the new array
#     for num in nums:
#         result.append(total_product // num)

#     return result
def product_except_self(nums):
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    result = [1] * n

    # Compute the product of all elements to the left of each element
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]

    # Compute the product of all elements to the right of each element
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]

    # Combine the left and right products to get the final product except for the element at index i
    for i in range(n):
        result[i] = left_products[i] * right_products[i]

    return result


# Example usage
nums = [1, 2, 3, 4, 5, 6]
result = product_except_self(nums)
print(result)  # Output: [120, 60, 40, 30, 24]
