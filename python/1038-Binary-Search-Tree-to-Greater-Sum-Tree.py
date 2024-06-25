class Solution:

    def dfs(self, node: TreeNode | None) -> None:
        if not node:
            return

        self.dfs(node.right)
        # idk why leetcode thinks this is slow
        # self.current_sum += node.val
        # node.val = self.current_sum
        node.val += self.current_sum
        self.current_sum = node.val
        self.dfs(node.left)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.current_sum = 0
        self.dfs(root)
        return root
