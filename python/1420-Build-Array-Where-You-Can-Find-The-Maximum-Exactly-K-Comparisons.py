from collections import defaultdict


class Solution:
    modulo = 10 ** 9 + 7

    def solve(self, idx: int, list_len: int, largest: int) -> int:
        if idx == self.n:
            if list_len == self.k:
                return 1
            return 0

        if largest in self.cache[idx][list_len]:
            return self.cache[idx][list_len][largest]

        res = 0
        for i in range(1, self.m + 1):
            if i > largest:
                res += self.solve(idx + 1, list_len + 1, i)
            else:
                res += self.solve(idx + 1, list_len, largest)

        res = res % self.modulo
        self.cache[idx][list_len][largest] = res
        return res

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        self.cache = defaultdict(lambda: defaultdict(dict))
        self.n = n
        self.k = k
        self.m = m
        return self.solve(0, 0, 0)
