# `math` is already imported in LeetCode
import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # num: count
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        res = 0
        for count in counts.values():
            if count > 1:
                res += math.ceil(count / 3)
            else:
                return -1

        return res
