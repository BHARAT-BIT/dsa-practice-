from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    # Serialize: Tree → String
    def serialize(self, root):
        if not root:
            return ""

        queue = deque([root])
        result = []

        while queue:
            node = queue.popleft()

            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("N")

        return ",".join(result)

    # Deserialize: String → Tree
    def deserialize(self, data):
        if not data:
            return None

        values = data.split(",")

        root = TreeNode(int(values[0]))
        queue = deque([root])

        index = 1

        while queue:
            node = queue.popleft()

            # Left child
            if values[index] != "N":
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)

            index += 1

            # Right child
            if values[index] != "N":
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)

            index += 1

        return root