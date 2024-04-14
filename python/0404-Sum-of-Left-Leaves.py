class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        if root.left:
            node = root.left
            if node.left or node.right:
                res += self.sumOfLeftLeaves(node)
            else:
                res += node.val

        res += self.sumOfLeftLeaves(root.right)
        return res
