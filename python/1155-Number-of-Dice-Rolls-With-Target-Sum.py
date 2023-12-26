class Solution:

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7
        # cache[i] -> num of ways to roll i dice
        cache = [0] * (target + 1)
        cache[0] = 1

        for _ in range(n):
            next_cache = [0] * (target + 1)

            for val in range(1, k + 1):
                for total in range(val, target + 1):
                    next_cache[total] = (next_cache[total] + cache[total - val]) % mod

            cache = next_cache

        return cache[target]
