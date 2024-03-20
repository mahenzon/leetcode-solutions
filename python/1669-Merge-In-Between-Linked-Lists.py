# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = list1
        for _ in range(a - 1):
            head = head.next

        l2_last = list2
        while l2_last.next:
            l2_last = l2_last.next

        the_a = head
        for _ in range(b - a + 2):
            head = head.next

        the_a.next = list2
        l2_last.next = head

        return list1
