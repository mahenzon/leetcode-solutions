class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        left = 1
        right = 2 ** (n - 1)
        res = 0

        for _ in range(n - 1):
            mid = (left + right) // 2
            if k <= mid:
                right = mid
            else:
                left = mid + 1
                res = 0 if res else 1

        return res
