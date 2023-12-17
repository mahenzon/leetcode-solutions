# https://leetcode.com/problems/line-reflection/
# https://www.lintcode.com/problem/908/

from typing import (
    List,
)


class Solution:
    """
    @param points: n points on a 2D plane
    @return: if there is such a line parallel to y-axis that reflect the given points
    """

    def is_reflected(self, points: List[List[int]]) -> bool:
        if not points:
            return True

        points_set = set()
        max_x = points[0][0]
        min_x = points[0][0]
        for x, y in points:
            points_set.add((x, y))
            max_x = max(max_x, x)
            min_x = min(min_x, x)

        dist = max_x + min_x

        for x, y in points:
            if (dist - x, y) not in points_set:
                return False

        return True
