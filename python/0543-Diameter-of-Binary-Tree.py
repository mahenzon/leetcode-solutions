# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_heights(self, node: Optional[TreeNode]):
        if not node:
            return 0

        left = self.find_heights(node.left)
        right = self.find_heights(node.right)

        self.result = max(self.result, left + right)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.find_heights(root)
        return self.result
