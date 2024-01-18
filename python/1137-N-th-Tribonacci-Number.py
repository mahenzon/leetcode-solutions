class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = 1
        t2 = 1
        for _ in range(n):
            t0, t1, t2 = t1, t2, t0 + t1 + t2

        return t0
