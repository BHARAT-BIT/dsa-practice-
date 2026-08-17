def cycle_start(self):
    slow = self.head
    fast = self.head

    # Step 1: Find where slow and fast meet
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None   # No cycle

    # Step 2: Move one pointer to head
    slow = self.head

    # Step 3: Move both one step at a time
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow