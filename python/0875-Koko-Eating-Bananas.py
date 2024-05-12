# `math` is already imported in LeetCode
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            speed = left + (right - left) // 2

            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / speed)

            if total_time <= h:
                res = speed
                right = speed - 1
            else:
                left = speed + 1

        return res
