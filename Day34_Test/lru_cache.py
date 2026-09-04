class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):

        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head


    def add(self, node):

        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node


    def remove(self, node):

        node.prev.next = node.next
        node.next.prev = node.prev


    def get(self, key):

        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.add(node)

        return node.value


    def put(self, key, value):

        if key in self.cache:

            node = self.cache[key]

            self.remove(node)

            node.value = value

            self.add(node)

        else:

            node = Node(key, value)

            self.cache[key] = node

            self.add(node)

            if len(self.cache) > self.capacity:

                lru = self.head.next

                self.remove(lru)

                del self.cache[lru.key]