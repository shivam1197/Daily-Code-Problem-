# import random

# # Set up the dice
# dice = [1, 2, 3]

# # Create a list to store the previous 1000 patterns
# previous_patterns = []

# # Roll the dice 1000 times and store the patterns
# for i in range(1000):
#     pattern = [random.choice(dice), random.choice(dice), random.choice(dice)]
#     previous_patterns.append(pattern)

# # Analyze the patterns
# count_numbers = {}
# for pattern in previous_patterns:
#     for number in pattern:
#         if number in count_numbers:
#             count_numbers[number] += 1
#         else:
#             count_numbers[number] = 1

# # Print the results
# print("Analysis of 3-number dice based on previous 1000 rolls:")
# print("Number of rolls:", len(previous_patterns))
# for number, count in count_numbers.items():
#     print(f"Number of times {number} was rolled:", count)
#     print(f"Percentage of rolls with {number}:",
#           count / len(previous_patterns) * 100, "%")

import random
from collections import Counter

rolls = []
colors = ["black", "yellow", "white"]

# Generate and save the previous 100 rolls
for _ in range(100):
    roll = random.choices(colors, weights=[0.45, 0.50, 0.05])[0]
    rolls.append(roll)

# Determine the most common roll and its count
roll_counts = Counter(rolls)
most_common_roll, most_common_count = roll_counts.most_common(1)[0]

# Find consecutive sequences of rolls
consecutive_sequences = []
current_sequence = []
for roll in rolls:
    if current_sequence and current_sequence[-1] != roll:
        consecutive_sequences.append(current_sequence)
        current_sequence = []
    current_sequence.append(roll)
consecutive_sequences.append(current_sequence)

# Find the longest consecutive sequence
longest_sequence = max(consecutive_sequences, key=len)

print(
    f"The most common roll is: {most_common_roll} (count: {most_common_count})")
print(f"The longest consecutive sequence is: {longest_sequence}")

# Predict the next roll based on the longest consecutive sequence, if available
# Default to a random roll if no consecutive sequence found
next_roll = random.choice(colors)
if len(longest_sequence) > 1:
    predicted_index = colors.index(longest_sequence[-1])
    next_roll = colors[(predicted_index + 1) % len(colors)]

print(f"The predicted next roll is: {next_roll}")
