# `collections` is already imported in LeetCode
import collections


class Solution:
    modulo = 10 ** 9 + 7

    def rev(self, num):
        res = 0
        while num:
            res = res * 10 + (num % 10)
            num //= 10
        return res

    def countNicePairs(self, nums: List[int]) -> int:
        result = 0

        freqs = collections.Counter(
            num - self.rev(num)
            for num in nums
        )

        result = sum(
            freq * (freq - 1) // 2
            for freq in freqs.values()
        )

        return result % self.modulo
