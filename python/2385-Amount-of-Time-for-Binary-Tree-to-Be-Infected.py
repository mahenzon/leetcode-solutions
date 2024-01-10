# `collections` is already imported in LeetCode
import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build_graph(self, node: Optional[TreeNode]):
        if node is None:
            return

        if node.left:
            self.graph[node.val].append(node.left.val)
            self.graph[node.left.val].append(node.val)

        if node.right:
            self.graph[node.val].append(node.right.val)
            self.graph[node.right.val].append(node.val)

        self.build_graph(node.left)
        self.build_graph(node.right)

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.graph = collections.defaultdict(list)
        self.build_graph(root)

        total_time = -1
        visited_values = set()
        values_to_visit = collections.deque([start])
        while values_to_visit:
            total_time += 1
            # traverse current level (one unit of time)
            for _ in range(len(values_to_visit)):
                node_val = values_to_visit.popleft()
                visited_values.add(node_val)
                for neighbour_val in self.graph[node_val]:
                    if neighbour_val not in visited_values:
                        values_to_visit.append(neighbour_val)

        return total_time
