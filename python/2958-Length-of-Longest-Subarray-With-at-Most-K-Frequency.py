from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        result = 0

        counts = defaultdict(int)
        left = 0
        for right, val in enumerate(nums):
            counts[val] += 1
            while counts[val] > k:
                counts[nums[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result
