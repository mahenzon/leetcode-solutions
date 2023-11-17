class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        len_nums = len(nums)
        return max(
            nums[i] + nums[len_nums - i - 1]
            for i in range(len_nums // 2)
        )
