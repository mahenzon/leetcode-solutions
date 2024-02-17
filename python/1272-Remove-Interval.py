# https://leetcode.com/problems/remove-interval/
# https://www.lintcode.com/problem/3678/

from typing import (
    List,
)

class Solution:
    def delete_interval(self, intervals: List[List[int]], to_be_removed: List[int]) -> List[List[int]]:
        """
        @param intervals: A sorted list of disjoint intervals.
        @param to_be_removed: An interval to be removed.
        @return: A sorted list of intervals.
        """
        result = []
        left_boundary, right_boundary = to_be_removed
        for left, right in intervals:
            if left >= right_boundary or right <= left_boundary:
                result.append([left, right])
                continue

            if left < left_boundary:
                result.append([left, left_boundary])
            if right > right_boundary:
                result.append([right_boundary, right])

        return result
