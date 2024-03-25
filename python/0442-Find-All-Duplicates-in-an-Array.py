class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for val in nums:
            v = abs(val)
            idx = v - 1
            if nums[idx] < 0:
                result.append(v)
            else:
                nums[idx] *= -1
        return result
