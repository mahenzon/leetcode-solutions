# https://leetcode.com/problems/paint-fence
# https://www.lintcode.com/problem/514/


class Solution:
    def num_ways(self, n: int, k: int) -> int:
        """
        @param n: non-negative integer, n posts
        @param k: non-negative integer, k colors
        @return: an integer, the total number of ways
        """
        cache = [0] * (max(n, 3) + 1)
        cache[1] = k
        cache[2] = cache[1] * k

        for i in range(2, n):
            cache[i + 1] = (cache[i] + cache[i - 1]) * (k - 1)
        return cache[n]
