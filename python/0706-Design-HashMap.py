class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        self.max_entries = 1000
        self.entries = [ListNode() for _ in range(self.max_entries)]

    def hash(self, val):
        return val % self.max_entries

    def put(self, key: int, value: int) -> None:
        node = self.entries[self.hash(key)]
        while node and node.next:
            if node.next.key == key:
                node.next.val = value
                return
            node = node.next

        node.next = ListNode(key, value)

    def get(self, key: int) -> int:
        node = self.entries[self.hash(key)].next
        while node:
            if node.key == key:
                return node.val
            node = node.next

        return -1

    def remove(self, key: int) -> None:
        node = self.entries[self.hash(key)]
        while node and node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next
