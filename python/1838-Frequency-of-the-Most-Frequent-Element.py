class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        total = 0

        left = 0
        for right, num in enumerate(nums):
            total += num

            while num * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1

            result = max(result, right - left + 1)

        return result
