class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_n = max(nums)
        max_count = 0
        left = 0
        result = 0
        for num in nums:
            max_count += num == max_n
            while max_count == k:
                if nums[left] == max_n:
                    max_count -= 1
                left += 1
            result += left

        return result
