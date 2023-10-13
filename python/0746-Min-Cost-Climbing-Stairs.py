class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        idx = len(cost) - 1
        cost.append(0)
        while idx:
            idx -= 1
            cost[idx] += min(
                cost[idx + 1],
                cost[idx + 2],
            )
        return min(cost[0], cost[1])
