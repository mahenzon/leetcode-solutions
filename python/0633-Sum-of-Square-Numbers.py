# `math.sqrt` is already imported in LeetCode
from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))
        while left <= right:
            total = left**2 + right**2
            if total == c:
                return True

            if total > c:
                right -= 1
            else:
                left += 1

        return False
