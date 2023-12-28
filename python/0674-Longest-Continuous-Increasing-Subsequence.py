# Longer code, faster solution
# Runtime 58 ms Beats 99.22%
# Memory 18.7 MB Beats 11.15%


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 1
        count = 1
        prev_num = nums[0]
        for idx in range(1, len(nums)):
            if prev_num < nums[idx]:
                count += 1
                res = max(res, count)
            else:
                count = 1
            prev_num = nums[idx]
        return res


# Shorted code, slower solution
# Runtime 129 ms Beats 6.9%
# Memory 18.8 MB Beats 8.82%


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 1
        last = 0
        for idx in range(1, len(nums)):
            if not (nums[idx] > nums[idx - 1]):
                last = idx
            res = max(res, idx - last + 1)
        return res
