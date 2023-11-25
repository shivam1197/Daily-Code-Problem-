"""Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

"""

# This problem was asked by Facebook.
import random


def select_random_element(stream):
    result = None
    count = 0

    for element in stream:
        count += 1
        # With probability 1/count, update the result
        if random.randint(1, count) == 1:
            result = element

    return result


# Example usage
stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
selected_element = select_random_element(stream)
print(f"The selected random element from the stream is: {selected_element}")
