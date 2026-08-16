class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k):
    dummy = Node(0)
    dummy.next = head
    group_prev = dummy

    while True:
        # Step 1: check if k nodes exist from group_prev.next
        kth_node = group_prev
        count = 0
        while kth_node and count < k:
            kth_node = kth_node.next
            count += 1

        if not kth_node:
            break  # less than k nodes left, stop — don't reverse

        group_next = kth_node.next   # node right after this group

        # Step 2: reverse this group
        prev, current = group_next, group_prev.next
        while current != group_next:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        # Step 3: reconnect
        new_group_head = prev              # what was last node, now head
        old_group_head = group_prev.next   # what was head, now tail
        group_prev.next = new_group_head
        group_prev = old_group_head        # move group_prev to end of this group

    return dummy.next