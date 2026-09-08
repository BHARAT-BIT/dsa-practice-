def search(root, target):
    if root is None:
        return False

    if root.val == target:
        return True

    if target < root.val:
        return search(root.left, target)

    return search(root.right, target)