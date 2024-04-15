class Solution:
    def dfs(self, node: Optional[TreeNode], total: int) -> int:
        if not node:
            return 0

        total = total * 10 + node.val
        if not (node.left or node.right):
            return total

        return self.dfs(node.left, total) + self.dfs(node.right, total)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
