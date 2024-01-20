"""
Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

is_locked, which returns whether the node is locked
lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.
"""

# This problem was asked by Google.


class TreeNode:
    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None
        self.is_locked = False
        self.locked_descendants_count = 0  # Count of locked descendants

    def is_locked(self):
        return self.is_locked

    def can_lock_or_unlock(self):
        # Check if any descendants are locked
        if self.locked_descendants_count > 0:
            return False

        # Check if any ancestors are locked
        current = self.parent
        while current:
            if current.is_locked:
                return False
            current = current.parent

        return True

    def lock(self):
        if self.can_lock_or_unlock():
            # Lock the node and update locked descendants count for ancestors
            self.is_locked = True
            current = self.parent
            while current:
                current.locked_descendants_count += 1
                current = current.parent
            return True
        else:
            return False

    def unlock(self):
        if self.can_lock_or_unlock():
            # Unlock the node and update locked descendants count for ancestors
            self.is_locked = False
            current = self.parent
            while current:
                current.locked_descendants_count -= 1
                current = current.parent
            return True
        else:
            return False


# Driver code
# Construct a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2, parent=root)
root.right = TreeNode(3, parent=root)
root.left.left = TreeNode(4, parent=root.left)
root.left.right = TreeNode(5, parent=root.left)

# Locking and unlocking operations
print(root.lock())      # Lock root (should return True)
print(root.is_locked)    # Check if root is locked (should return True)
print(root.unlock())    # Unlock root (should return True)
print(root.is_locked)    # Check if root is locked (should return False)
