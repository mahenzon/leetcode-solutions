class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        res = 0
        for pos in right:
            res = max(res, n - pos)

        for pos in left:
            res = max(res, pos)

        return res
