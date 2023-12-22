# https://leetcode.com/problems/max-consecutive-ones-ii/
# https://www.lintcode.com/problem/883/

class Solution:
    def find_max_consecutive_ones(self, nums):
        """
        @param nums: a list of integer
        @return: return a integer, denote  the maximum number of consecutive 1s
        """
        zeros = 0
        left = 0
        result = 0
        for right, num in enumerate(nums):
            if num == 0:
                zeros += 1
            while zeros == 2:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            result = max(result, right - left + 1)

        return result
