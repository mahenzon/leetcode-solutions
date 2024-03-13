# `sqrt` from `math` is already imported in LeetCode
from math import sqrt


class Solution:
    def pivotInteger(self, n: int) -> int:
        x = sqrt(n * (n + 1) / 2)
        if x % 1:
            return -1
        return int(x)
