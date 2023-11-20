"""A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1"""

 #This problem was asked by Google.


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def countUnivalSubtrees(root):
    count = 0

    def isUnival(node):
        nonlocal count

        # Base case: Empty node, considered as a unival subtree
        if not node:
            return True

        # Check if the left and right subtrees are unival
        left_unival = isUnival(node.left)
        right_unival = isUnival(node.right)

        # Conditions for a subtree to be unival:
        # 1. Both left and right subtrees are unival
        # 2. If there is a left child, its value matches the current node's value
        # 3. If there is a right child, its value matches the current node's value
        if (
            left_unival and
            right_unival and
            (not node.left or node.val == node.left.val) and
            (not node.right or node.val == node.right.val)
        ):
            # Increment the count if the subtree is unival
            count += 1
            return True

        return False

    # Call the helper function to start the traversal from the root
    isUnival(root)

    # Return the count of unival subtrees
    return count


# Example tree
root = TreeNode(0)
root.left = TreeNode(1)
# root.right = TreeNode(0)
# root.right.left = TreeNode(1)
# root.right.right = TreeNode(0)
# root.right.left.left = TreeNode(1)
# root.right.left.right = TreeNode(1)

# Count unival subtrees
unival_count = countUnivalSubtrees(root)
print("Number of unival subtrees:", unival_count)
