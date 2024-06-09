class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        total = 0
        prefix_sums = {total: 1}

        for num in nums:
            total += num
            diff = total - k

            result += prefix_sums.get(diff, 0)
            prefix_sums[total] = 1 + prefix_sums.get(total, 0)

        return result
