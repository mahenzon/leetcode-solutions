# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_leafs(self, root: Optional[TreeNode], leafs: list[TreeNode]) -> None:
        if not root:
            return
        if not root.left and not root.right:
            leafs.append(root.val)
            return

        self.find_leafs(root.left, leafs)
        self.find_leafs(root.right, leafs)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs1 = []
        leafs2 = []
        self.find_leafs(root1, leafs1)
        self.find_leafs(root2, leafs2)
        return leafs1 == leafs2
