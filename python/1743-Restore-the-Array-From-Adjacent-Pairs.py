# `defaultdict` is already imported in LeetCode
from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        result = []
        graph = defaultdict(list)

        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)

        for num, neighbours in graph.items():
            if len(neighbours) == 1:
                result.append(num)
                result.append(neighbours[0])
                break

        while len(result) <= len(adjacentPairs):
            last = result[-1]
            prev = result[-2]
            neighbours = graph[last]
            if neighbours[0] == prev:
                result.append(neighbours[1])
            else:
                result.append(neighbours[0])

        return result
