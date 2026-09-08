class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, root, val):
        if root is None:
            return Node(val)

        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        return root