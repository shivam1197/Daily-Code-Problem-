"""The flight itinerary problem is as follows:

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. All flights must be used in the itinerary.

For example, given the following list of flights:

HNL ➔ AKL
YUL ➔ ORD
ORD ➔ SFO
SFO ➔ HNL
and starting airport YUL, you should return YUL ➔ ORD ➔ SFO ➔ HNL ➔ AKL. (This also happens to be the actual itinerary for the trip I'm about to take.)
"""

from collections import defaultdict


def findItinerary(flights, start):
    # Create a graph to store flights as adjacency lists
    graph = defaultdict(list)
    for origin, destination in flights:
        graph[origin].append(destination)

    # Sort the destinations in reverse order for lexical order
    for origin, destinations in graph.items():
        destinations.sort(reverse=True)

    # Initialize a stack for DFS and the result list for the itinerary
    stack = [start]
    itinerary = []

    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop())
        itinerary.append(stack.pop())

    # Reverse the itinerary to get the correct order
    return itinerary[::-1] if len(itinerary) == len(flights) + 1 else None


# Example usage:
flights = [("HNL", "AKL"), ("YUL", "ORD"), ("ORD", "SFO"), ("SFO", "HNL")]
start_airport = "YUL"
result = findItinerary(flights, start_airport)
print(result)
