class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for idx in range(len(points) - 1):
            x1, y1 = points[idx]
            x2, y2 = points[idx + 1]
            res += max(abs(x1 - x2), abs(y1 - y2))
        return res
