class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        left = 0
        product = 1
        for right, val in enumerate(nums):
            product *= val
            while left <= right and product >= k:
                product //= nums[left]
                left += 1
            res += (right - left + 1)
        return res
