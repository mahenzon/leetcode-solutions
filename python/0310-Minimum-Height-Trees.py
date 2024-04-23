# `collections` is already imported in LeetCode
import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = collections.defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        edges_count = {}
        leaves = collections.deque()
        for src, neighbors in graph.items():
            edges_count[src] = len(neighbors)
            if edges_count[src] == 1:
                leaves.append(src)

        while leaves:
            if n <= 2:
                return list(leaves)
            for _ in range(len(leaves)):
                n -= 1
                val = leaves.popleft()
                for neigbor in graph[val]:
                    edges_count[neigbor] -= 1
                    if edges_count[neigbor] == 1:
                        leaves.append(neigbor)
