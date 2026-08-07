class SNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_two_sorted(l1, l2):
    dummy = SNode(0)
    tail = dummy
    
    p1 = l1
    p2 = l2
    
    while p1 and p2:
        if p1.data <= p2.data:
            tail.next = p1
            p1 = p1.next
        else:
            tail.next = p2
            p2 = p2.next
        tail = tail.next
    
    if p1 is None:
        tail.next = p2
    else:
        tail.next = p1
    
    return dummy.next