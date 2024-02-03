class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        cache = [0] * (n + 1)

        for i in range(1, n + 1):
            v = -1
            for j in range(1, min(i, k) + 1):
                v = max(v, arr[i - j])
                cache[i] = max(cache[i], cache[i - j] + v * j)

        return cache[n]
