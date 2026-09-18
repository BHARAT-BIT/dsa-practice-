class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def middle_of_list(head):


    slow = head 
    fast = head 
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next
    return slow.data
