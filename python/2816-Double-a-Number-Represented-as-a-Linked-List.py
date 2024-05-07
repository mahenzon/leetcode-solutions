# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def process_previous(self, node: Optional[ListNode]) -> int:
        new_val = node.val * 2
        if node.next:
            new_val += self.process_previous(node.next)
        node.val = new_val % 10
        return new_val // 10

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if new_val := self.process_previous(head):
            head = ListNode(new_val, head)
        return head
