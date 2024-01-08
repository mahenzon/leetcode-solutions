# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    NULL = "N"
    SPLIT = "|"

    def _serialize_node(self, node: Optional[TreeNode]) -> None:
        if node is None:
            self.values.append(self.NULL)
            return
        self.values.append(str(node.val))
        self._serialize_node(node.left)
        self._serialize_node(node.right)

    def _deserialize_tree(self) -> Optional[TreeNode]:
        val = self.deserialized_values[self.idx]
        if val == self.NULL:
            self.idx += 1
            return None

        root = TreeNode(int(val))
        self.idx += 1
        root.left = self._deserialize_tree()
        root.right = self._deserialize_tree()
        return root

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.values: List[str] = []
        self._serialize_node(root)
        return self.SPLIT.join(self.values)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.deserialized_values = data.split(self.SPLIT)
        self.idx = 0
        return self._deserialize_tree()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
