# `defaultdict` is already imported in LeetCode

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        current_sum = 0
        res = 0
        prefix_count = defaultdict(int)
        prefix_count[current_sum] = 1

        for num in nums:
            current_sum += num
            remainder = current_sum % k

            if remainder in prefix_count:
                res += prefix_count[remainder]
            prefix_count[remainder] += 1

        return res
