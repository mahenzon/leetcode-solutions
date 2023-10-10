class Solution:
    def minOperations(self, nums: List[int]) -> int:
        initial_nums_length = len(nums)
        sorted_unique_nums = list(sorted(set(nums)))
        sorted_unique_nums_len = len(sorted_unique_nums)
        right = 0
        result = initial_nums_length

        for left in range(sorted_unique_nums_len):
            target_max = sorted_unique_nums[left] + initial_nums_length
            while right < sorted_unique_nums_len and sorted_unique_nums[right] < target_max:
                right += 1

            diff_len = right - left
            result = min(result, initial_nums_length - diff_len)

        return result
