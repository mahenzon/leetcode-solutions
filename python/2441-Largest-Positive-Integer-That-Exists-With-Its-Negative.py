class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = -1
        seen = {}
        for num in nums:
            v = abs(num)
            if v in seen and -num == seen[v] and v > res:
                res = v
            else:
                seen[v] = num
        return res
