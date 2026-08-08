class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data


# Create linked list
ll = LinkedList()

nums = [1, 2, 3, 4]

# Append all elements
for num in nums:
    ll.append(num)

# Find middle
print(ll.middle())