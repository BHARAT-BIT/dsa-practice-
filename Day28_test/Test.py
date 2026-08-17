# ============================================================
# DAY 28 TEST — Q1 (Concept): Floyd's Cycle Detection
# ============================================================
"""
Q: Why are slow and fast pointers GUARANTEED to meet if a cycle exists?
 
A: Inside the cycle, slow moves 1 step and fast moves 2 steps per round,
   so fast closes the gap to slow by exactly 1 step every round.
   Since the cycle is finite in length, fast will eventually catch up
   and overtake slow — meaning at some point they must land on the
   exact same node. It's not optional; the shrinking gap guarantees it.
"""
 
 
# ============================================================
# DAY 28 TEST — Q2 (Coding): Reverse Nodes in K-Group (LeetCode 25)
# ============================================================
"""
Reverse the list in chunks of size k. If the last chunk has fewer than
k nodes, leave it as-is (don't reverse).
 
Example: 1->2->3->4->5->6->7->8, k=3  =>  3->2->1->6->5->4->7->8
 
Key idea:
1. Look ahead k nodes from current position — if fewer than k nodes
   remain, stop (don't reverse the leftover).
2. Reverse exactly k nodes using standard iterative reversal.
3. Reconnect: previous group's tail -> new group's head,
   and move group_prev to what was the group's original head
   (which is now the tail after reversal).
"""


class ListNode:
    def __init__(self,head):
        self.head = head 


def reverse_k_group(head, k):
    dummy = ListNode(0)
    dummy.next = head
    group_prev = dummy
 
    while True:
        # check if k nodes exist from group_prev.next
        kth_node = group_prev
        count = 0
        while kth_node and count < k:
            kth_node = kth_node.next
            count += 1
 
        if not kth_node:
            break  # fewer than k nodes left — leave as-is
 
        group_next = kth_node.next   # node right after this group
 
        # reverse this group
        prev, current = group_next, group_prev.next
        while current != group_next:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
 
        # reconnect
        new_group_head = prev              # was last node, now head
        old_group_head = group_prev.next   # was head, now tail
        group_prev.next = new_group_head
        group_prev = old_group_head        # move group_prev to end of this group
 
    return dummy.next
 
 
# ============================================================
# DAY 28 TEST — Q3 (Concept): LRU Cache — HashMap + DLL
# ============================================================
"""
Q: Why do we need HashMap + Doubly Linked List together for LRU Cache?
 
A: HashMap alone gives O(1) lookup by key, but has no concept of order —
   so finding the "least recently used" item would require O(n) scanning.
 
   DLL alone maintains order (most recent at head, least recent at tail),
   but finding a SPECIFIC key's node requires O(n) traversal — no direct lookup.
 
   Combining them:
   - HashMap: key -> reference to that key's DLL node  (O(1) lookup)
   - DLL: each node has both next AND prev pointers, so once you have
     the node (via HashMap), you can remove it or move it to the head
     in O(1) — no traversal needed to find the previous node.
 
   Why DOUBLY and not SINGLY linked list?
   Removing/moving a node requires access to its PREVIOUS node
   (prev.next = current.next). In a singly linked list, finding the
   previous node requires O(n) traversal from head. In a DLL, every
   node already stores its own prev pointer — removal is O(1).
"""
 
 
# ============================================================
# DAY 28 TEST — Q4 (Coding): Intersection of Two Linked Lists (LeetCode 160)
# ============================================================
"""
Two linked lists that intersect (Y-shape) at some node. Find the
intersection point in O(1) space (no hash set).
 
Approach: get both lengths, advance the pointer of the longer list
by the length difference so both pointers are equidistant from the end,
then move both one step at a time until they meet (reference equality,
not value equality). If no intersection, both hit None simultaneously
and the loop ends naturally with None == None.
"""
 
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
 
    if lenA > lenB:
        diff = lenA - lenB
        for _ in range(diff):
            ptrA = ptrA.next
    elif lenB > lenA:
        diff = lenB - lenA
        for _ in range(diff):
            ptrB = ptrB.next
 
    while ptrA != ptrB:
        ptrA = ptrA.next
        ptrB = ptrB.next
 
    return ptrA
 
 
