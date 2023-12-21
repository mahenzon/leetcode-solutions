class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()

        res = 0
        prev = points[0][0]
        for x, _ in points:
            res = max(res, x - prev)
            prev = x

        return res
