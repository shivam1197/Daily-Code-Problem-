"""Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds."""

# This problem was asked by Apple.

import time


def job_scheduler(f, n):
    # Convert milliseconds to seconds
    delay = n / 1000

    # Sleep for the specified delay
    time.sleep(delay)

    # Call the provided function
    f()

# Example function to be scheduled


def example_function():
    print("Function executed!")


# Test the job scheduler
# Call example_function after 5 seconds (5000 milliseconds)
job_scheduler(example_function, 5000)
