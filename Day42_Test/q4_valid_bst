class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def BSTvalidate(root):
    def validate(root, low, high):
        if root is None:
            return True

        if root.val <= low or root.val >= high:
            return False

        left = validate(root.left, low, root.val)
        right = validate(root.right, root.val, high)

        return left and right

    return validate(root, float("-inf"), float("inf"))