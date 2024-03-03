# `collections` is already imported in LeetCode
import collections


class Solution:
    MIN_VAL = 0
    MAX_VAL = 10**6 + 1

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([root])
        even_lvl = True

        while q:
            prev = self.MIN_VAL if even_lvl else self.MAX_VAL

            for _ in range(len(q)):
                node = q.popleft()

                val = node.val
                if (
                    even_lvl and (not val % 2 or val <= prev)
                    or
                    not even_lvl and (val % 2 or val >= prev)
                ):
                    return False

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                prev = node.val
            even_lvl = not even_lvl

        return True
