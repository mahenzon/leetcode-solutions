class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        total = 0
        satisfaction_total = 0
        for s in sorted(satisfaction, reverse=True):
            satisfaction_total += s
            if satisfaction_total <= 0:
                return total
            total += satisfaction_total
        return total
