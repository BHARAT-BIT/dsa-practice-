def diameter_of_tree(root):
    max_diameter = 0

    def height(node):
        nonlocal max_diameter
        if node is None:
            return 0
        left_h = height(node.left)
        right_h = height(node.right)
        max_diameter = max(max_diameter, left_h + right_h)
        return 1 + max(left_h, right_h)

    height(root)
    return max_diameter