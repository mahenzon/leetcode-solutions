class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = None
        count = 0

        for num in nums:
            if count == 0:
                res = num
                count += 1
            elif res == num:
                count += 1
            else:
                count -= 1

        return res
