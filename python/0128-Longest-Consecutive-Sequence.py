class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in nums_set:
                seq_len = 0
                while (n + seq_len) in nums_set:
                    seq_len += 1
                longest = max(longest, seq_len)

        return longest
