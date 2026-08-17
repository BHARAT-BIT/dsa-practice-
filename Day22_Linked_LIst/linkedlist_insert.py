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

    def traverse(self):
        current = self.head 
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")        


    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node



