class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):

    inorder_map = {value: i for i, value in enumerate(inorder)}
    pre_idx = 0

    def build(left, right):

        nonlocal pre_idx

        if left > right:
            return None

        root_val = preorder[pre_idx]
        pre_idx += 1

        root = TreeNode(root_val)

        mid = inorder_map[root_val]

        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)

        return root

    return build(0, len(inorder) - 1)