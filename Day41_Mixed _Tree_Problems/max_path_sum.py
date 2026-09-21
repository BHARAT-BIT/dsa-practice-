def maxPathSum(root):

    best = float("-inf")

    def max_gain(root):
        nonlocal best

        if root is None:
            return 0

        left = max_gain(root.left)
        right = max_gain(root.right)

        # Ignore negative contributions
        l = max(0, left)
        r = max(0, right)

        # Complete path through this node
        through = root.val + l + r

        # Update global best answer
        best = max(best, through)

        # Offer only one side to the parent
        return root.val + max(l, r)

    max_gain(root)

    return best





#       -10
#       /  \
#      9    20
#          /  \
#         15   7

# Node: 9, l: 0, r: 0, through: 9, return: 9, best: 9
# Node: 15, l: 0, r: 0, through: 15, return: 15, best: 15
# Node: 7, l: 0, r: 0, through: 7, return: 7, best: 15
# Node: 20, l: 15, r: 7, through: 42, return: 35, best: 42
# Node: -10, l: 9, r: 35, through: 34, return: 25, best: 42