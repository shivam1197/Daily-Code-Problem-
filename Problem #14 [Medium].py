"""The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

# This problem was asked by Google.

import random


def estimate_pi(num_points):
    points_inside_circle = 0
    total_points = num_points

    for _ in range(num_points):
        # Generate random coordinates within the square (-1,1) x (-1,1)
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Check if the point falls within the quarter circle
        if x**2 + y**2 <= 1:
            points_inside_circle += 1

    # Estimate π using the ratio of points inside the quarter circle to total points
    estimated_pi = 4 * points_inside_circle / total_points
    return estimated_pi


# Number of random points to generate
num_points = 1000000  # You can adjust this for better accuracy

# Estimate π using Monte Carlo simulation
estimated_pi = estimate_pi(num_points)
print(f"Estimated value of π using {num_points} points: {estimated_pi:.3f}")
