class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 1
        count = 1
        prev_num = nums[0]
        for idx in range(1, len(nums)):
            if prev_num < nums[idx]:
                count += 1
                res = max(res, count)
            else:
                count = 1
            prev_num = nums[idx]
        return res
