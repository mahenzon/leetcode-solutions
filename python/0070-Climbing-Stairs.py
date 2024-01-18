class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        current = 1
        for _ in range(n - 1):
            prev, current = current, prev + current

        return current
