# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_ancestor_diff(
        self,
        node: Optional[TreeNode],
        min_val: int,
        max_val: int,
    ) -> int:
        if not node:
            return 0
        min_val = min(min_val, node.val)
        max_val = max(max_val, node.val)
        left_ancestor_diff = self.find_ancestor_diff(node.left, min_val, max_val)
        right_ancestor_diff = self.find_ancestor_diff(node.right, min_val, max_val)
        return max(
            max_val - min_val,
            max(left_ancestor_diff, right_ancestor_diff),
        )

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.find_ancestor_diff(root, root.val, root.val)
