class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        cache = [0] * 26
        for c in s:
            current = ord(c) - ord("a")
            longest = 1
            for prev in range(26):
                if abs(current - prev) <= k:
                    longest = max(longest, cache[prev] + 1)
            cache[current] = max(cache[current], longest)

        return max(cache)
