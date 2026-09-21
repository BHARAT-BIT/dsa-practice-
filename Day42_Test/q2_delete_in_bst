def delete(root, val):

    if root is None:
        return None

    if val < root.val:
        root.left = delete(root.left, val)

    elif val > root.val:
        root.right = delete(root.right, val)

    else:
        # CASE 1: NO CHILDREN
        if root.left is None and root.right is None:
            return None

        # CASE 2: ONLY RIGHT CHILD
        if root.left is None:
            return root.right

        # CASE 2: ONLY LEFT CHILD
        if root.right is None:
            return root.left

        # CASE 3: TWO CHILDREN
        successor = root.right

        while successor.left:
            successor = successor.left

        root.val = successor.val
        root.right = delete(root.right, successor.val)

    return root