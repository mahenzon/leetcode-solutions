class Solution:
    def rob(self, nums: List[int]) -> int:
        sum_one = 0
        sum_two = 0

        for n in nums:
            sum_one, sum_two = sum_two, max(n + sum_one, sum_two)

        return sum_two
