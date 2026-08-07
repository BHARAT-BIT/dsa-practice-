class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
        self.prev = None 

class LinkedList:
    def __init__(self):
        self.head = None 
        
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        current = self.head 

        while current.next:
            current = current.next

        current.next = new_node 
        new_node.prev = current    


