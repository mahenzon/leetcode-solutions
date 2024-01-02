class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        total = len(nums)
        max_val = total + 1
        default = -max_val

        # get rid of negative values
        for idx, num in enumerate(nums):
            if num < 0:
                nums[idx] = 0

        # mark positive values that are present
        for num in nums:
            idx = abs(num) - 1
            if idx >= total or idx < 0:
                continue
            val = abs(nums[idx])
            nums[idx] = -val if val else default

        # find min missing positive
        for i in range(total):
            if nums[i] >= 0:
                return i + 1

        return max_val
