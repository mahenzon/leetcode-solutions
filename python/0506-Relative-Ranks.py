class Solution:
    medals = (
        "Gold Medal",
        "Silver Medal",
        "Bronze Medal",
    )
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        result = [""] * len(score)
        scores = iter(sorted(enumerate(score), key=lambda x: -x[1]))
        for medal, (idx, _) in zip(self.medals, scores):
            result[idx] = medal
        for medal, (idx, _) in enumerate(scores, start=len(self.medals) + 1):
            result[idx] = str(medal)
        return result
