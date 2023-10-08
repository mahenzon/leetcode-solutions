import math
from collections import defaultdict


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        len_m = len(nums1)
        len_n = len(nums2)

        cache = defaultdict(lambda: defaultdict(lambda: -math.inf))

        for i in range(len_m):
            for j in range(len_n):
                next_for_i = cache[i + 1][j]
                next_for_j = cache[i][j + 1]
                current_max = max(cache[i][j], 0) + nums1[i] * nums2[j]

                cache[i + 1][j + 1] = max(
                    next_for_i,
                    next_for_j,
                    current_max,
                )

        return cache[len_m][len_n]
