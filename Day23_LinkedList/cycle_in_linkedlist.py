class Solution(object):
    def hasCycle(self, head):
        self.head = head

        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False