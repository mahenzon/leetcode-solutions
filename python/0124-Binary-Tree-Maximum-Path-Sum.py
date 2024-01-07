# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_max_path_sum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # take side's val or don't use it at all
        left_val = max(0, self.find_max_path_sum(root.left))
        right_val = max(0, self.find_max_path_sum(root.right))
        # check path for root + sides
        self.res = max(self.res, left_val + root.val + right_val)
        return root.val + max(left_val, right_val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -10**5
        self.find_max_path_sum(root)
        return self.res
