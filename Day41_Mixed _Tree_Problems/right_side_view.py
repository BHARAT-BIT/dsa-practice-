from collections import deque

def rightSideView(root):
    if not root:
        return []

    q = deque([root])
    result = []

    while q:
        level_size = len(q)

        for i in range(level_size):
            node = q.popleft()

            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

    return result