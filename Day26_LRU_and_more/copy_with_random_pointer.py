class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copyRandomList(head):
    if head is None:
        return None

    map = {None: None}

    # Pass 1: create all copy nodes (empty pointers for now)
    current = head
    while current is not None:
        map[current] = Node(current.val)
        current = current.next

    # Pass 2: wire next and random pointers using the map
    current = head
    while current is not None:
        map[current].next = map[current.next]
        map[current].random = map[current.random]
        current = current.next

    return map[head]


# ---------- Test ----------
if __name__ == "__main__":
    # Build: A(random->C) -> B(random->A) -> C(random->None)
    A = Node(1)
    B = Node(2)
    C = Node(3)

    A.next = B
    B.next = C
    C.next = None

    A.random = C
    B.random = A
    C.random = None

    copied_head = copyRandomList(A)

    orig = A
    copy = copied_head
    while orig is not None:
        same_val = orig.val == copy.val
        different_node = orig is not copy
        random_val_match = (orig.random.val if orig.random else None) == \
                            (copy.random.val if copy.random else None)

        print(f"val={orig.val} | same_val={same_val} | different_node_obj={different_node} | random_val_match={random_val_match}")

        orig = orig.next
        copy = copy.next