# `reduce` and `xor` are already imported in LeetCode
from functools import reduce
from operator import xor


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xored = reduce(xor, nums)
        diff_bit = 1
        while not (xored & diff_bit):
            diff_bit <<= 1

        a = 0
        b = 0
        for num in nums:
            if diff_bit & num:
                a ^= num
            else:
                b ^= num

        return a, b
