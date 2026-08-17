class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse_from(self, node):
        prev = None
        curr = node

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def is_palindrome(self):
        # Find middle
        mid = self.middle()

        # Reverse second half
        second_half = self.reverse_from(mid)

        # Compare first half and reversed second half
        p1 = self.head
        p2 = second_half

        while p2:
            if p1.data != p2.data:
                return False

            p1 = p1.next
            p2 = p2.next

        return True


# -------------------------
# TRUE / PALINDROME LIST
# -------------------------

true_list = LinkedList()

true_list.append(1)
true_list.append(2)
true_list.append(3)
true_list.append(2)
true_list.append(1)

print("True List:", true_list.is_palindrome())


# -------------------------
# FALSE / NOT PALINDROME
# -------------------------

false_list = LinkedList()

false_list.append(1)
false_list.append(2)
false_list.append(3)
false_list.append(4)
false_list.append(5)

print("False List:", false_list.is_palindrome())