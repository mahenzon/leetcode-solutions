class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        for n in sorted(arr):
            if n not in rank:
                rank[n] = len(rank) + 1
        return [rank[n] for n in arr]
