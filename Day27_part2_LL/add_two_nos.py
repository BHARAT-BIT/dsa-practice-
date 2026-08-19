class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = Node()   # dummy head — result list banane ka trick
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        # Step 1: current value nikaalo, agar list khatam hai to 0 use karo
        val1 = l1.val if l1 is not None else 0
        val2 = l2.val if l2 is not None else 0

        # Step 2: sum + purani carry
        total = val1 + val2 + carry

        # Step 3: naya digit aur naya carry nikaalo
        carry = total // 10       # 10 se bada hua to carry 1, warna 0
        digit = total % 10        # ones place ka digit

        # Step 4: naya node banao result list mein
        current.next = Node(digit)
        current = current.next

        # Step 5: dono lists ko aage badhao (agar available hain)
        if l1 :
            l1 = l1.next
        if l2 :
            l2 = l2.next

    return dummy.next   # dummy khud fake tha, uska next hi asli answer hai