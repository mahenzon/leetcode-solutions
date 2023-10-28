class Solution:
    def countVowelPermutation(self, n: int) -> int:
        modulo = 10 ** 9 + 7
        cache = [1, 1, 1, 1, 1]
        a = 0
        e = 1
        i = 2
        o = 3
        u = 4

        for _ in range(n - 1):
            prev = list(cache)
            cache[a] = (prev[e] + prev[i] + prev[u]) % modulo
            cache[e] = (prev[a] + prev[i]) % modulo
            cache[i] = (prev[e] + prev[o]) % modulo
            cache[o] = prev[i]
            cache[u] = (prev[i] + prev[o]) % modulo

        return sum(cache) % modulo
