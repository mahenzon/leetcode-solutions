# `deque` from `collections` is already imported in LeetCode
from collections import deque


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque(range(1, n + 1))

        while len(q) > 1:
            q.rotate(-(k - 1))
            q.popleft()

        return q.pop()
