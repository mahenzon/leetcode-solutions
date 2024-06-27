class Solution:

    def inorder(self, node: TreeNode | None) -> TreeNode | None:
        if not node:
            return
        self.inorder(node.left)
        self.nums.append(node.val)
        self.inorder(node.right)

    def build(self, left: int, right: int) -> TreeNode | None:
        if left > right:
            return

        mid = left + (right - left) // 2
        return TreeNode(
            self.nums[mid],
            self.build(left, mid - 1),
            self.build(mid + 1, right),
        )

    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.nums = []
        self.inorder(root)
        return self.build(0, len(self.nums) - 1)
