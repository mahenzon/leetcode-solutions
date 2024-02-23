# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])

        stack = [root]
        for idx in range(1, len(preorder)):
            child = TreeNode(preorder[idx])
            parent = stack[-1]
            while stack and stack[-1].val < child.val:
                parent = stack.pop()
            if parent.val < child.val:
                parent.right = child
            else:
                parent.left = child
            stack.append(child)

        return root
