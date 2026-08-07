def delete(self, value):
    if self.head is None:
        return
    
    if self.head.data == value:
        if self.head.next is None:      # only one node
            self.head = None
        else:                            # multi-node, deleting head
            self.head = self.head.next
            self.head.prev = None
        return
    
    current = self.head
    while current:
        if current.data == value:
            if current.next is None:     # tail case
                current.prev.next = None
            else:                        # middle case
                current.prev.next = current.next
                current.next.prev = current.prev
            return
        current = current.next