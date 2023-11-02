# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self, node: Optional[TreeNode]) -> tuple[int, int]:
        if not node:
            return 0, 0  # nodes_sum, nodes_total_count

        left_sum, left_total = self.postorder(node.left)
        right_sum, right_total = self.postorder(node.right)

        total_sum = left_sum + right_sum + node.val
        total_count = left_total + right_total + 1

        average = total_sum // total_count
        if node.val == average:
            self.res += 1
        return total_sum, total_count

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.postorder(root)
        return self.res
