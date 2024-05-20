# `operator` is already imported in LeetCode
# `functools` is already imported in LeetCode
# `combinations` is already imported in LeetCode
import operator
from functools import reduce
from itertools import combinations


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        for length in range(1, len(nums) + 1):
            for combination in combinations(nums, length):
                result += reduce(operator.xor, combination)

        return result
        # faster and shorter, but harder to get
        # return reduce(operator.or_, nums) << len(nums) - 1
