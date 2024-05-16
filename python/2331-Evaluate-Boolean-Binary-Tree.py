# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# `operator` is already imported in LeetCode
import operator


class Solution:
    operations = {
        2: operator.or_,
        3: operator.and_,
    }

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val < 2:
            return root.val
        op = self.operations[root.val]
        return op(
            self.evaluateTree(root.left),
            self.evaluateTree(root.right),
        )
