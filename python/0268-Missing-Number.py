class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # [0, 1, 2] -> sum = 3
        # [0, 1, 2, 3] -> sum = 6

        # [0, 1, 3] -> sum = 4, missing 2
        return sum(range(len(nums) + 1)) - sum(nums)
