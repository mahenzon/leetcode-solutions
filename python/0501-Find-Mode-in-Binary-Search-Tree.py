# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, node: Optional[TreeNode]) -> None:
        if not node:
            return

        self.inorder(node.left)
        if self.prev_node:
            # node has parent
            if node.val == self.prev_node.val:
                self.count += 1
            else:
                self.count = 1

        if self.count > self.max_count:
            self.modes.clear()
            self.modes.append(node.val)
            self.max_count = self.count
        elif self.count == self.max_count:
            self.modes.append(node.val)

        self.prev_node = node
        self.inorder(node.right)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.modes = []
        self.max_count = 0
        self.count = 1
        self.prev_node = None

        self.inorder(root)

        return self.modes
