class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        left = 0

        for right in range(1, len(colors)):
            if colors[left] == colors[right]:
                if neededTime[left] < neededTime[right]:
                    total_time += neededTime[left]
                    left = right
                else:
                    total_time += neededTime[right]
            else:
                left = right

        return total_time
