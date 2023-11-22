# `defaultdict` is already imported in LeetCode
from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        items = defaultdict(list)
        for i, inner_list in enumerate(nums):
            for j, num in enumerate(inner_list):
                items[i + j].append(num)

        result = []
        for values in items.values():
            result.extend(values[::-1])

        return result
