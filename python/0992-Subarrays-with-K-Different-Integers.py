import collections
from typing import List


class Solution:
    def subarrays_with_at_most_k_distinct(self, k: int) -> int:
        res = 0
        counts = collections.defaultdict(int)

        left = 0
        for right, num in enumerate(self.nums):
            counts[num] += 1
            if counts[num] == 1:
                k -= 1
            while k < 0:
                left_val = self.nums[left]
                counts[left_val] -= 1
                if not counts[left_val]:
                    k += 1
                left += 1

            res += right - left + 1

        return res

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        self.nums = nums
        return self.subarrays_with_at_most_k_distinct(k) - self.subarrays_with_at_most_k_distinct(k - 1)
