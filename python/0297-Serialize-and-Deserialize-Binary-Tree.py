# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    SEP = "|"
    NULL = "N"

    def serialize_preorder(self, root) -> list[str]:
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node is None:
                res.append(self.NULL)
                continue
            res.append(str(node.val))
            stack.append(node.right)
            stack.append(node.left)
        return res

    def read_preorder(self, values: list[str]) -> Optional[TreeNode]:
        val = values.pop()
        if val == self.NULL:
            return None

        node = TreeNode(int(val))
        node.left = self.read_preorder(values)
        node.right = self.read_preorder(values)
        return node

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self.SEP.join(self.serialize_preorder(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        values = data.split(self.SEP)
        values.reverse()
        return self.read_preorder(values)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
