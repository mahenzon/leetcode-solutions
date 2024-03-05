class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        res = 0
        score = 0
        tokens.sort()
        left = 0
        right = len(tokens) - 1
        for _ in range(len(tokens)):
            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                score += 1
                res = max(res, score)
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1

        return res
