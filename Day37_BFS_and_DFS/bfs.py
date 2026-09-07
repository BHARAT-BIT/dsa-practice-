from collections import deque

def bfs(root):
    if root is None:
        return []

    queue = deque([root])
    result = []

    while queue:
        level = []
        
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(level)

    return result