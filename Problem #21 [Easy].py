"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

# This problem was asked by Snapchat.


def minMeetingRooms(intervals):
    if not intervals:
        return 0

    start_times = sorted([interval[0] for interval in intervals])
    end_times = sorted([interval[1] for interval in intervals])

    start_ptr, end_ptr = 0, 0
    rooms_needed = 0
    max_rooms = 0

    while start_ptr < len(intervals):
        if start_times[start_ptr] < end_times[end_ptr]:
            rooms_needed += 1
            max_rooms = max(max_rooms, rooms_needed)
            start_ptr += 1
        else:
            rooms_needed -= 1
            end_ptr += 1

    return max_rooms


# Example usage:
intervals = [(30, 75), (0, 50), (60, 150), (45, 75)]
result = minMeetingRooms(intervals)
print("Minimum number of rooms required:", result)
