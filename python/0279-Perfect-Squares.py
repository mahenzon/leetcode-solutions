class Solution:
    def numSquares(self, n: int) -> int:
        cache = [n] * (n + 1)
        cache[0] = 0
        cache[1] = 1

        for target in range(2, n + 1):
            num = 1
            while (sq := num * num) <= target:
                cache[target] = min(cache[target], cache[target - sq] + 1)
                num += 1

        return cache[n]
