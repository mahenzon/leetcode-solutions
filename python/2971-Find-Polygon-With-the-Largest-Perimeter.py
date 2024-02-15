class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res = -1
        total = 0
        for num in nums:
            if total > num:
                res = total + num
            total += num
        return res
