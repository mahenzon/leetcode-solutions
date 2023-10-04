class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right]:
                # this condition is optional,
                # just to skip an unnecessary swap
                if left != right:
                    nums[left], nums[right] = nums[right], nums[left]
                left += 1
