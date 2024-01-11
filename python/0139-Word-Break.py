class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        cache = [0] * (n + 1)
        cache[n] = 1

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                w_end = i + len(word)
                if w_end <= n and s[i:w_end] == word:
                    cache[i] = cache[w_end]
                if cache[i]:
                    break

        return cache[0]
