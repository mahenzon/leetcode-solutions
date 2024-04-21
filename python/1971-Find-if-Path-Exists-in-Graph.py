# `collections` is already imported in LeetCode
import collections


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if destination == source:
            return True

        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        if not (source in graph and destination in graph):
            return False

        to_visit = collections.deque()
        to_visit.extend(graph[source])
        visited = {source}

        while to_visit:
            ver = to_visit.popleft()
            if ver in visited:
                continue
            if ver == destination:
                return True
            visited.add(ver)
            to_visit.extend(graph[ver])

        return False
