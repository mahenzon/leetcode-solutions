class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        idx_pos = 0
        idx_neg = 1
        for num in nums:
            if num > 0:
                result[idx_pos] = num
                idx_pos += 2
            else:
                result[idx_neg] = num
                idx_neg += 2

        return result
