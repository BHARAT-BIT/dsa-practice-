def preorder_iterative(root):
    if root is None:
        return

    stack = [root]

    while stack:

        node = stack.pop()

        print(node.val)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)