"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""

# This problem was asked by Google.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None

    # Function to calculate the length of a linked list
    def get_length(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    lenA = get_length(headA)
    lenB = get_length(headB)
    diff = abs(lenA - lenB)

    # Move the pointer of the longer list by diff steps
    if lenA > lenB:
        for _ in range(diff):
            headA = headA.next
    else:
        for _ in range(diff):
            headB = headB.next

    # Traverse both lists until they intersect
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next

    return None


# Example usage:
# Create linked lists
# A: 3 -> 7 -> 8 -> 10 -> None
headA = ListNode(3)
headA.next = ListNode(7)
headA.next.next = ListNode(8)
headA.next.next.next = ListNode(10)

# B: 99 -> 1 -> 8 -> 10 -> None
headB = ListNode(99)
headB.next = ListNode(1)
# Making it intersect with A at node with value 8
headB.next.next = headA.next.next

intersect_node = getIntersectionNode(headA, headB)
if intersect_node:
    print("Intersecting node value:", intersect_node.val)
else:
    print("No intersection found")
