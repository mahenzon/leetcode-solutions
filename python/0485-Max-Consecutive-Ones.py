class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for num in nums:
            if num:
                count += 1
                res = max(res, count)
            else:
                count = 0
        return res
