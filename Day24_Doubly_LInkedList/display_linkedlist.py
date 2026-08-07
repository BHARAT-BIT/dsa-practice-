class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
        self.prev = None 

class LinkedList:
    def __init__(self):
        self.head = None 

    def display(self):
        current = self.head 
        while current:
            print(current.data)
            current = current.next 
        print("None")        