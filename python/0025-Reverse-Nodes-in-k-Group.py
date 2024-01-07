# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_to_node(self, head: Optional[ListNode], tail: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head is not tail:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return

        tail = head
        for _ in range(k):
            # check before going next
            if tail is None:
                # if we couldn't go to the k-th elem,
                # head should be used as next node
                return head
            # tail may become None and this is OK!
            tail = tail.next

        new_head = self.reverse_to_node(head, tail)
        head.next = self.reverseKGroup(tail, k)
        return new_head
