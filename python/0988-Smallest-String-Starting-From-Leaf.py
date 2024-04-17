# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    start = ord('a')

    def dfs(self, node: Optional[TreeNode], chars: str) -> str:
        chars = chr(self.start + node.val) + chars

        if node.left and node.right:
            return min(
                self.dfs(node.left, chars),
                self.dfs(node.right, chars),
            )

        if node.right:
            return self.dfs(node.right, chars)
        if node.left:
            return self.dfs(node.left, chars)
        return chars

    def smallestFromLeaf(self, root: TreeNode) -> str:
        return self.dfs(root, "")
