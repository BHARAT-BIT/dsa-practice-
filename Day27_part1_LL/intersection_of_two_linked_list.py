#Not Optimal 

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_length(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length

def get_intersection_node(headA, headB):
    lenA = get_length(headA)
    lenB = get_length(headB)

    ptrA, ptrB = headA, headB

    # Step 1: give headstart to the longer list
    if lenA > lenB:
        diff = lenA - lenB
        for _ in range(diff):
            ptrA = ptrA.next
    elif lenB > lenA:
        diff = lenB - lenA
        for _ in range(diff):
            ptrB = ptrB.next

    # Step 2: move both together, same speed
    while ptrA != ptrB:
        ptrA = ptrA.next
        ptrB = ptrB.next

    # Step 3: either both are None (no intersection)
    # or both point to the same intersection node
    return ptrA



# Optimal 

class Solution:
    def getIntersectionNode(self, headA, headB):
        
        p1 = headA
        p2 = headB
        
        while p1 != p2:
            
            if p1:
                p1 = p1.next
            else:
                p1 = headB
                
            if p2:
                p2 = p2.next
            else:
                p2 = headA
        
        return p1