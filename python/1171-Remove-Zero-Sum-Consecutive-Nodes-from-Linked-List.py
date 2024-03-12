# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        total = 0
        total_to_node = {total: dummy}
        while head:
            total += head.val
            total_to_node[total] = head
            head = head.next

        total = 0
        head = dummy

        while head:
            total += head.val
            head.next = total_to_node[total].next
            head = head.next

        return dummy.next
