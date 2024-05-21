# `combinations` is already imported in LeetCode
from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        for length in range(1, len(nums) + 1):
            results.extend(combinations(nums, length))
        return results
