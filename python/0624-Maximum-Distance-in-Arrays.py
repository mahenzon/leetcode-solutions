class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_value = 10_000
        max_value = -10_000
        res = 0

        for arr in arrays:
            res = max(res, arr[-1] - min_value, max_value - arr[0])
            min_value = min(min_value, arr[0])
            max_value = max(max_value, arr[-1])

        return res
