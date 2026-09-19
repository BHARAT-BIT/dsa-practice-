def kthSmallest(root, k):
    ans = None

    def inorder(node):
        nonlocal k, ans

        if not node:
            return

        inorder(node.left)

        if ans is not None:
            return

        k -= 1

        if k == 0:
            ans = node.val
            return

        inorder(node.right)

    inorder(root)
    return ans