class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # [0, 1, 2] -> sum = 3
        # [0, 1, 2, 3] -> sum = 6

        # [0, 1, 3] -> sum = 4, missing 2
        # total present: 3
        # 3 + (idx num sum) = 3 + sum(range(len(nums))) = 3 + (0 + 1 + 2) = 6
        # 6 - 0 - 1 - 3 = 2 <- result
        # range(len(nums)) is range for [0, n) where n is number if nums
        total = len(nums) + sum(range(len(nums)))
        return total - sum(nums)
