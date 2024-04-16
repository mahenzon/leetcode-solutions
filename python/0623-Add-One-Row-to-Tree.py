# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    TOP_LEVEL = 1

    def dfs(self, node: Optional[TreeNode], val: int, depth: int) -> None:
        if not node:
            return
        if depth:
            self.dfs(node.left, val, depth - 1)
            self.dfs(node.right, val, depth - 1)
            return

        new_left = TreeNode(val=val, left=node.left)
        new_right = TreeNode(val=val, right=node.right)
        node.left = new_left
        node.right = new_right

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == self.TOP_LEVEL:
            return TreeNode(val=val, left=root)

        self.dfs(root, val, depth - (self.TOP_LEVEL + 1))
        return root
