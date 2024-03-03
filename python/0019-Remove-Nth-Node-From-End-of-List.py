class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fw = head
        for _ in range(n):
            fw = fw.next
        if not fw:
            return head.next
        node = head
        while fw.next:
            node = node.next
            fw = fw.next
        node.next = node.next.next
        return head
