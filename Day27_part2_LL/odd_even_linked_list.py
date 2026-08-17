def oddEvenList(head):
    if head is None or head.next is None:
        return head
 
    odd = head
    even = head.next
    evenHead = even          # even chain's fixed start — never moves
 
    while even and even.next:
        odd.next = even.next     # connect odd to next odd node
        odd = odd.next           # advance odd pointer
 
        even.next = odd.next     # connect even to next even node
        even = even.next         # advance even pointer
 
    odd.next = evenHead          # join odd chain's end to even chain's start
    return head
 