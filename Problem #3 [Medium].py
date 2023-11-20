"""Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
Given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
# This problem was asked by Google.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    # Serialize the binary tree into a string representation

    if root is None:
        return "None"  # Base case: If node is None, return "None"

    # Recursively serialize the left and right subtrees
    serialized_left = serialize(root.left)
    serialized_right = serialize(root.right)

    # Concatenate the node value and the serialized subtrees with commas
    serialized_node = f"{root.val},{serialized_left},{serialized_right}"

    return serialized_node


def deserialize(data):
    # Deserialize the string representation back into a binary tree

    def helper(nodes):
        # Helper function to recursively deserialize nodes

        # Get the next node value from the iterator
        node_val = next(nodes)

        if node_val == "None":
            return None  # Base case: If node value is "None", return None

        # Create a new node with the current value
        node = Node(node_val)

        # Recursively deserialize the left and right subtrees
        node.left = helper(nodes)
        node.right = helper(nodes)

        return node

    # Split the serialized data string into individual node values
    nodes = iter(data.split(","))

    # Start the deserialization process
    return helper(nodes)


# Create a test binary tree
node = Node('root', Node('left', Node('left.left')), Node('right'))

# Serialize the binary tree
serialized_node = serialize(node)
print(serialized_node)
# Deserialize the serialized data back into a binary tree
deserialized_node = deserialize(serialized_node)
print(deserialized_node)

# Assert the value of a node in the deserialized binary tree
assert deserialized_node.left.left.val == 'left.left'

print("Test Passed!")
