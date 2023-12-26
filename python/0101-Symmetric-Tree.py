# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check_eq(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if not (p and q):
            return False

        return (
            p.val == q.val
            and self.check_eq(p.left, q.right)
            and self.check_eq(p.right, q.left)
        )

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.check_eq(root.left, root.right)
