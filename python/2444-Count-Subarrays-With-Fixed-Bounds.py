class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0
        j = -1
        prev_min_k_idx = -1
        prev_max_k_idx = -1

        for idx, num in enumerate(nums):
            if num < minK or num > maxK:
                j = idx
            if num == minK:
                prev_min_k_idx = idx
            if num == maxK:
                prev_max_k_idx = idx

            result += max(0, min(prev_min_k_idx, prev_max_k_idx) - j)
        return result
