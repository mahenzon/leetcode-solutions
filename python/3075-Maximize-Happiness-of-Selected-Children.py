class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        dec = 0
        for idx in range(k):
            res += max(0, happiness[idx] - dec)
            dec += 1

        return res
