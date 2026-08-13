def copyRandomList(head):
    if head is None:
        return None
    
    map = {None: None}
    
    # Pass 1: create all copy nodes
    current = head
    while current is not None:
        map[current] = Node(current.val)
        current = current.next
    
    # Pass 2: wire next and random pointers
    current = head
    while current is not None:
        map[current].next = map[current.next]
        map[current].random = map[current.random]
        current = current.next
    
    return map[head]