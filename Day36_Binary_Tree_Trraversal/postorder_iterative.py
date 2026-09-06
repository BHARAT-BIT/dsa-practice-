def postorder_iterative(root):
    if root is None:
        return []
    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    result.reverse()
    return result