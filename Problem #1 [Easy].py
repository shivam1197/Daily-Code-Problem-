"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""
# This problem was recently asked by Google.
# Can you do it one pass


def find_pair_sum(numbers, k):
    encountered_numbers = set()
    print("encountered_numbers", encountered_numbers)

    for num in numbers:
        num_diff = k - num
        print("num_diff", num_diff)
        if num_diff in encountered_numbers:
            return True
        encountered_numbers.add(num)

    return False


# Example usage
numbers = [10, 15, 3, 7, 1]
k = 11

result = find_pair_sum(numbers, k)
print(result)  # Output: True
