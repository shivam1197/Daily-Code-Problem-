"""
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""

# This problem was asked by Twitter.


class OrderLog:
    def __init__(self, N):
        self.N = N
        self.circular_buffer = [None] * N
        self.head = 0
        self.size = 0

    def record(self, order_id):
        self.circular_buffer[self.head] = order_id
        self.head = (self.head + 1) % self.N
        if self.size < self.N:
            self.size += 1

    def get_last(self, i):
        if i <= 0 or i > self.size:
            return None
        return self.circular_buffer[(self.head - i + self.N) % self.N]


# Example usage:
log = OrderLog(5)  # Initialize with a log size of 5
log.record(1)
log.record(2)
log.record(3)
log.record(4)
log.record(5)

# Retrieve the 2nd last element from the log (Expected: 4)
print(log.get_last(2))

# Add more orders to the log
log.record(6)
log.record(7)

# Retrieve the 3rd last element from the log (Expected: 5)
print(log.get_last(3))
