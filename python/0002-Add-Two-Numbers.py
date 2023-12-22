# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        extra = 0
        while l1 or l2:
            a = 0
            b = 0

            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next

            total = a + b + extra
            extra = total // 10
            # extra = total > 9
            cur.next = ListNode(total % 10)
            cur = cur.next

        if extra:
            cur.next = ListNode(extra)

        return dummy.next
