class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def reverse(self):
        prev = None 
        current = self.head
        next_node = None 

        while current:
            next_node = current.next 
            current.next = prev 
            prev = current 
            current = next_node
        self.head = prev        