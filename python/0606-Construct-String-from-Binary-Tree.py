# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, node: Optional[TreeNode]) -> Optional[str]:
        if not node:
            return

        self.res.append("(")
        self.res.append(str(node.val))

        if not node.left and node.right:
            self.res.append("()")

        self.preorder(node.left)
        self.preorder(node.right)

        self.res.append(")")

    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.res = []
        self.preorder(root)
        return "".join(self.res[1:-1])
