# `collections` is already imported in LeetCode
import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node: Optional[TreeNode]) -> 0:
        if not node:
            return 0

        self.counts[node.val] += 1
        odd_update = 1 if self.counts[node.val] % 2 else -1
        self.odd_count += odd_update

        if not node.left and not node.right:
            res = 1 if self.odd_count <= 1 else 0
        else:
            res = self.inorder(node.left) + self.inorder(node.right)

        self.odd_count -= odd_update
        self.counts[node.val] -= 1
        return res

    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.counts = collections.defaultdict(int)
        self.odd_count = 0

        return self.inorder(root)
