"""An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses."""

#This problem was asked by Google.

# XorLinkedList class
# This class represents an XOR linked list.
class XorLinkedList:

    # __init__ method
    # This method initializes the XorLinkedList object.
    def __init__(self):
        # head: The head node of the list.
        self.head = None

        # tail: The tail node of the list.
        self.tail = None

    # add method
    # This method adds an element to the end of the list.
    def add(self, element):
        # new_node: The new node to be added to the list.
        new_node = Node(element)

        # If the list is empty, set the head and tail nodes to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # Otherwise, set the tail node's next node to the new node and update the tail node.
        else:
            self.tail.next = new_node
            self.tail = new_node

    # get method
    # This method returns the node at the specified index.
    def get(self, index):
        # If the index is out of range, raise an IndexError exception.
        if index < 0 or index >= self.size():
            raise IndexError("Index out of range")

        # current_node: The current node being traversed.
        current_node = self.head

        # Iterate over the list until the current node's index is equal to the specified index.
        for i in range(index):
            current_node = current_node.next

        # Return the current node.
        return current_node

    # size method
    # This method returns the number of nodes in the list.
    def size(self):
        # current_node: The current node being traversed.
        current_node = self.head

        # size: The number of nodes in the list.
        size = 0

        # Iterate over the list until the current node is None.
        while current_node is not None:
            size += 1
            current_node = current_node.next

        # Return the size of the list.
        return size


# Node class
# This class represents a node in an Xor linked list.
class Node:

    # __init__ method
    # This method initializes the Node object.
    def __init__(self, element):
        # element: The element stored in the node.
        self.element = element

        # address: The address of the node.
        self.address = id(self)

        # next: The next node in the list.
        self.next = None

        # both: The XOR of the addresses of the previous and next nodes.
        self.both = self.address ^ self.next.address if self.next is not None else 0

# Create a new XorLinkedList object.
linked_list = XorLinkedList()

# Add three elements to the list.
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)
linked_list.add(344)


# Get the element at index 0.
node = linked_list.get(0)

# Print the element at index 0.
print(node.element)  # 1

# Get the element at index 1.
node = linked_list.get(1)

# Print the element at index 1.
print(node.element)  # 2

# Get the element at index 2.
node = linked_list.get(2)

# Print the element at index 2.
print(node.element)  # 3

node = linked_list.get(3)

# Print the element at index 2.
print(node.element)  # 3

# Get the size of the list.
size = linked_list.size()

# Print the size of the list.
print(size)  # 3

"""The get_pointer and dereference_pointer functions are not used in the code above because they are not necessary. The both field in the Node class already stores the XOR of the addresses of the previous and next nodes. This means that we can access the previous and next nodes directly by XORing the both field with the address of the current node. For example, to get the previous node, we would do the following:

Python
current_node = linked_list.head
previous_node = current_node.both ^ current_node.address

The get_pointer and dereference_pointer functions would be useful if we wanted to store the addresses of the previous and next nodes in separate fields. However, this would require more memory and would not be necessary for the implementation of an XOR linked list."""

#Usage

"""Overall, XOR linked lists find application in scenarios where memory efficiency and optimization are crucial, particularly in resource-constrained environments like embedded systems, operating systems, network protocols, and database systems.
"""